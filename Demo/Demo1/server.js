const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/welcome', (req, res) => {
    const name = req.query.name || 'Guest';

    console.log("-------- Name received from client -------");
    console.log("Name:", name);
    console.log("------------------------------------------\n\n\n");

    const templatePath = path.join(__dirname, 'public', 'welcome.html');
    let html = fs.readFileSync(templatePath, 'utf8');

    html = html.replace('{{name}}', name);

    console.log("---- Server response for /welcome.html ----");
    console.log(html);
    console.log("------------------------------------------");

    res.send(html);
});

app.listen(port, () => {
    console.log(`XSS demo app listening at http://localhost:${port}`);
});