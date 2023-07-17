import csv
from pymongo import MongoClient

class fdb():
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')

        # Select the database and collection
        self.db = client['mydatabase']
        self.collection = self.db['foodItems']

    def add_item(self, sr, name, price, nord, date):
        # Create a new document
        new_item = {
            'Sno':sr,
            'Food Name': name,
            'Price': price,
            'Orders':nord,
            'Date':date
        }

        # Insert the document into the collection
        self.collection.insert_one(new_item)

    def get_items(self):
        # Retrieve all documents from the collection
        items = self.collection.find()

        # Convert the documents to a list
        item_list = []
        for item in items:
            item_list.append(item)



    #csv convert
        with open('food_db.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            ti_li = ["Sno", "Food Name","Price","Orders", "Date"]
            writer.writerow(ti_li)
            for i in range(len(item_list)):
                c=item_list[i]
                temp = []
                temp.append(c['Sno'])
                temp.append(c['Food Name'])
                temp.append(c['Price'])
                temp.append(c['Orders'])
                temp.append(c['Date'])
                writer.writerow(temp)




if __name__ == '__main__':
    fd=fdb()
    fd.add_item(99,'sample',2,10,"1010-10-10") #testing function
    fd.get_items()
