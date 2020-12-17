from flask import Flask, jsonify, request , make_response

import dataset

'''
crud operation Sqlite

sql delete -> table.delete(id = '')
sql update -> table.update( {} , id = '')
sql create -> table.insert({})
sql read -> table.find_one(id = '')
'''

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

table = db['books']


def fetch_db(book_id):
	return table.find_one( id=book_id)

def fetch_db_all():
	books = []
	for book in table:
		books.append(book)
	return books

@app.route('/db_populate' ,methods=['GET'])
def db_populate():
	table.insert({
		"book_id": "1",
		"name": "Joker",
		"author": " George Martin "
		})
	table.insert({
		"book_id": "2",
		"name": "Batman",
		"author": " kevin hemsworth "
		})
	table.insert({
		"book_id": "3",
		"name": "lion King",
		"author": " Krish James "
		})
	return make_response(jsonify(fetch_db_all()),
	                     200)

#All
@app.route('/books', methods=('GET', 'POST'))
def sql_name():
	if request.method == "GET":
	    return make_response( jsonify(fetch_db_all()) , 200)

	elif request.method == "POST":
		content = request.json
		book_id = content['book_id']

		table.insert(content) #Add Table
		# Books[book_id] = content #Its a dictionary(object) not list(array) so can't Append
		# book_obj = Books.get(book_id, {})#if bookId exist then give the respective object or {}
		return make_response(jsonify(fetch_db(book_id)), 200)

#Bu book Id
@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def sql_something(book_id):
	if request.method == "GET":
		book_obj = fetch_db(book_id)
		if book_obj:
			return make_response(jsonify(book_obj), 200)
		else: 
			return make_response(jsonify(book_obj), 400)

	elif request.method == "PUT":
		content = request.json
		table.update(content, ['book_id'])
		# Books[book_id] = content
		book_obj = fetch_db(book_id)
		return make_response(jsonify(book_obj), 200)

	elif request.method == "DELETE":
		table.delete(book_id = book_id)
		# if book_id in Books:
		# 	del Books[book_id]
		return make_response(jsonify({}), 204)



'''
# Json Array (Objects in Javascript)
Books = {
	'1': {
		"id": "1",
		"name": "Joker",
		"author": " George Martin "
	},
	'2': {
		"id": "2",
		"name": "Batman",
		"author": " kevin hemsworth "
	},
	'3': {
		"id": "3",
		"name": "lion King",
		"author": " Krish James "
	}
}

#All
@app.route('/books', methods=('GET', 'POST'))
def name():
	if request.method == "GET":
	    #return jsonify(Books)
	    return make_response(jsonify(Books), 200)
	elif request.method == "POST":
		content = request.json
		book_id = content['id']
		Books[book_id] = content #Its a dictionary(object) not list(array) so can't Append
		book_obj = Books.get(book_id, {})#if bookId exist then give the respective object or {}
		return make_response(jsonify(book_obj), 200)

#Bu book Id
@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def something(book_id):
	if request.method == "GET":
		book_obj = Books.get(book_id, {})
		if book_obj:
			return make_response(jsonify(book_obj), 200)
		else: 
			return make_response(jsonify(book_obj), 400)

	elif request.method == "PUT":
		content = request.json
		Books[book_id] = content
		book_obj = Books.get(book_id, {})
		return make_response(jsonify(book_obj), 200)

	elif request.method == "DELETE":
		if book_id in Books:
			del Books[book_id]
		return make_response(jsonify({}), 204)
'''
if __name__ == '__main__':

    app.run(debug=True)
