<?php
require_once '../vendor/autoload.php';
require_once '../src/weatherApp.php';



if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET['location'])) {
    $location = $_GET['location'];
    
    $response = $app->generateWeatherEmail();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Weather Information</h1>
        <form action="index.php" method="get">
            <input type="text" name="location" placeholder="Enter a location" required>
            <button type="submit">Get Weather</button>
        </form>
        <?php if(isset($response)): ?>
            <div class="weather-response">
                <?php echo nl2br($response); ?>
            </div>
        <?php endif; ?>
    </div>
</body>
</html>

