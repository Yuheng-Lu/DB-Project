from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db import db
from schemas import EmployeeSchema, EmployeeUpdateSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import EmployeeModel

blp = Blueprint("employees", __name__, description="Operations on employees")


@blp.route("/employees/<string:employee_id>")
class Employee(MethodView):
    @jwt_required()
    @blp.response(200, EmployeeSchema)
    def get(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        print(employee)

        return employee

    @jwt_required()
    def delete(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted."}

    @jwt_required()
    @blp.arguments(EmployeeUpdateSchema)
    @blp.response(200, EmployeeSchema)
    def put(self, employee_data, employee_id):
        employee = EmployeeModel.query.get(employee_id)
        if employee:
            employee.email = employee_data["email"]
            employee.first_name = employee_data["first_name"]
            employee.last_name = employee_data["last_name"]
            employee.phone = employee_data["phone"]
        else:
            employee = EmployeeModel(id=employee_id, **employee_data)

        db.session.add(employee)
        db.session.commit()
        return employee


@ blp.route("/employees")
class EmployeeList(MethodView):
    @jwt_required()
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        return EmployeeModel.query.all()

    @jwt_required()
    @blp.arguments(EmployeeSchema)
    @blp.response(200, EmployeeSchema)
    def post(self, employee_data):
        employee = EmployeeModel(**employee_data)
        try:
            db.session.add(employee)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A customer with that email/phone already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the customer.")
        return employee
