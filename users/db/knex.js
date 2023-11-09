import knex from "knex";

export const connectedKnex = knex({
    client: 'sqlite3',
    connection: {
        filename: '/usr/src/app/data/users.sqlite3',
    },
    useNullAsDefault: true,
});
