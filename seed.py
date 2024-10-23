import os
import logging
from app import create_app, db
from models import User, Client, Employee, Project, Material, Equipment
from datetime import datetime, date

app = create_app()

# Configure logging
logging.basicConfig(level=logging.INFO)

# def create_users():
#     """Add predefined user data (12 users)."""
#     users = [
#         User(name='John Doe', email='john.doe@email.com', password='password123', role='Project Manager', phone_number='+254701234567'),
#         User(name='Jane Smith', email='jane.smith@email.com', password='password456', role='Site Engineer', phone_number='+254712345678'),
#         User(name='Mike Johnson', email='mike.johnson@email.com', password='password789', role='Foreman', phone_number='+254723456789'),
#         User(name='Emily Davis', email='emily.davis@email.com', password='password101', role='Architect', phone_number='+254734567890'),
#         User(name='Chris Brown', email='chris.brown@email.com', password='password202', role='Civil Engineer', phone_number='+254745678901'),
#         User(name='Alice White', email='alice.white@email.com', password='password303', role='Construction Worker', phone_number='+254756789012'),
#         User(name='Bob Green', email='bob.green@email.com', password='password404', role='Surveyor', phone_number='+254767890123'),
#         User(name='Charlie Blue', email='charlie.blue@email.com', password='password505', role='Mechanical Engineer', phone_number='+254778901234'),
#         User(name='Diana Red', email='diana.red@email.com', password='password606', role='Electrical Engineer', phone_number='+254789012345'),
#         User(name='Edward Black', email='edward.black@email.com', password='password707', role='Plumber', phone_number='+254790123456'),
#         User(name='Fiona Silver', email='fiona.silver@email.com', password='password808', role='Carpenter', phone_number='+254801234567'),
#         User(name='George Gold', email='george.gold@email.com', password='password909', role='Safety Officer', phone_number='+254812345678')
#     ]
#     return users

def create_users():
    """Add predefined user data (12 users)."""
    users = [
        User(first_name='John', last_name='Doe', email='john.doe@email.com', password='password123', role='Project Manager', phone_number='+254701234567'),
        User(first_name='Jane', last_name='Smith', email='jane.smith@email.com', password='password456', role='Site Engineer', phone_number='+254712345678'),
        User(first_name='Mike', last_name='Johnson', email='mike.johnson@email.com', password='password789', role='Foreman', phone_number='+254723456789'),
        User(first_name='Emily', last_name='Davis', email='emily.davis@email.com', password='password101', role='Architect', phone_number='+254734567890'),
        User(first_name='Chris', last_name='Brown', email='chris.brown@email.com', password='password202', role='Civil Engineer', phone_number='+254745678901'),
        User(first_name='Alice', last_name='White', email='alice.white@email.com', password='password303', role='Construction Worker', phone_number='+254756789012'),
        User(first_name='Bob', last_name='Green', email='bob.green@email.com', password='password404', role='Surveyor', phone_number='+254767890123'),
        User(first_name='Charlie', last_name='Blue', email='charlie.blue@email.com', password='password505', role='Mechanical Engineer', phone_number='+254778901234'),
        User(first_name='Diana', last_name='Red', email='diana.red@email.com', password='password606', role='Electrical Engineer', phone_number='+254789012345'),
        User(first_name='Edward', last_name='Black', email='edward.black@email.com', password='password707', role='Plumber', phone_number='+254790123456'),
        User(first_name='Fiona', last_name='Silver', email='fiona.silver@email.com', password='password808', role='Carpenter', phone_number='+254801234567'),
        User(first_name='George', last_name='Gold', email='george.gold@email.com', password='password909', role='Safety Officer', phone_number='+254812345678')
    ]
    return users


def create_clients():
    """Add predefined client data (12 clients)."""
    clients = [
        Client(company_name='Skyline Construction', contact_name='Alice Smith', email='alice.smith@email.com', phone_number='123-456-7890', address='123 Skyline Rd'),
        Client(company_name='Mountain Builders', contact_name='Bob Johnson', email='bob.johnson@email.com', phone_number='234-567-8901', address='456 Mountain St'),
        Client(company_name='Urban Developments', contact_name='Charlie Brown', email='charlie.brown@email.com', phone_number='345-678-9012', address='789 Urban Ave'),
        Client(company_name='GreenTech Construction', contact_name='Diana Prince', email='diana.prince@email.com', phone_number='456-789-0123', address='321 Green Blvd'),
        Client(company_name='Steel Structure Inc.', contact_name='Edward Elric', email='edward.elric@email.com', phone_number='567-890-1234', address='654 Steel Dr'),
        Client(company_name='Concrete Works', contact_name='George White', email='george.white@email.com', phone_number='678-901-2345', address='987 Concrete Pl'),
        Client(company_name='BuildRight', contact_name='Fiona Black', email='fiona.black@email.com', phone_number='789-012-3456', address='321 BuildRight St'),
        Client(company_name='BridgeMasters', contact_name='Hank Green', email='hank.green@email.com', phone_number='890-123-4567', address='654 BridgeWay'),
        Client(company_name='HeavyWorks', contact_name='Ivy Red', email='ivy.red@email.com', phone_number='901-234-5678', address='789 Heavy Ln'),
        Client(company_name='Foundation Experts', contact_name='Jack Blue', email='jack.blue@email.com', phone_number='012-345-6789', address='123 Foundation Way'),
        Client(company_name='Real Estate Builders', contact_name='Karen Gold', email='karen.gold@email.com', phone_number='123-456-7891', address='456 Real Estate Rd'),
        Client(company_name='Renovation Pro', contact_name='Leo Silver', email='leo.silver@email.com', phone_number='234-567-8902', address='789 Renovation Blvd')
    ]
    return clients

def create_projects(client_ids, user_ids):
    """Add predefined project data (12 construction projects)."""
    projects = [
    Project(name='Skyscraper Construction', client_id=client_ids[0], user_id=user_ids[4] ,start_date=date(2023, 1, 1), end_date=date(2025, 6, 1), budget=50000000, status='In Progress'),
    Project(name='Mountain Retreat Housing', client_id=client_ids[1],user_id=user_ids[1] , start_date=date(2023, 2, 1), end_date=date(2024, 12, 1), budget=30000000, status='In Progress'),
    Project(name='Urban Office Complex', client_id=client_ids[2], user_id=user_ids[8] ,start_date=date(2023, 3, 1), end_date=date(2024, 9, 1), budget=20000000, status='In Progress'),
    Project(name='Green Building Project', client_id=client_ids[3],user_id=user_ids[7] , start_date=date(2023, 4, 1), end_date=date(2025, 10, 3), budget=15000000, status='In Progress'),
    Project(name='Steel Warehouse', client_id=client_ids[4],user_id=user_ids[2] , start_date=date(2023, 5, 1), end_date=date(2023, 12, 1), budget=10000000, status='Completed'),
    Project(name='Concrete Bridge Construction', client_id=client_ids[5],user_id=user_ids[9] , start_date=date(2023, 6, 1), end_date=date(2026, 4, 1), budget=25000000, status='In Progress'),
    Project(name='Residential Housing Complex', client_id=client_ids[6], user_id=user_ids[4] ,start_date=date(2023, 7, 1), end_date=date(2025, 1, 1), budget=60000000, status='In Progress'),
    Project(name='Heavy Machinery Depot', client_id=client_ids[7],user_id=user_ids[6] , start_date=date(2023, 8, 1), end_date=date(2050, 11, 6), budget=40000000, status='Planned'),
    Project(name='Foundation Strengthening', client_id=client_ids[8],user_id=user_ids[8] , start_date=date(2023, 9, 1), end_date=date(2026, 4, 12), budget=5000000, status='In Progress'),
    Project(name='Luxury Apartment Towers', client_id=client_ids[9], user_id=user_ids[1] ,start_date=date(2023, 10, 1), end_date=date(2024, 8, 1), budget=80000000, status='In Progress'),
    Project(name='Real Estate Development', client_id=client_ids[10],user_id=user_ids[2] , start_date=date(2023, 11, 1), end_date=date(2030, 10, 3), budget=50000000, status='In Progress'),
    Project(name='Office Renovation', client_id=client_ids[11],user_id=user_ids[3] , start_date=date(2023, 12, 1), end_date=date(2022, 12, 8), budget=10000000, status='Planned')
]

    return projects

def create_employees(project_ids):
    """Add predefined employee data (12 construction employees)."""
    employees = [
        Employee(first_name='John', last_name='Doe', role='Project Manager', email='john.doe@email.com', phone_number='123-456-7890', hire_date=date(2020, 1, 15), salary=90000, project_id=project_ids[0]),
        Employee(first_name='Jane', last_name='Smith', role='Site Engineer', email='jane.smith@email.com', phone_number='234-567-8901', hire_date=date(2019, 3, 20), salary=85000, project_id=project_ids[1]),
        Employee(first_name='Mike', last_name='Johnson', role='Foreman', email='mike.johnson@email.com', phone_number='345-678-9012', hire_date=date(2018, 5, 25), salary=70000, project_id=project_ids[2]),
        Employee(first_name='Emily', last_name='Davis', role='Architect', email='emily.davis@email.com', phone_number='456-789-0123', hire_date=date(2021, 7, 30), salary=95000, project_id=project_ids[3]),
        Employee(first_name='Chris', last_name='Brown', role='Civil Engineer', email='chris.brown@email.com', phone_number='567-890-1234', hire_date=date(2022, 2, 5), salary=80000, project_id=project_ids[4]),
        Employee(first_name='Alice', last_name='White', role='Construction Worker', email='alice.white@email.com', phone_number='678-901-2345', hire_date=date(2023, 8, 10), salary=45000, project_id=project_ids[5]),
        Employee(first_name='Bob', last_name='Green', role='Surveyor', email='bob.green@email.com', phone_number='789-012-3456', hire_date=date(2020, 9, 15), salary=65000, project_id=project_ids[6]),
        Employee(first_name='Charlie', last_name='Blue', role='Mechanical Engineer', email='charlie.blue@email.com', phone_number='890-123-4567', hire_date=date(2019, 11, 20), salary=85000, project_id=project_ids[7]),
        Employee(first_name='Diana', last_name='Red', role='Electrical Engineer', email='diana.red@email.com', phone_number='901-234-5678', hire_date=date(2021, 12, 25), salary=78000, project_id=project_ids[8]),
        Employee(first_name='Edward', last_name='Black', role='Plumber', email='edward.black@email.com', phone_number='012-345-6789', hire_date=date(2018, 10, 30), salary=50000, project_id=project_ids[9]),
        Employee(first_name='Fiona', last_name='Silver', role='Carpenter', email='fiona.silver@email.com', phone_number='123-456-7891', hire_date=date(2017, 4, 15), salary=48000, project_id=project_ids[10]),
        Employee(first_name='George', last_name='Gold', role='Safety Officer', email='george.gold@email.com', phone_number='234-567-8902', hire_date=date(2016, 6, 20), salary=67000, project_id=project_ids[11])
    ]
    return employees

def create_materials(project_ids):
    """Add predefined materials data (12 materials)."""
    materials = [
        Material(name='Steel Beams', unit='tons', unit_price=500, quantity=100, project_id=project_ids[0]),
        Material(name='Concrete', unit='cubic meters', unit_price=100, quantity=500, project_id=project_ids[1]),
        Material(name='Bricks', unit='pieces', unit_price=1, quantity=10000, project_id=project_ids[2]),
        Material(name='Lumber', unit='cubic meters', unit_price=200, quantity=300, project_id=project_ids[3]),
        Material(name='Reinforcing Bars', unit='tons', unit_price=600, quantity=50, project_id=project_ids[4]),
        Material(name='Glass Panels', unit='square meters', unit_price=150, quantity=200, project_id=project_ids[5]),
        Material(name='Insulation Material', unit='cubic meters', unit_price=50, quantity=400, project_id=project_ids[6]),
        Material(name='Tiles', unit='pieces', unit_price=5, quantity=5000, project_id=project_ids[7]),
        Material(name='Cement Bags', unit='bags', unit_price=10, quantity=1000, project_id=project_ids[8]),
        Material(name='Roofing Sheets', unit='pieces', unit_price=30, quantity=600, project_id=project_ids[9]),
        Material(name='Paint', unit='liters', unit_price=25, quantity=400, project_id=project_ids[10]),
        Material(name='Pipes', unit='meters', unit_price=10, quantity=1000, project_id=project_ids[11])
    ]
    return materials

def create_equipments(project_ids):
    """Add predefined equipment data (12 construction equipments)."""
    equipments = [
       Equipment(name='Excavator', quantity=1, cost=50000.0, rental_price=5600.00, purchase_date=date(2022, 1, 15), maintenance_date=date(2023, 1, 15), project_id=project_ids[0], status='Available'),
        Equipment(name='Bulldozer', quantity=1, cost=70000.0, rental_price=2400.00, purchase_date=date(2021, 2, 20), maintenance_date=date(2022, 2, 20), project_id=project_ids[1], status='Available'),
        Equipment(name='Crane', quantity=1, cost=100000.0, rental_price=43000.00, purchase_date=date(2020, 3, 25), maintenance_date=date(2021, 3, 25), project_id=project_ids[2], status='Available'),
        Equipment(name='Concrete Mixer', quantity=1, cost=25000.0, rental_price=2200.00, purchase_date=date(2019, 4, 30), maintenance_date=date(2020, 4, 30), project_id=project_ids[3], status='Available'),
        Equipment(name='Forklift', quantity=1, cost=30000.0, rental_price=457000.00, purchase_date=date(2018, 5, 5), maintenance_date=date(2019, 5, 5), project_id=project_ids[4], status='Available'),
        Equipment(name='Scaffolding', quantity=1, cost=15000.0, rental_price=33000.000, purchase_date=date(2017, 6, 10), maintenance_date=date(2018, 6, 10), project_id=project_ids[5], status='Available'),
        Equipment(name='Drill', quantity=1, cost=5000.0, rental_price=78000.00, purchase_date=date(2016, 7, 15), maintenance_date=date(2017, 7, 15), project_id=project_ids[6], status='Available'),
        Equipment(name='Loader', quantity=1, cost=40000.0, rental_price=65000.000, purchase_date=date(2015, 8, 20), maintenance_date=date(2016, 8, 20), project_id=project_ids[7], status='Available'),
        Equipment(name='Welding Machine', quantity=1, cost=10000.0, rental_price=123000.000, purchase_date=date(2014, 9, 25), maintenance_date=date(2015, 9, 25), project_id=project_ids[8], status='Available'),
        Equipment(name='Compactor', quantity=1, cost=25000.0, rental_price=12300.000, purchase_date=date(2013, 10, 30), maintenance_date=date(2014, 10, 30), project_id=project_ids[9], status='Available'),
        Equipment(name='Generator', quantity=1, cost=15000.0, rental_price=5000.000, purchase_date=date(2012, 11, 5), maintenance_date=date(2013, 11, 5), project_id=project_ids[10], status='Available'),
        Equipment(name='Water Pump', quantity=1, cost=7000.0, rental_price=9000.000, purchase_date=date(2011, 12, 10), maintenance_date=date(2012, 12, 10), project_id=project_ids[11], status='Available')
    ]
    return equipments


# with app.app_context():

#         # Clear existing data
#     db.drop_all()  # Drops all tables
#     db.create_all()  # Recreate tables
#     logging.info("Database cleared and tables created.")

#     # Add users
#     users = create_users()
#     db.session.add_all(users)
#     db.session.commit()
#     logging.info("Users added.")

#     # Add clients
#     clients = create_clients()
#     db.session.add_all(clients)
#     db.session.commit()
#     logging.info("Clients added.")

#     # Get client IDs
#     client_ids = [client.id for client in clients]

#     # Add projects
#     projects = create_projects(client_ids)
#     db.session.add_all(projects)
#     db.session.commit()
#     logging.info("Projects added.")

#     # Get project IDs
#     project_ids = [project.id for project in projects]

#     # Add employees
#     employees = create_employees(project_ids)
#     db.session.add_all(employees)
#     db.session.commit()
#     logging.info("Employees added.")

#     # Add materials
#     materials = create_materials(project_ids)
#     db.session.add_all(materials)
#     db.session.commit()
#     logging.info("Materials added.")

#     # Add equipment
#     equipments = create_equipments(project_ids)
#     db.session.add_all(equipments)
#     db.session.commit()
#     logging.info("Equipment added.")

with app.app_context():
    # Clear existing data
    db.drop_all()  # Drops all tables
    db.create_all()  # Recreate tables
    logging.info("Database cleared and tables created.")

    # Add users
    users = create_users()
    db.session.add_all(users)
    db.session.commit()
    logging.info("Users added.")

    # Add clients
    clients = create_clients()
    db.session.add_all(clients)
    db.session.commit()
    logging.info("Clients added.")

    # Get client IDs
    client_ids = [client.id for client in clients]

    # Get user IDs
    user_ids = [user.id for user in users]

    # Add projects
    projects = create_projects(client_ids, user_ids)
    db.session.add_all(projects)
    db.session.commit()
    logging.info("Projects added.")

    # Get project IDs
    project_ids = [project.id for project in projects]

    # Add employees
    employees = create_employees(project_ids)
    db.session.add_all(employees)
    db.session.commit()
    logging.info("Employees added.")

    # Add materials
    materials = create_materials(project_ids)
    db.session.add_all(materials)
    db.session.commit()
    logging.info("Materials added.")

    # Add equipment
    equipments = create_equipments(project_ids)
    db.session.add_all(equipments)
    db.session.commit()
    logging.info("Equipment added.")
