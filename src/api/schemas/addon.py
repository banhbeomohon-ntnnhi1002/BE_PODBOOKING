from marshmallow import Schema, fields

class AddonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Decimal(as_string=True, required=True)
    currency = fields.Str()
    is_active = fields.Bool()
    service_id = fields.Int()
