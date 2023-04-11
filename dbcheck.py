from dbconnection import Database

with Database() as db:
	result = db("SELECT * FROM users")
	result = result.fetchall()
	for i in result:
		print(i)