from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/clients', methods=['GET'])
def get_clients():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Client)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    db_session = db.getSession(engine)
    users = db_session.query(entities.Client).filter(entities.Client.id == id)
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return Response(js, status=200, mimetype='application/json')

    message = { 'status': 404, 'message': 'Not Found' }
    return Response(message, status=404, mimetype='application/json')

@app.route('/create_test_clients', methods=['GET'])
def create_test_clients():
    db_session = db.getSession(engine)
    user = entities.Client(
        email="sanjuan.pama@gmail.com",
        password="123456",
        name="Piero",
        fullname="Morales",
        phone="947861220",
        address="Santiago de Surco, Lima")
    db_session.add(user)
    db_session.commit()
    return "Test client created!"

@app.route('/clients', methods=['POST'])
def create_client():
    client = json.loads(request.form['values'])
    user = entities.Client(
        email=client['email'],
        password=client['password'],
        name=client['name'],
        fullname=client['fullname'],
        phone=client['phone'],
        address=client['address']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Client created!'

@app.route('/authenticate', methods=['POST'])
def authenticate():
    time.sleep(1)
    message = json.loads(request.data)
    email = message['email']
    password = message['password']
    db_session = db.getSession(engine)
    try:
        user = db_session.query(entities.Client
            ).filter(entities.Client.email == email
            ).filter(entities.Client.password == password
            ).one()
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')

@app.route('/clients', methods=['PUT'])
def update_client():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.Client).filter(entities.Client.id == id).first()
    c = json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return 'Client updated!'

@app.route('/clients', methods=['DELETE'])
def delete_client():
    id = request.form['key']
    session = db.getSession(engine)
    users = session.query(entities.Client).filter(entities.Client.id == id)
    for user in users:
        session.delete(user)
    session.commit()
    return 'Client deleted!'

if __name__ == '__main__':
    app.run()