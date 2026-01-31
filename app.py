from flask import Flask, render_template, request
from model import db, EmployeeModel





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emplyee.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()
    
    
    
@app.route("/add", methods = ['GET', 'POST'])
def add():
    
    if request.method == 'GET':
        return render_template("add")





app.run(host="localhost")