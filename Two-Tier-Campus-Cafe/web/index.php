<?php
$cfg = require __DIR__ . '/config.php';
require __DIR__ . '/db.php';

$error = '';
$notice = '';
$menu = [];
$orders = [];
$connected = false;

try {
    $db = db_connect($cfg);
    $connected = true;

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $student = trim($_POST['student_name'] ?? '');
        $itemId = (int) ($_POST['item_id'] ?? 0);

        if ($student === '' || $itemId < 1) {
            $error = 'Enter your name and pick a menu item.';
        } else {
            $stmt = $db->prepare('INSERT INTO orders (item_id, student_name) VALUES (?, ?)');
            $stmt->bind_param('is', $itemId, $student);
            $stmt->execute();
            $stmt->close();
            $notice = 'Order placed. The kitchen (database) has the ticket.';
        }
    }

    $menu = $db->query('SELECT id, name, category, price, description FROM menu_items ORDER BY category, name')->fetch_all(MYSQLI_ASSOC);
    $orders = $db->query(
        'SELECT o.id, o.student_name, o.created_at, m.name AS item_name
         FROM orders o
         JOIN menu_items m ON m.id = o.item_id
         ORDER BY o.id DESC
         LIMIT 8'
    )->fetch_all(MYSQLI_ASSOC);
    $db->close();
} catch (Throwable $e) {
    $connected = false;
    $error = 'Web tier is up, but it cannot reach the database. Check DB_HOST, credentials, and that MySQL is running.';
}

function h(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Campus Cafe — 2-tier demo</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="hero">
    <div class="badge-row">
      <span class="badge web">Web tier · Apache + PHP</span>
      <span class="badge <?= $connected ? 'db-ok' : 'db-bad' ?>">
        DB tier · <?= $connected ? 'connected to ' . h($cfg['host']) : 'unreachable' ?>
      </span>
    </div>
    <h1>Campus Cafe</h1>
    <p>A simple two-tier app: this page is served by the web server; the menu and orders live in MySQL.</p>
  </header>

  <?php if ($error): ?>
    <div class="banner error"><?= h($error) ?></div>
  <?php endif; ?>
  <?php if ($notice): ?>
    <div class="banner ok"><?= h($notice) ?></div>
  <?php endif; ?>

  <main>
    <section>
      <h2>Today's menu</h2>
      <?php if (!$menu): ?>
        <p class="muted">No items loaded. If the database is empty, run <code>db/init.sql</code>.</p>
      <?php else: ?>
        <div class="grid">
          <?php foreach ($menu as $item): ?>
            <article class="card">
              <span class="tag"><?= h($item['category']) ?></span>
              <h3><?= h($item['name']) ?></h3>
              <p><?= h($item['description']) ?></p>
              <strong>₹<?= h(number_format((float) $item['price'], 2)) ?></strong>
            </article>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </section>

    <section class="split">
      <div>
        <h2>Place an order</h2>
        <p class="muted">This INSERT goes to the database server — same host or a second VM.</p>
        <form method="post">
          <label>
            Your name
            <input type="text" name="student_name" maxlength="100" required placeholder="e.g. Asha">
          </label>
          <label>
            Item
            <select name="item_id" required>
              <option value="">Choose…</option>
              <?php foreach ($menu as $item): ?>
                <option value="<?= (int) $item['id'] ?>"><?= h($item['name']) ?></option>
              <?php endforeach; ?>
            </select>
          </label>
          <button type="submit" <?= $connected ? '' : 'disabled' ?>>Send to database</button>
        </form>
      </div>
      <div>
        <h2>Recent tickets</h2>
        <?php if (!$orders): ?>
          <p class="muted">No orders yet. Place one to see a write to MySQL.</p>
        <?php else: ?>
          <ul class="tickets">
            <?php foreach ($orders as $order): ?>
              <li>
                <strong><?= h($order['student_name']) ?></strong>
                ordered <?= h($order['item_name']) ?>
                <time><?= h($order['created_at']) ?></time>
              </li>
            <?php endforeach; ?>
          </ul>
        <?php endif; ?>
      </div>
    </section>
  </main>

  <footer>
    <p>Health check: <a href="/health.php">/health.php</a> · Config via <code>DB_HOST</code>, <code>DB_USER</code>, <code>DB_PASSWORD</code>, <code>DB_NAME</code></p>
  </footer>
</body>
</html>
