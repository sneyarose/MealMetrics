<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
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

