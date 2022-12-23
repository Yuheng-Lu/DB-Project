from marshmallow import Schema, fields


class PlainInsuranceSchenma(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Float(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)


class PlainCustomerSchenma(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    age = fields.Int(required=True)
    weight = fields.Float(required=True)
    height = fields.Float(required=True)
    gender = fields.Str(required=True)
    number_of_child = fields.Int(required=True)
    address = fields.Str(required=True)


class PlainEmployeeSchenma(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)


class InsuranceSchema(PlainInsuranceSchenma):
    customer_id = fields.Str(required=True)


class CustomerSchema(PlainCustomerSchenma):
    employee_id = fields.Str(required=True)
    insurance = fields.List(fields.Nested(
        PlainInsuranceSchenma(), dump_only=True))


class EmployeeSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    customer = fields.List(fields.Nested(
        PlainCustomerSchenma(), dump_only=True))


class InsuranceUpdateSchema(Schema):
    price = fields.Float(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)


class CustomerUpdateSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    age = fields.Int(required=True)
    weight = fields.Float(required=True)
    height = fields.Float(required=True)
    gender = fields.Str(required=True)
    number_of_child = fields.Int(required=True)
    address = fields.Str(required=True)


class EmployeeUpdateSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
