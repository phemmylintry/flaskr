from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
Bootstrap(app)

#configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # cur = mysql.connection.cursor()
    # if cur.execute("INSERT user(username) VALUES('Ben')"):
    #     mysql.connection.commit()
    #     return 'success', 201
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO details(name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
    # ls = ['mango', 'Apple', 'orange']
    return render_template('index.html')
    #return url_for('about')

@app.route('/about')
def about():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM details")
    if result > 0:
        details = cur.fetchall()
        return render_template('about.html', details=details)

# @app.route('/css')
# def css():
#     return render_template('css.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'Page Not Found'

if __name__ == '__main__':
    app.run(debug=True)