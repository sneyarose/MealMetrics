const express = require('express');
const multer = require('multer');
const fastcsv = require('fast-csv');
const csv = require('csv-parser');
const { MongoClient, ObjectId } = require('mongodb');
const fs = require('fs');
const path = require('path');



const app = express();
const port = process.env.PORT || 3000;

// MongoDB connection parameters
const mongoURI = 'mongodb://0.0.0.0:27017'; // Update with your MongoDB URI
const dbName = 'Food'; // Update with your database name
const collectionName = 'f_db'; // Update with your collection name

//update.html............................................................................

// Set up the multer middleware to handle file uploads
const upload = multer({ dest: 'uploads/' });

// Function to connect to MongoDB
async function connectToDB() {
  const client = new MongoClient(mongoURI, { useUnifiedTopology: true }); // Add useUnifiedTopology option
  try {
    await client.connect();
    console.log('Connected to MongoDB successfully!');
    return client.db(dbName).collection(collectionName);
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}

// Function to insert data into MongoDB
async function insertData(collection, data) {
  try {
    await collection.insertMany(data);
    console.log('Data inserted successfully into MongoDB.');
  } catch (error) {
    console.error('Error inserting data into MongoDB:', error);
  }
}

// Function to convert data to the desired format
function convertDataToFormat(data) {
  return data.map((row) => ({
    id: parseInt(row['Sno']),
    name: row['Name'].trim(),
    price: parseFloat(row['Price']),
    order: parseInt(row['Orders']),
    date: formatDate(row['Date']), // Format date as "YYYY-MM-DD"
  }));
}

// Function to format date as "YYYY-MM-DD"
function formatDate(dateString) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// Read and parse the CSV file
function readCSVAndInsertData(filePath, collection) {
  const data = [];
  fs.createReadStream(filePath)
    .pipe(csv({ mapHeaders: ({ header }) => header.trim() }))
    .on('data', (row) => {
      data.push(row);
    })
    .on('end', () => {
      if (data.length > 0) {
        const formattedData = convertDataToFormat(data);
        insertData(collection, formattedData);
      } else {
        console.log('No data found in the CSV.');
      }
    });
}

// Route for handling the file upload
app.post('/upload', upload.single('csvFile'), async (req, res) => {
  const collection = await connectToDB();
  const filePath = req.file.path;

  readCSVAndInsertData(filePath, collection);

  //res.sendFile(__dirname + '/public/Upload.html')
});

//-update.html....................................................................................................


//Home.html......Staff.html.......................................................................................

// Define the route to retrieve data for the last updated date from MongoDB and send it as a JSON response
app.get('/api/foodData', async (req, res) => {
    try {
      const collection = await connectToDB();
  
      // Fetch the last updated date from the latest document in MongoDB
      const lastUpdatedDate = await collection.find().sort({ date: -1 }).limit(1).project({ date: 1 }).toArray();
  
      // Fetch all data with the same date as the last updated date from MongoDB
      const data = await collection.find({ date: lastUpdatedDate[0].date }).toArray();
  
      // Send the data as a JSON response
      res.json(data);
    } catch (error) {
      console.error('Error fetching data from MongoDB:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });
  
 //-Home.html......-Staff.html....................................................................................
  

//mlc.html......................................................................................................

// Middleware to parse incoming JSON data
app.use(express.json());

// API endpoint to fetch data from MongoDB
app.get('/api/get-data-from-mongodb', async (req, res) => {
  try {
    const collection = await connectToDB();
    const data = await collection.find({}).toArray();
    res.json(data);
  } catch (error) {
    console.error('Error fetching data from MongoDB:', error);
    res.status(500).json({ error: 'Error fetching data from MongoDB' });
  }
});

//...............................................................................................................
// Endpoint to store prediction data in MongoDB
app.post('/api/store-predictions', async (req, res) => {
  const predictions = req.body.predictions; // Expecting an array of predictions from the front-end

  try {
    const collection = await connectToDB_MLC();
    await collection.deleteMany({});
    await collection.insertMany(predictions);
    console.log('Predictions stored in MongoDB successfully!');
    res.json({ message: 'Predictions stored in MongoDB successfully!' });
  } catch (error) {
    console.error('Error storing predictions in MongoDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

async function connectToDB_MLC() {
  const client = new MongoClient(mongoURI, { useUnifiedTopology: true });
  try {
    await client.connect();
    console.log('Connected to MongoDB successfully!');
    return client.db(dbName).collection("predict");
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}



//...............................................................................................................



//-mlc.html......................................................................................................

//stat.html......................................................................................................

app.get('/api/foodDataLastWeek', async (req, res) => {
  try {
    const collection = await connectToDB();
    const { foodId } = req.query;

    // Fetch the last updated date from the latest document in MongoDB
    const lastUpdatedDate = await collection.find().sort({ date: -1 }).limit(1).project({ date: 1 }).toArray();

    // Get the date range for last week (from 7 days ago to the last updated date)
    const lastUpdated = new Date(lastUpdatedDate[0].date);
    const lastWeek = new Date(lastUpdated);
    lastWeek.setDate(lastUpdated.getDate() - 7);
    const lastUpdatedISO = lastUpdated.toISOString();
    const lastWeekISO = lastWeek.toISOString();

    console.log('Fetching data from MongoDB for foodId:', foodId);
    console.log('Date range from:', lastWeekISO, 'to', lastUpdatedISO);

    // Fetch data from MongoDB based on the provided food ID and date range
    const data = await collection
      .find({
        id: parseInt(foodId),
        date: { $gte: lastWeekISO, $lte: lastUpdatedISO },
      })
      .toArray();

    console.log('Fetched data:', data);
    const food = await collection.findOne({ id: parseInt(foodId) });

    // If the food exists, get its name; otherwise, use "Unknown Food"
    const foodName = food ? food.name : "Unknown Food";

    const chartData = [['Day', 'Orders']];
    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const dayof=[1,2,3,4,5,6,7];
    i=0
    for (const day of daysOfWeek) {
      const orderData = data.filter(item => {
        const itemDate = new Date(item.date);
        return itemDate.getDay() === daysOfWeek.indexOf(day);
      });
      //const orderData = data.find(item => item.date === day);
      const orders = orderData.reduce((total, item) => total + item.order, 0);
      //const orders = orderData ? orderData.order : 0;
      chartData.push([day, orders]);
      
    }
    console.log(foodName);
    res.json({ foodName, chartData });
    
  } catch (error) {
    console.error('Error fetching data from MongoDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

//-stat.html.............................................................................

//Admin..................................................................................


async function connectToDB_Admin() {
  const client = new MongoClient(mongoURI, { useUnifiedTopology: true }); // Add useUnifiedTopology option
  try {
    await client.connect();
    console.log('Connected to MongoDB successfully!');
    return client.db(dbName).collection("predict");
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}



// Function to retrieve food names by foodid array
app.post('/api/store-Optimal', async (req, res) => {
  const predictions = req.body.combinedArray; // Expecting an array of predictions from the front-end

  try {
    const collection = await connectToDB_addi();
    await collection.deleteMany({});
    await collection.insertMany(predictions);
    console.log('Optimal price stored in MongoDB successfully!');
    res.json({ message: 'Optimal price stored in MongoDB successfully!' });
  } catch (error) {
    console.error('Error storing Price in MongoDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

async function connectToDB_addi() {
  const client = new MongoClient(mongoURI, { useUnifiedTopology: true });
  try {
    await client.connect();
    console.log('Connected to MongoDB successfully!');
    return client.db(dbName).collection("STAFF");
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}


app.use(express.json());

// API endpoint to fetch data from MongoDB
app.get('/api/get-data-from-mongodb_admin', async (req, res) => {
  try {
    const collection = await connectToDB_Admin();
    const data = await collection.find({}).toArray();
    console.log("Success")
    res.json(data);
  } catch (error) {
    console.error('Error fetching data from MongoDB:', error);
    res.status(500).json({ error: 'Error fetching data from MongoDB' });
  }
});



//Admin..................................................................................
//Staff.afa..f...a..f.....a.f............................................................

async function connectToDBStaff() {
  const client = new MongoClient(mongoURI, { useUnifiedTopology: true }); // Add useUnifiedTopology option
  try {
    await client.connect();
    console.log('Connected to MongoDB successfully!');
    return client.db(dbName).collection("STAFF");
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}





app.get('/api/foodPrice', async (req, res) => {
  try {
    const collection = await connectToDBStaff();

    // Fetch the last updated date from the latest document in MongoDB

    // Fetch all data with the same date as the last updated date from MongoDB
    const data = await collection.find({}).toArray();

    // Send the data as a JSON response
    res.json(data);
  } catch (error) {
    console.error('Error fetching data from MongoDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

//staff................a............a......s........a..d.......a....ds...................







//set static folder
app.use(express.static(path.join(__dirname, 'public')));

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
