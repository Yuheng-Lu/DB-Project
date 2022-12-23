from db import db


class InsuranceModel(db.Model):
    __tablename__ = "insurances"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    type = db.Column(db.String(80), unique=False, nullable=True)
    customer_id = db.Column(
        db.Integer, db.ForeignKey("customers.id"), unique=False, nullable=False
    )
    # customer = db.relationship(
    #    "CustomerModel", back_populates="insurance", lazy=True)
    # employee_id = db.Column(db.Integer, unique=False, nullable=False)
