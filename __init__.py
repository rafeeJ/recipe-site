from flask import Flask, render_template
#from flask_bootstrap import Bootstrap

def create_app(config_file=None):
    app = Flask(__name__)
    #Bootstrap(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/')
    def home():
        return render_template('home.html')

    return app