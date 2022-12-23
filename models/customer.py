from db import db


class CustomerModel(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Float(precision=2), unique=False, nullable=False)
    height = db.Column(db.Float(precision=2), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    number_of_child = db.Column(db.Integer, unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    employee_id = db.Column(
        db.Integer, db.ForeignKey("employees.id"), unique=False, nullable=False
    )
    # employee = db.relationship(
    #    "EmployeeModel", back_populates="customer", cascade="all, delete")
    insurance = db.relationship(
        "InsuranceModel", backref="customer", lazy="dynamic", cascade="all, delete")
    # account_number = relationship("Account", back_populates="customers")
