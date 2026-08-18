<?php
/**
 * Load DB settings from environment (Docker / systemd) or a local .env file (VMs).
 */

function load_env_file(string $path): void
{
    if (!is_readable($path)) {
        return;
    }

    $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if ($lines === false) {
        return;
    }

    foreach ($lines as $line) {
        $line = trim($line);
        if ($line === '' || $line[0] === '#') {
            continue;
        }
        if (strpos($line, '=') === false) {
            continue;
        }
        [$name, $value] = explode('=', $line, 2);
        $name = trim($name);
        $value = trim($value);
        if ($name === '') {
            continue;
        }
        if (getenv($name) === false) {
            putenv("{$name}={$value}");
            $_ENV[$name] = $value;
        }
    }
}

function env_value(string $key, string $default = ''): string
{
    $value = getenv($key);
    if ($value === false || $value === '') {
        return $default;
    }
    return $value;
}

load_env_file(__DIR__ . '/.env');

return [
    'host' => env_value('DB_HOST', 'localhost'),
    'user' => env_value('DB_USER', 'cafeuser'),
    'pass' => env_value('DB_PASSWORD', 'cafepass'),
    'name' => env_value('DB_NAME', 'campuscafe'),
];
