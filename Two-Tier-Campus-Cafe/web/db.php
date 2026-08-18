<?php

function db_connect(array $cfg): mysqli
{
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    $mysqli = new mysqli($cfg['host'], $cfg['user'], $cfg['pass'], $cfg['name']);
    $mysqli->set_charset('utf8mb4');
    return $mysqli;
}
