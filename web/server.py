from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/registro_cliente')
def registro_cliente():
    return render_template('registro_cliente.html')

@app.route('/mapa/')
def mapa():
    return render_template('mapa.html')

@app.route('/01.html')
def restaurant():
    return render_template('01.html')

@app.route('/register_business.html')
def register_restaurant():
    return render_template('register_business.html')

if __name__ == '__main__':
    app.run()