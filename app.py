from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/recipe_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    ingredients = data.get('ingredients').split(',')
    matching_recipes = Recipe.query.filter(Recipe.ingredients.contains(','.join(ingredients))).all()
    return render_template('search_results.html', recipes=matching_recipes)


if __name__ == '__main__':
    app.run(debug=True)
