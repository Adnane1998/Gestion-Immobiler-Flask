from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy.orm import session, load_only

app = Flask(__name__)
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/immobilier'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Good(db.Model):
    __tablename__ = 'goods'
    good_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    type = db.Column(db.String(100))
    city = db.Column(db.String(100))
    characteristics = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, name, description, type, city, characteristics, user_id):
        self.name = name
        self.description = description
        self.type = type
        self.city = city

        self.characteristics = characteristics
        self.user_id = user_id


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    birth_date = db.Column(db.String(100))

    type = db.Column(db.String(100))

    city = db.Column(db.String(100))

    def __init__(self, first_name, last_name, birth_date,type, city):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.type = type

        self.city = city


# This is the index route where we are going to
# query on all our Users data
@app.route('/')
def Index():


    return "Welcome to the real estate management application"


@app.route('/<id>')
def User_HomePage(id):
    user_selected = User.query.get(id)
    all_users = User.query.all()
    all_goods = Good.query.all()
    owner_goods= Good.query.filter(Good.user_id == id)
    goods = Good.query.filter(Good.city == User.query.get(id).city)
    if User.query.get(id).type == "admin" : return render_template("admin.html", employees=all_users, Goods= all_goods)
    elif User.query.get(id).type == "owner" : return render_template("owner.html", employees=user_selected, Goods=goods,owner_goods= owner_goods)
    else: return render_template("user.html", employees= user_selected, Goods=goods)


@app.route('/insert_user', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        types= request.form['type']

        city = request.form['city']

        my_data = User(first_name, last_name, birth_date, types, city)
        db.session.add(my_data)
        db.session.commit()

        flash("User Inserted Successfully")

        return request.form


@app.route('/insert_good', methods=['POST'])
def insert_good():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        type = request.form['type']

        city = request.form['city']
        characteristics = request.form['characteristics']
        user_id = request.form['user_id']
        all_data = User.query.get(user_id)
        my_data = Good(name, description, type, city, characteristics, user_id)
        db.session.add(my_data)
        db.session.commit()

        flash("Good Inserted Successfully")
        return "Good Inserted Successfully"


@app.route('/update_good/<id>', methods=['POST'])
def update_good(id):
    if request.method == 'POST':
        my_data = Good.query.get(id)
        print(my_data)
        my_data.name = request.form['name']
        print(my_data.name)
        my_data.description = request.form['description']
        print(my_data.description)
        my_data.type = request.form['type']
        print(my_data.type)
        my_data.city = request.form['city']
        print(my_data.city)
        my_data.characteristics = request.form['characteristics']
        my_data.user_id = request.form['user_id']
        print(my_data.characteristics)


        db.session.add(my_data)
        db.session.commit()

        flash("Good Updated Successfully")

        return redirect(url_for('User_HomePage', id="7"))



# this is our update route where we are going to update our employee
@app.route('/update_user/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        my_data = User.query.get(id)
        my_data.first_name = request.form['first_name']
        my_data.last_name = request.form['last_name']

        my_data.birth_date = request.form['birth_date']
        my_data.city = request.form['city']
        my_data.type = request.form['type']

        db.session.add(my_data)
        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('User_HomePage', id=id))


# This is the index route where we are going to
# query on all our Goods data

@app.route('/<id>')
def Good_HomePage(id):
    all_data = User.query.get(id)
    return render_template("user.html", employees=all_data)


if __name__ == "__main__":
   app.run(host='0.0.0.0')
