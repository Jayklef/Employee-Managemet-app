from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "employees"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    geneder = db.Column(db.String())
    hobbies = db.Column(db.String())
    country = db.Column(db.String())
    
    
    def __init__(self, first_name, last_name, email, geneder, password, hobbies, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.geneder = geneder
        self.password = password
        self.hobbies = hobbies
        self.country = country


