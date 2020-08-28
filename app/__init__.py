from flask import Flask, render_template, url_for

def create_app(config_file=None):
    app = Flask(__name__)

    @app.route('/recipes')
    def recipes():
        return render_template('recipes.html')
    
    @app.route('/')
    def home():
        return render_template('home.html')

    return app