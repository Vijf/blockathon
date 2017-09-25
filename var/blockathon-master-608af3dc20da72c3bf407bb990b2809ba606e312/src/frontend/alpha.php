<!DOCTYPE html>
<html>
<body>

<center>

<form action="upload.php" method="post" enctype="multipart/form-data">
    Selecteer een bestand om te uploaden: <br /> <br />
    <input type="file" name="fileToUpload" id="fileToUpload">
    <br /><br />
    <textarea name="textbox" type="text"></textarea>
    <br /><br />

    <?php
        $format = '<input type="hidden" name="idnummer" value="%s">';
        echo sprintf($format, $_GET['sticker'])
    ?>

    <input type="submit" value="Verzend informatie" name="submit">
</form>

</center>


</body>
</html>