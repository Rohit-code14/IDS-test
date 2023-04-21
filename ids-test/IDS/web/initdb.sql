create table if not exists users;
    create table users (
    id integer primary key autoincrement,
    email text not null,
    password text not null,
    companyname text not null,
    name text not null,
    apikey text not null
);