import { connectedKnex } from './knex.js';

const tableName = 'users';

export const createUser = (user) => {
    return connectedKnex(tableName).insert(user);
}

export const getAllUsers = () => {
    return connectedKnex(tableName).select('*');
}

export const getUser = (id) => {
    return connectedKnex(tableName).where('id', id).first();
}

export const deleteUser = (id) => {
    return connectedKnex(tableName).where('id', id).del();
}

export const updateUser = (id, user) => {
    return connectedKnex(tableName).where('id', id).update(user);
}
