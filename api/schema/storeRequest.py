from marshmallow import Schema,fields

class StoreRequest(Schema):
    file_name = fields.Str(required=True)
    access_token = fields.Str(required=True)
