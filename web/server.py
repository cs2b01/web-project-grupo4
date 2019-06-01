from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/mapa/')
def mapa():
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run()
