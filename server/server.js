const express = require('express');
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser');
const net = require('net');
// Allows for an app on another port to make requests to server
app.use(cors());

app.use(bodyParser.json());
// Handle POST request from weather app
app.post('/suggestions', (req, res)  => {
    console.log('Received from UI:', req.body);
    const weatherData = JSON.stringify(req.body)
    // This server will be the client for the microservice
    const client = new net.Socket();
    const serverAddress = 'localhost';
    const serverPort = 3000;

    client.connect(serverPort, serverAddress, () => {
        console.log('Connected to server:', serverAddress, serverPort);
        // Send data to microservice
        client.write(weatherData);
    });
    // Receive data from microservice
    client.on('data', (data) => {
        const receivedData = data.toString();
        console.log('Received from server:', receivedData);
        // Send received data to UI
        res.send(receivedData);
        // Close the connection with the microservice
        client.end();
    });
    // Handle connection close
    client.on('close', () => {
        console.log('Connection closed');
    });
});

app.listen(3000, () => {
    console.log('Server is listening on port 3000');
  });