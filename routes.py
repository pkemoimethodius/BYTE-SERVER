from flask import request, jsonify
from db import db
from models import User, Project, Client, Employee, Material, Equipment

def register_routes(app):
    # Employee Routes (as already defined)

    # Client Routes (as already defined)

    # User Routes
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([{
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'phone_number': user.phone_number
        } for user in users]), 200

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        required_fields = ['name', 'email', 'password', 'role']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=data['password'],  # Ensure to hash this before storing in production
            role=data['role'],
            phone_number=data.get('phone_number')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role,
                'phone_number': user.phone_number
            }), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    @app.route('/users/<int:user_id>', methods=['PATCH'])
    def update_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.get_json()
        for field in ['name', 'email', 'role', 'phone_number']:
            if field in data:
                setattr(user, field, data[field])

        db.session.commit()
        return jsonify({'message': 'User updated successfully!'}), 200

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'}), 200

    # Project Routes
    @app.route('/projects', methods=['GET'])
    def get_projects():
        projects = Project.query.all()
        return jsonify([{
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'start_date': project.start_date.isoformat(),
            'end_date': project.end_date.isoformat()
        } for project in projects]), 200

    @app.route('/projects', methods=['POST'])
    def create_project():
        data = request.get_json()
        required_fields = ['name', 'description', 'start_date', 'end_date']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_project = Project(
            name=data['name'],
            description=data['description'],
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully!'}), 201

    @app.route('/projects/<int:project_id>', methods=['GET'])
    def get_project(project_id):
        project = Project.query.get(project_id)
        if project:
            return jsonify({
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'start_date': project.start_date.isoformat(),
                'end_date': project.end_date.isoformat()
            }), 200
        else:
            return jsonify({'error': 'Project not found'}), 404

    @app.route('/projects/<int:project_id>', methods=['PATCH'])
    def update_project(project_id):
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        data = request.get_json()
        for field in ['name', 'description', 'start_date', 'end_date']:
            if field in data:
                setattr(project, field, data[field])

        db.session.commit()
        return jsonify({'message': 'Project updated successfully!'}), 200

    @app.route('/projects/<int:project_id>', methods=['DELETE'])
    def delete_project(project_id):
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully!'}), 200

    # Material Routes
    @app.route('/materials', methods=['GET'])
    def get_materials():
        materials = Material.query.all()
        return jsonify([{
            'id': material.id,
            'name': material.name,
            'quantity': material.quantity,
            'unit_price': material.unit_price
        } for material in materials]), 200

    @app.route('/materials', methods=['POST'])
    def create_material():
        data = request.get_json()
        required_fields = ['name', 'quantity', 'unit_price']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_material = Material(
            name=data['name'],
            quantity=data['quantity'],
            unit_price=data['unit_price']
        )
        db.session.add(new_material)
        db.session.commit()
        return jsonify({'message': 'Material created successfully!'}), 201

    @app.route('/materials/<int:material_id>', methods=['GET'])
    def get_material(material_id):
        material = Material.query.get(material_id)
        if material:
            return jsonify({
                'id': material.id,
                'name': material.name,
                'quantity': material.quantity,
                'unit_price': material.unit_price
            }), 200
        else:
            return jsonify({'error': 'Material not found'}), 404

    @app.route('/materials/<int:material_id>', methods=['PATCH'])
    def update_material(material_id):
        material = Material.query.get(material_id)
        if not material:
            return jsonify({'error': 'Material not found'}), 404

        data = request.get_json()
        for field in ['name', 'quantity', 'unit_price']:
            if field in data:
                setattr(material, field, data[field])

        db.session.commit()
        return jsonify({'message': 'Material updated successfully!'}), 200

    @app.route('/materials/<int:material_id>', methods=['DELETE'])
    def delete_material(material_id):
        material = Material.query.get(material_id)
        if not material:
            return jsonify({'error': 'Material not found'}), 404

        db.session.delete(material)
        db.session.commit()
        return jsonify({'message': 'Material deleted successfully!'}), 200

   # Equipment Routes
    @app.route('/equipments', methods=['GET'])
    def get_equipments():
        equipments = Equipment.query.all()
        return jsonify([{
            'id': equipment.id,
            'name': equipment.name,
            'quantity': equipment.quantity,
            'cost': equipment.cost,
            'rental_price': equipment.rental_price,
            'purchase_date': equipment.purchase_date.isoformat() if equipment.purchase_date else None,
            'maintenance_date': equipment.maintenance_date.isoformat() if equipment.maintenance_date else None,
            'project_id': equipment.project_id,
            'status': equipment.status
        } for equipment in equipments]), 200

    @app.route('/equipments', methods=['POST'])
    def create_equipment():
        data = request.get_json()
        required_fields = ['name', 'quantity', 'cost', 'purchase_date', 'status']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_equipment = Equipment(
            name=data['name'],
            quantity=data['quantity'],
            cost=data['cost'],
            rental_price=data.get('rental_price'),  # Optional
            purchase_date=data['purchase_date'],  # Ensure this is in the correct format
            maintenance_date=data.get('maintenance_date'),  # Optional
            project_id=data['project_id'],  # Ensure this is provided
            status=data['status']
        )
        db.session.add(new_equipment)
        db.session.commit()
        return jsonify({'message': 'Equipment created successfully!'}), 201

    @app.route('/equipments/<int:equipment_id>', methods=['GET'])
    def get_equipment(equipment_id):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            return jsonify({
                'id': equipment.id,
                'name': equipment.name,
                'quantity': equipment.quantity,
                'cost': equipment.cost,
                'rental_price': equipment.rental_price,
                'purchase_date': equipment.purchase_date.isoformat() if equipment.purchase_date else None,
                'maintenance_date': equipment.maintenance_date.isoformat() if equipment.maintenance_date else None,
                'project_id': equipment.project_id,
                'status': equipment.status
            }), 200
        else:
            return jsonify({'error': 'Equipment not found'}), 404

    @app.route('/equipments/<int:equipment_id>', methods=['PATCH'])
    def update_equipment(equipment_id):
        equipment = Equipment.query.get(equipment_id)
        if not equipment:
            return jsonify({'error': 'Equipment not found'}), 404

        data = request.get_json()
        for field in ['name', 'quantity', 'cost', 'rental_price', 'maintenance_date', 'status']:
            if field in data:
                setattr(equipment, field, data[field])

        db.session.commit()
        return jsonify({'message': 'Equipment updated successfully!'}), 200

    @app.route('/equipments/<int:equipment_id>', methods=['DELETE'])
    def delete_equipment(equipment_id):
        equipment = Equipment.query.get(equipment_id)
        if not equipment:
            return jsonify({'error': 'Equipment not found'}), 404

        db.session.delete(equipment)
        db.session.commit()
        return jsonify({'message': 'Equipment deleted successfully!'}), 200

    # # Client Routes
    # @app.route('/clients', methods=['GET'])
    # def get_clients():
    #     clients = Client.query.all()
    #     return jsonify([{
    #         'id': client.id,
    #         'name': client.name,
    #         'email': client.email,
    #         'phone_number': client.phone_number
    #     } for client in clients]), 200

    # @app.route('/clients', methods=['POST'])
    # def create_client():
    #     data = request.get_json()
    #     required_fields = ['name', 'email', 'phone_number']
    #     if not all(field in data for field in required_fields):
    #         return jsonify({'error': 'Missing fields'}), 400

    #     new_client = Client(
    #         name=data['name'],
    #         email=data['email'],
    #         phone_number=data['phone_number']
    #     )
    #     db.session.add(new_client)
    #     db.session.commit()
    #     return jsonify({'message': 'Client created successfully!'}), 201

    # @app.route('/clients/<int:client_id>', methods=['GET'])
    # def get_client(client_id):
    #     client = Client.query.get(client_id)
    #     if client:
    #         return jsonify({
    #             'id': client.id,
    #             'name': client.name,
    #             'email': client.email,
    #             'phone_number': client.phone_number
    #         }), 200
    #     else:
    #         return jsonify({'error': 'Client not found'}), 404

    # @app.route('/clients/<int:client_id>', methods=['PATCH'])
    # def update_client(client_id):
    #     client = Client.query.get(client_id)
    #     if not client:
    #         return jsonify({'error': 'Client not found'}), 404

    #     data = request.get_json()
    #     for field in ['name', 'email', 'phone_number']:
    #         if field in data:
    #             setattr(client, field, data[field])

    #     db.session.commit()
    #     return jsonify({'message': 'Client updated successfully!'}), 200

    # @app.route('/clients/<int:client_id>', methods=['DELETE'])
    # def delete_client(client_id):
    #     client = Client.query.get(client_id)
    #     if not client:
    #         return jsonify({'error': 'Client not found'}), 404

    #     db.session.delete(client)
    #     db.session.commit()
    #     return jsonify({'message': 'Client deleted successfully!'}), 200



    # Client Routes
    @app.route('/clients', methods=['GET'])
    def get_clients():
        clients = Client.query.all()
        return jsonify([{
            'id': client.id,
            'company_name': client.company_name,
            'contact_name': client.contact_name,
            'email': client.email,
            'phone_number': client.phone_number,
            'address': client.address
        } for client in clients]), 200

    @app.route('/clients', methods=['POST'])
    def create_client():
        data = request.get_json()
        required_fields = ['company_name', 'contact_name', 'email', 'phone_number']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_client = Client(
            company_name=data['company_name'],
            contact_name=data['contact_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            address=data.get('address')  # Address is optional
        )
        db.session.add(new_client)
        db.session.commit()
        return jsonify({'message': 'Client created successfully!'}), 201

    @app.route('/clients/<int:client_id>', methods=['GET'])
    def get_client(client_id):
        client = Client.query.get(client_id)
        if client:
            return jsonify({
                'id': client.id,
                'company_name': client.company_name,
                'contact_name': client.contact_name,
                'email': client.email,
                'phone_number': client.phone_number,
                'address': client.address
            }), 200
        else:
            return jsonify({'error': 'Client not found'}), 404

    @app.route('/clients/<int:client_id>', methods=['PATCH'])
    def update_client(client_id):
        client = Client.query.get(client_id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404

        data = request.get_json()
        for field in ['company_name', 'contact_name', 'email', 'phone_number', 'address']:
            if field in data:
                setattr(client, field, data[field])

        db.session.commit()
        return jsonify({'message': 'Client updated successfully!'}), 200

    @app.route('/clients/<int:client_id>', methods=['DELETE'])
    def delete_client(client_id):
        client = Client.query.get(client_id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404

        db.session.delete(client)
        db.session.commit()
        return jsonify({'message': 'Client deleted successfully!'}), 200



    # Employee Routes
    @app.route('/employees', methods=['GET'])
    def get_employees():
        employees = Employee.query.all()
        return jsonify([{
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'role': employee.role,
            'email': employee.email,
            'phone_number': employee.phone_number,
            'hire_date': employee.hire_date.isoformat(),
            'salary': employee.salary,
            'project_id': employee.project_id
        } for employee in employees]), 200

    @app.route('/employees', methods=['POST'])
    def create_employee():
        data = request.get_json()
        required_fields = ['first_name', 'last_name', 'role', 'email', 'hire_date', 'salary', 'project_id']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        new_employee = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role'],
            email=data['email'],
            phone_number=data.get('phone_number'),
            hire_date=data['hire_date'],  # Ensure this is a date object
            salary=data['salary'],
            project_id=data['project_id']
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee created successfully!'}), 201

    @app.route('/employees/<int:employee_id>', methods=['GET'])
    def get_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            return jsonify({
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'role': employee.role,
                'email': employee.email,
                'phone_number': employee.phone_number,
                'hire_date': employee.hire_date.isoformat(),
                'salary': employee.salary,
                'project_id': employee.project_id
            }), 200
        else:
            return jsonify({'error': 'Employee not found'}), 404

    @app.route('/employees/<int:employee_id>', methods=['PATCH'])
    def update_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return jsonify({'error': 'Employee not found'}), 404

        data = request.get_json()
        for field in ['first_name', 'last_name', 'role', 'email', 'phone_number', 'hire_date', 'salary', 'project_id']:
            if field in data:
                setattr(employee, field, data[field])

        db.session.commit()
        return jsonify({'message': 'Employee updated successfully!'}), 200

    @app.route('/employees/<int:employee_id>', methods=['DELETE'])
    def delete_employee(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return jsonify({'error': 'Employee not found'}), 404

        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully!'}), 200
















