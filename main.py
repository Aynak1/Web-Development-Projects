<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Will You Be My Date?</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-image: url('https://source.unsplash.com/1600x900/?red-roses');
      background-size: cover;
      margin: 0;
      padding: 0;
      overflow: hidden; /* Prevent scrolling */
    }
    .container {
      max-width: 600px;
      margin: 100px auto;
      padding: 20px;
      background-color: rgba(255, 255, 255, 0.8);
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      border: 1px solid #ccc;
      text-align: center; /* Center align content */
      position: relative; /* For absolute positioning of flower */
    }
    h1 {
      color: #333;
    }
    p {
      color: #666;
      margin-bottom: 20px;
    }
    .button-container {
      margin-left: -65px; /* Move buttons more to the left */
    }
    .yes-button,
    .no-button {
      margin: 0 10px; /* Add space between buttons */
    }
    .yes-button {
      background-color: #ff6b6b;
      color: #fff;
      border: none;
      padding: 10px 20px;
      font-size: 18px;
      border-radius: 5px;
      cursor: pointer;
    }
    .no-button {
      background-color: #ccc;
      color: #333;
      border: none;
      padding: 10px 20px;
      font-size: 18px;
      border-radius: 5px;
      cursor: pointer;
      position: absolute;
      transition: left 0.5s ease, top 0.5s ease;
    }
    .popup {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      display: none;
      justify-content: center;
      align-items: center;
    }
    .popup img {
      max-width: 90%;
      max-height: 90%;
      border-radius: 10px;
    }
    .popup-text {
      color: white;
      font-size: 24px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Will You Be My Date?</h1>
    <p>Hey there! I have something important to ask...</p>
    <p>Would you do me the honor of being my date?</p>
    <div class="button-container">
      <button class="yes-button" onclick="sendResponse('Yes')">Yes, I'd love to!</button>
      <button class="no-button" onclick="moveNoButton()">No, I can't</button>
    </div>
  </div>
  <div class="popup" id="popup">
    <img src="https://source.unsplash.com/1600x900/?anime-couple" alt="Anime Couple">
    <div class="popup-text">Let's start our journey together</div>
  </div>
  <script>
    function sendResponse(response) {
      if (response === 'Yes') {
        document.querySelector('.yes-button').style.display = 'none';
        document.querySelector('.no-button').style.display = 'none';
        document.getElementById('popup').style.display = 'flex';
      }
    }

    function moveNoButton() {
      var button = document.querySelector('.no-button');
      var newPositionLeft = Math.random() * (window.innerWidth - button.offsetWidth);
      var newPositionTop = Math.random() * (window.innerHeight - button.offsetHeight);
      button.style.left = newPositionLeft + 'px';
      button.style.top = newPositionTop + 'px';
    }
  </script>
</body>
</html>
