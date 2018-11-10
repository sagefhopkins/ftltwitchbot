import sqlite3

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = sqlite3.connect('locations.db')

    return connection

#Inserts new rows into a table, this is created to ensure uniformity between rows
def database_Update(name, x, y):
    try:
        sql = database_Connect()
        query = "UPDATE `location` SET x = ?, y = ? WHERE name=?"
        sql.execute(query, (int(x), int(y), str(name)))
        sql.commit()
    except():
        pass
        print "Error occurred databasing!"
def database_Insert(name, x, y):
    sql = database_Connect()
    query = "INSERT INTO `location` VALUES(?, ?, ?)"
    print query
    sql.execute(query, (name, x, y))
    sql.commit()

#Queries the table, and returns all values which either match or include the
#name string in their overall value
def database_Read(name):
    sql = database_Connect()
    query = "SELECT * FROM location WHERE name=?"
    cur = sql.cursor()
    cur.execute(query, (name, ))
    return cur.fetchall()

#Creates new tables into the database, this will always use the same format
#to ensure uniformity between tables
def database_Table(name):
    sql = database_Connect()
    query = "CREATE TABLE `{0}` (`name` text, `x` int, `y` int)".format(name)
    sql.execute(query)
    sql.commit()
    print name + " New table created!"
