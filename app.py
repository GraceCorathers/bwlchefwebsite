from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes/')
def recipes():
    return render_template('recipes.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

# allows u to click run button
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5423, debug=True)
    
