import express from 'express';
import bodyParser from 'body-parser';
import userRoutes from './routes/users.js';

const app = express();
const port = process.env.USERS_PORT || 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/users', userRoutes);
app.get('/', (req, res) => res.send({ message: 'Welcome to the Users API!' }));
app.all('*', (req, res) => res.send({ message: 'You\'ve tried reaching a route that doesn\'t exist.' }));

app.listen(port, () => {
   console.log(`Server is running on port ${port}`);
});
