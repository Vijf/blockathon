<?php

$myfile = fopen("/usr/share/nginx/html/chain/images/ae7b5414d1bca1f90aa8dde7fb3d947d66693b1e0e871f0a14f5001c8ec8c622", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/usr/share/nginx/html/chain/images/ae7b5414d1bca1f90aa8dde7fb3d947d66693b1e0e871f0a14f5001c8ec8c622"));
fclose($myfile);


$dir = '/usr/share/blockathon/chain/images/';

if (is_dir($dir)) {
    if ($dh = opendir($dir)) {
        while (($file = readdir($dh)) !== false)
        {
            echo "filename: .".$file."<br />";

            $fileoutput = file_get_contents('$file');
            echo $fileoutput;
        }
        closedir($dh);
    }
}

?>