<?php
session_start(); 
?>
<!DOCTYPE html>
<html>
<head>
  <title>Very Secure Server</title>
<h1> Welcome to Very Secure Server </h1>
</head>
<body>
  <?php
    if (isset($_SESSION['message']) && $_SESSION['message'])
    {
      printf('<b>%s</b>', $_SESSION['message']);
      unset($_SESSION['message']);
    }
  ?>
  <form method="POST" action="upload.php" enctype="multipart/form-data">
    <div>
      <span>Upload a File:</span>
      <input type="file" name="uploadedFile" />
    </div>

    <input type="submit" name="uploadBtn" value="Upload" />
  </form>
</body>
<h1> Developed By Bekar Company</h1>
</html>
