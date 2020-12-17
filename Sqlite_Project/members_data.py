
from flask import Flask, jsonify, request, make_response

import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///member.db')

table = db['members_data']


def fetch_db(members_id):
    return table.find_one(id=members_id)


def fetch_db_all():
    members = []
    for member in table:
        members.append(member)
    return members


def count_db():
    members = []
    for member in table:
        members.append(member)
    count = len(members)
    return count


@app.route('/db_populate', methods=['GET'])
def db_populate():
    table.insert({'members_id': '1', 'name': 'Joker',
                 'password': ' 3511 '})
    return make_response(jsonify(fetch_db_all()), 200)

@app.route('/db_clear', methods=['DELETE'])
def db_clear():
    total = count_db() + 1
    for x in range(1 , total):
        table.delete(members_id=x)
    return make_response(jsonify({}), 204)

@app.route('/members', methods=('GET', 'POST'))
def sql_name():
    if request.method == 'GET':
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':

        content = request.json
        count = count_db() + 1
        content['members_id'] = str(count)
        table.insert(content)  # Add Table
        return make_response(jsonify(fetch_db(count)), 200)


@app.route('/members/<members_id>', methods=['GET', 'PUT', 'DELETE'])
def sql_something(members_id):
    if request.method == 'GET':
        member_obj = fetch_db(members_id)
        if member_obj:
            return make_response(jsonify(member_obj), 200)
        else:
            return make_response(jsonify(member_obj), 400)
    elif request.method == 'PUT':

        content = request.json
        content['members_id'] = str(members_id)
        table.update(content, ['members_id'])
        member_obj = fetch_db(members_id)
        return make_response(jsonify(member_obj), 200)
    elif request.method == 'DELETE':

        table.delete(members_id=members_id)
        return make_response(jsonify({}), 204)


if __name__ == '__main__':

    app.run(debug=True)