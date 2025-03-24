
from flask import Flask
from routes import login_route

app = Flask(__name__)
app.secret_key = 'c7IVzYZekc'


login_route(app)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)

