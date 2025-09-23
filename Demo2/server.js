const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const postsFile = path.join(__dirname, 'posts.json');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

function loadPosts() {
  if (!fs.existsSync(postsFile)) {
    fs.writeFileSync(postsFile, '[]');
  }
  return JSON.parse(fs.readFileSync(postsFile, 'utf8'));
}

function savePosts(posts) {
  fs.writeFileSync(postsFile, JSON.stringify(posts, null, 2));
}

app.get('/feed', (req, res) => {
  const posts = loadPosts();

  const renderedPosts = posts.map(p => `
    <div class="card">
      <p>${p.content}</p>
    </div>
  `).join('');

  res.send(`
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Stored XSS Demo - Feed</title>
      <style>
        body { font-family: Arial, sans-serif; padding: 2rem; background: #f4f6fb; color: #222; }
        .card { background: #fff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.1); max-width: 600px; margin: auto; margin-bottom: 1rem; }
      </style>
    </head>
    <body>
      <h1>Posts Feed</h1>
      ${renderedPosts}
      <p><a href="/">Go back</a></p>
    </body>
    </html>
  `);
});

app.post('/new', (req, res) => {
  const posts = loadPosts();
  const content = req.body.content || '';

  posts.push({ content });
  savePosts(posts);

  res.redirect('/feed');
});

app.listen(port, () => {
  console.log(`Stored XSS demo running at http://localhost:${port}`);
});