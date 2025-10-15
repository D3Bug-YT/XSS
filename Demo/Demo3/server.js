const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;

app.get('/theme.html', (req, res) => {
  const filePath = path.join(__dirname, 'public', 'theme.html');
  const html = fs.readFileSync(filePath, 'utf8');

  console.log("---- Server response for /theme.html ----");
  console.log(html);
  console.log("------------------------------------------");

  res.send(html);
});

app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
  console.log(`DOM XSS demo running at http://localhost:${port}`);
});