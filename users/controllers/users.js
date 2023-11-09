import * as db from '../db/users.js';

export const getUsers = async (req, res) => {
    const users = await db.getAllUsers();
    res.status(200).json({ users });
}

export const getUser = async (req, res) => {
    const user = await db.getUser(req.params.id);
    res.status(200).json({ user });
}

export const createUser = async (req, res) => {
    const user = await db.createUser(req.body);
    res.status(201).json({ user });
}

export const updateUser = async (req, res) => {
    const user = await db.updateUser(req.params.id, req.body);
    res.status(200).json({ user });
}

export const deleteUser = async (req, res) => {
    await db.deleteUser(req.params.id);
    res.status(200).json({ success: true });
}
