from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities

import json
import time
import smtplib

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
        username="angelinux",
        password="123456",
        name="Angel",
        fullname="Motta",
        phone="948712638",
        address="Santiago de Surco, Lima"
    )
    db_session.add(user)
    db_session.commit()
    return "Test client created!"


@app.route('/clients', methods=['POST'])
def create_client():
    time.sleep(2)
    db_session = db.getSession(engine)
    message = json.loads(request.data)
    user = entities.Client(
        username=message['username'],
        password=message['password'],
        name=message['name'],
        fullname=message['fullname'],
        phone=message['phone'],
        address=message['address']
    )
    db_session.add(user)
    db_session.commit()
    message = {'message': 'Registered'}
    #return Response(message, status=200, mimetype='application/json')
    return Response(json.dumps(message, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')


@app.route('/authenticate', methods=["POST"])
def authenticate():
    time.sleep(2)
    message = json.loads(request.data)
    username = message['username']
    password = message['password']

    db_session = db.getSession(engine)
    try:

        if username == "piero16301" or "angelinux" or "THEFLILUX":
            user = db_session.query(entities.Client
                   ).filter(entities.Client.username == username
                   ).filter(entities.Client.password == password
                   ).one()
            message = {'message': 'Admin_auth'}
            return Response(message, status=303, mimetype='application/json')
    except Exception:

        try:
            user = db_session.query(entities.Client
                   ).filter(entities.Client.username == username
                   ).filter(entities.Client.password == password
                   ).one()
            message = {'message': 'Authorized'}
            return Response(json.dumps(message, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')
            #return Response(message, status=404, mimetype='application/json')

        except Exception:

            try:
                user = db_session.query(entities.Restaurante
                          ).filter(entities.Restaurante.username == username
                          ).filter(entities.Restaurante.password == password
                          ).one()
                message = {'message': 'Rest_auth'}
                return Response(message, status=200, mimetype='application/json')

            except Exception:
                message = {'message': 'Unauthorized'}
                return Response(json.dumps(message, cls=connector.AlchemyEncoder), status=401, mimetype='application/json')
                #return Response(message, status=400, mimetype='application/json')


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

## Methods Restaurants ##
@app.route('/restaurantes', methods=['POST'])
def create_restarante():
    db_session = db.getSession(engine)
    message = json.loads(request.data)
    #print(message)
    restaurante = entities.Restaurante(
        name_fullname=message['nombre'],
        username=message['correo'],
        phone=message['telefono'],
        password=message['pass'],
        name_restaurant=message['restaurante'],
        num_mesas=message['num_mesas'],
        address=message['address'],
        slogan=message['slogan']
    )
    db_session.add(restaurante)
    db_session.commit()
    response = {'message': 'Restaurante registered'}
    return Response(json.dumps(response, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')

@app.route('/restaurantes', methods = ['GET'])
def get_restaurantes():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Restaurante)
    data = []
    for restaurante in dbResponse:
        data.append(restaurante)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


res_id = 0

@app.route('/restaurantes/<int:rest>')
def show_restaurant(rest):
    global res_id
    res_id = rest
    return render_template('restaurant.html')


@app.route('/restaurant', methods=['GET'])
def get_restaurant():
    db_session = db.getSession(engine)
    restaurant = db_session.query(entities.Restaurante).filter(entities.Restaurante.id == res_id).one()
    return Response(json.dumps(restaurant, cls=connector.AlchemyEncoder), mimetype='application/json')

## End Methods Resturants ##

## Menu methods ##
@app.route('/add_menu/', methods=['GET'])
def add_menu():
    db_session = db.getSession(engine)
    plate = entities.Menu(
        restaurant_id=1,
        tipo_plato="segundo",
        name="Arroz con mariscos"
    )
    db_session.add(plate)
    db_session.commit()
    return "Plato de menu creado"


@app.route('/add_menu/', methods=['POST'])
def register_menu():
    db_session = db.getSession(engine)
    message = json.loads(request.data)
    print(message)
    for key in message:
        if 'entrada' in key:
            tipo = 'entrada'
        elif 'segundo' in key:
            tipo = 'segundo'
        else:
            print("Tipo de comida desconocida")
            tipo = 'otro'
        plate = entities.Menu(
            restaurant_id=8,
            tipo_plato=tipo,
            name=message.get(key)
        )
        db_session.add(plate)
    db_session.commit()
    response = {'message': 'Menu registered'}
    return Response(json.dumps(response, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')


@app.route('/menu', methods=['GET'])
def get_menu():
    db_session = db.getSession(engine)
    menu = db_session.query(entities.Menu).filter(entities.Menu.restaurant_id == res_id)
    data = []
    for item in menu:
        data.append(item)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/getmenu/<int:id_r>')
def get_menu_restaurante(id_r):
    db_session = db.getSession(engine)
    menu = db_session.query(entities.Menu).filter(entities.Menu.restaurant_id == id_r)
    data = []
    for item in menu:
        data.append(item)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')
## End Menu methods ##

@app.route('/soporte', methods=['POST'])
def send_email():
    db_session = db.getSession(engine)
    respuesta = json.loads(request.data)

    reclamos=entities.Reclamo(
        subject=respuesta["subject"],
        msg=respuesta["message"]
    )

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("netchmap@gmail.com", "susti con fe")
    messagegmail = 'Subject: {}\n\n{}'.format(respuesta["subject"], respuesta["message"])
    server.sendmail("netchmap@gmail.com", "netchmap@gmail.com", messagegmail)
    server.quit()
    db_session.add(reclamos)
    db_session.commit()
    response = {'message': 'Reclamo registrado'}
    return Response(json.dumps(response, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
