<?php
if (isset($_SERVER["REQUEST_METHOD"]) && $_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // User credentials
    $users = array(
        "Yadu" => "admin",
        "Sneya" => "manager"
    );

    // Check if the username and password match the desired values
    if (array_key_exists($username, $users) && $users[$username] === $password) {
        // Successful login, redirect to the appropriate page
        if ($username === "Yadu") {
            header("Location: admin.html");
            exit();
        } elseif ($username === "Sneya") {
            header("Location: login.html");
            exit();
        }
    } else {
        // Failed login, redirect back to the login page
        header("Location: login.html");
        exit();
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Roboto', sans-serif;
    }
    .main {
      display: flex;
      width: 100%;
      height: 100vh;
    }
    .logo {
      display: flex;
      justify-content: center;
      align-items: center;
      flex: 65;
      background-image: url("login_bg_new.jpg");
      background-size: cover;
    }
    .login {
      display: flex;
      justify-content: center;
      align-items: center;
      flex: 35;
      background-color: #f1e3d7;
    }
    img {
      margin-left: 30px;
      margin-right: 30px;
      width: 50%;
      height: 200px;
    }
    .img-fluid {
      padding-bottom: 30%;
    }
    .sub-but {
      margin-left: 20px;
      margin-right: 20px;
      border: none;
      background: #f2f2f2;
      padding: 10px 20px;
      border-radius: 10px;
      color: #333;
      font-size: 17px;
      transition: background-color 0.6s ease; /* Slower transition for the background color change on hover */
    }
    .form-group {
      margin-left: 20%;
      margin-right: 20%;
    }
    .sub-but:hover {
      background-color: #fd7048; /* Orange-skin color on hover */
    }
    /* Click animation with green color */
    .sub-but:active {
      background-color: #01850c; /* Green color when clicked */
      transform: scale(0.95); /* Slight scale down effect when clicked */
    }
    .sub-but:focus {
      animation: pulse 1s ease infinite; /* Slower pulse animation */
      outline: none; /* Remove the default focus outline from the button */
    }

    @keyframes pulse {
      0% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.05); /* Slightly larger scale for the pulse effect */
      }
      100% {
        transform: scale(1);
      }
    }

    /* Additional style for successful login */
    .login-success {
      border-color: #01850c; /* Green color for the button border */
    }
  </style>
</head>

<body>
  <div class="main">
    <div class="logo">
      <img src="logo_new-removebg-preview.png" class="img-fluid" alt="Logo" />
    </div>
    <div class="login">
      <div class="container">
        <h1 class="text-center">Login</h1>
        <br><br><br>
        <form action="Home.html">
          <div class="form-group">
            <input name="username" type="text" class="form-control" placeholder="Username" />
          </div>
          <div class="form-group">
            <input name="password" type="password" class="form-control" placeholder="Password" />
          </div>
          <div class="form-group text-center">
            <br>
            <button class="btn btn-primary sub-but" type="button" onclick="login()" onblur="this.blur()">
              Submit
            </button>
            <br><br><br>
            <a href="Staff.html" style="color: #fd7048">Staff View</a>
          </div>
        </form>
      </div>
    </div>
  </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <script>
    function login() {
      var username = document.querySelector('input[name="username"]').value;
      var password = document.querySelector('input[name="password"]').value;
      var submitButton = document.querySelector('.sub-but');

      if (username === "Yadu" && password === "admin") {
        submitButton.classList.add('login-success');
        setTimeout(function() {
          window.location.href = "admin.html";
        }, 1000);
      } else if (username === "Sneya" && password === "manager") {
        submitButton.classList.add('login-success');
        setTimeout(function() {
          window.location.href = "home.html";
        }, 1000);
      } else {
        alert("Access denied. Invalid username or password.");
      }
    }
  </script>
</body>
</html>
