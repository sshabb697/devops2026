const express = require('express');

function createApp() {
  const app = express();
  app.use(express.json());

  // In-memory task store (resets on restart) — fine for a demo.
  const tasks = [
    { id: 1, title: 'Learn Azure DevOps', done: false }
  ];
  let nextId = 2;

  app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the Contoso Tasks API' });
  });

  app.get('/health', (req, res) => {
    res.json({ status: 'ok' });
  });

  app.get('/tasks', (req, res) => {
    res.json(tasks);
  });

  app.post('/tasks', (req, res) => {
    const title = (req.body && req.body.title) || '';
    if (!title.trim()) {
      return res.status(400).json({ error: 'title is required' });
    }
    const task = { id: nextId++, title: title.trim(), done: false };
    tasks.push(task);
    res.status(201).json(task);
  });

  return app;
}

module.exports = { createApp };
