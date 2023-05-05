from dbconnection import Database

# A simple script to check if the database is working correctly

with Database() as db:
    result = db("SELECT * FROM users")
    result = result.fetchall()
    for i in result:
        print(i)
