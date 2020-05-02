from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    ls = ['mango', 'Apple', 'orange']
    return render_template('index.html', ls=ls)
    #return url_for('about')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/css')
# def css():
#     return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)