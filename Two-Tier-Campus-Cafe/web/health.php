<?php
header('Content-Type: application/json');

$cfg = require __DIR__ . '/config.php';
require __DIR__ . '/db.php';

$payload = [
    'status' => 'ok',
    'tier' => 'web',
    'db_host' => $cfg['host'],
    'database' => 'disconnected',
];

try {
    $db = db_connect($cfg);
    $row = $db->query('SELECT COUNT(*) AS n FROM menu_items')->fetch_assoc();
    $payload['database'] = 'connected';
    $payload['menu_items'] = (int) $row['n'];
    $db->close();
} catch (Throwable $e) {
    http_response_code(503);
    $payload['status'] = 'degraded';
    $payload['error'] = 'database unreachable';
}

echo json_encode($payload, JSON_PRETTY_PRINT) . "\n";
