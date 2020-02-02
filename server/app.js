const WebSocket = require('ws');
const express = require('express');
const http = require('http');
const
  app = express(),
  server = http.createServer(app),
  wss = new WebSocket.Server({ server });


app.use('/', express.static('../client/dist'));

server.listen(8080, () => {
  console.log('got listen');
});

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    console.log('received: %s', message);
    console.log(message);
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN)
        client.send(message);
    });
  });

  ws.send('something');
});
