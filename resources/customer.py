from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from flask_jwt_extended import jwt_required
from schemas import CustomerSchema, CustomerUpdateSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import CustomerModel

blp = Blueprint("customers", __name__, description="Operations on customers")


@blp.route("/customers/<string:customer_id>")
class Customer(MethodView):
    @jwt_required()
    @blp.response(200, CustomerSchema)
    def get(self, customer_id):
        customer = CustomerModel.query.get_or_404(customer_id)
        return customer

    @jwt_required()
    def delete(self, customer_id):
        customer = CustomerModel.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted"}, 200

    @jwt_required()
    @blp.arguments(CustomerUpdateSchema)
    @blp.response(200, CustomerSchema)
    def put(self, customer_data, customer_id):
        customer = CustomerModel.query.get(customer_id)
        if customer:
            customer.address = customer_data["address"]
            customer.age = customer_data["age"]
            customer.email = customer_data["email"]
            customer.first_name = customer_data["first_name"]
            customer.gender = customer_data["gender"]
            customer.height = customer_data["height"]
            customer.last_name = customer_data["last_name"]
            customer.number_of_child = customer_data["number_of_child"]
            customer.phone = customer_data["phone"]
            customer.weight = customer_data["weight"]
        else:
            customer = CustomerModel(id=customer_id, **customer_data)

        db.session.add(customer)
        db.session.commit()
        return customer


@ blp.route("/customers")
class CustomerList(MethodView):
    @jwt_required()
    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return CustomerModel.query.all()

    @jwt_required()
    @blp.arguments(CustomerSchema)
    @blp.response(200, CustomerSchema)
    def post(self, customer_data):
        customer = CustomerModel(**customer_data)
        try:
            db.session.add(customer)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A customer with that email/phone already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the customer.")

        return customer
