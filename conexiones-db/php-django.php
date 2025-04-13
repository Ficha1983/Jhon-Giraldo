<?php
$url = "http://localhost:8000/api/productos/";
$response = file_get_contents($url);
echo $response;
?>
