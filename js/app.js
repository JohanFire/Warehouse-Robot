const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Ruta principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Otra ruta
app.get('/otra-ruta', (req, res) => {
    res.send('Esta es otra ruta');
});

app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});