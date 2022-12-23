from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db import db
from schemas import InsuranceSchema, InsuranceUpdateSchema
from models import InsuranceModel, CustomerModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Insurances", "insurances",
                description="Operations on insurances")


@blp.route("/insurances/<string:insurance_id>")
class Insurance(MethodView):
    @jwt_required()
    @blp.response(200, InsuranceSchema)
    def get(self, insurance_id):
        insurance = InsuranceModel.query.get_or_404(insurance_id)
        return insurance

    @jwt_required()
    def delete(self, insurance_id):
        insurance = InsuranceModel.query.get_or_404(insurance_id)
        db.session.delete(insurance)
        db.session.commit()
        return {"message": "Insurance deleted."}

    @jwt_required()
    @blp.arguments(InsuranceUpdateSchema)
    @blp.response(200, InsuranceSchema)
    def put(self, insurance_data, insurance_id):
        insurance = InsuranceModel.query.get(insurance_id)
        if insurance:
            insurance.price = insurance_data["price"]
            insurance.name = insurance_data["name"]
            insurance.type = insurance_data["type"]
        else:
            insurance = InsuranceModel(id=insurance_id, **insurance_data)
        db.session.add(insurance)
        db.session.commit()
        return insurance


@blp.route("/insurances")
class InsuranceList(MethodView):
    @jwt_required()
    @blp.response(200, InsuranceSchema)
    @blp.response(200, InsuranceSchema(many=True))
    def get(self):
        return InsuranceModel.query.all()

    @jwt_required()
    @blp.arguments(InsuranceSchema)
    @blp.response(201, InsuranceSchema)
    def post(self, insurance_data):
        insurance = InsuranceModel(**insurance_data)
        if CustomerModel.query.get(insurance.customer_id):
            try:
                db.session.add(insurance)
                db.session.commit()
            except IntegrityError:
                abort(
                    400,
                    message="Insurance exists, try to update the insurace or choose a different name",
                )
            except SQLAlchemyError:
                abort(500, message="An error occurred while inserting the insurance.")
            return insurance

        else:
            abort(
                404,
                message="Customer not found",
            )
