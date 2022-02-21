from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': u'Raju',
        'contact': u'9384743998',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'contact': u'4544578767',
        'done': False
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)

    contact = {
            'id': contacts[-1]['id'] + 1,
            'Name': request.json['Name'],
            'contact': request.json.get('contact', ""),
            'done': False
    }

    contacts.append(contact)
    return jsonify({
        "status": 'success',
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })


if(__name__ == "__main__"):
    app.run(debug=True)
