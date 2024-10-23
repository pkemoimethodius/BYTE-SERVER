from db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15))

    projects = db.relationship('Project', backref='user')

    def __repr__(self):
        return f"User('{self.first_name} {self.last_name}', '{self.email}')"

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=True)

    projects = db.relationship('Project', backref='client')

    def __repr__(self):
        return f"Client('{self.company_name}', '{self.contact_name}')"

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    hire_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    project = db.relationship('Project', backref='employees')

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', '{self.role}')"

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Added user_id for the user responsible for the project
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    budget = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    materials = db.relationship('Material', backref='project')
    equipments = db.relationship('Equipment', backref='project')

    def __repr__(self):
        return f"Project('{self.name}', '{self.client_id}')"

class Material(db.Model):
    __tablename__ = 'materials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    unit = db.Column(db.String(50), nullable=True)
    unit_price = db.Column(db.Float, nullable=True)
    quantity = db.Column(db.Float, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __repr__(self):
        return f"Material('{self.name}', '{self.unit_price}', '{self.quantity}')"

class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    rental_price = db.Column(db.Float, nullable=True)
    purchase_date = db.Column(db.Date, nullable=False)
    maintenance_date = db.Column(db.Date, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Equipment('{self.name}', '{self.cost}', '{self.status}')"
