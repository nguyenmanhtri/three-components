const express = require('express');
const app = express();

const port = process.env.USERS_PORT;

app.get('/', (req, res) => {
   res.send('Hello World!');
});

app.listen(port, () => {
   console.log(`Server is running on port ${port}`);
});
