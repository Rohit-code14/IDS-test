import sqlite3 as sql

def dbInit():
	conn = sql.connect("database.db")
	c = conn.cursor()
	c.execute('''create table if not exists users (
                id integer primary key autoincrement,
                email text not null,
                password text not null,
                companyname text not null,
                name text not null,
                apikey text not null
                )''')
	conn.commit()
	
def insertUser(email,password,companyname,name,apikey):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,password,companyname,name,apikey) VALUES (?,?,?,?,?)", (email,password,companyname,name,apikey))
    con.commit()
    con.close()
    return cur

def retrieveUsers(email):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users where email=?",(email,))
	users = cur.fetchall()
	con.close()
	return users

def verifyUsers(email,password):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users where email=? and password=?",(email,password))
	users = cur.fetchone()
	con.close()
	return users