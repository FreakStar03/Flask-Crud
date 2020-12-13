
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
data = [{'data': "hello world"}, {'data': 'rajesh'}]

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return jsonify(data)
    elif(request.method == 'POST'):
    	new_item = {'data': request.json['data']}
    	data.append(new_item)
    	return jsonify({'data': data})

@app.route('/put/<string:name>', methods=['PUT'])
def putMethod(name):
	get_item = [d for d in data if d['data'] == name]
	get_item[0]['data'] = request.json['data']
	return jsonify({'data' : data})


@app.route('/delete/<string:name>', methods=['DELETE'])
def deleteMethod(name):
	get_item = [d for d in data if d['data'] == name]
	data.remove(get_item[0])
	return jsonify({'data' : data})

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
	if 'id' in request.args:
	    id = int(request.args['id'])
	    return jsonify({'data': num*id}) 
	return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

    app.run(debug=True)
