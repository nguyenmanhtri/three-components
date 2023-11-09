const express = require('express');
const app = express();

const port = process.env.USERS_PORT || 3000;

app.get('/', (req, res) => {
   console.log('===== Received request =====');
   const message = {
      'message': 'hello world',
   }
   res.send(message);
});

app.listen(port, () => {
   console.log(`Server is running on port ${port}`);
});
