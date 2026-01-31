from flask import Flask, render_template, request, redirect
from model import db, EmployeeModel





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emplyee.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


#@app.before_first_request
#ef create_table():
#    db.create_all()
    
with app.app_context():
    db.create_all()
    
    
    
@app.route("/add", methods = ['GET', 'POST'])
def add():
    
    if request.method == 'GET':
        return render_template("add.html")


    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies =",".join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']
        
        
        employee = EmployeeModel(
            first_name= first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,
            country=country
        )
        
        db.session.add(employee)
        db.session.commit()
        
        return redirect("/index")
    
    
@app.route("/", methods = ['GET'])
def index():
    employees = EmployeeModel.query.all()
    return render_template("index.html", employees = employees)


app.run(host="localhost")