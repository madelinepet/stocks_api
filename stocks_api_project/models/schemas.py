from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
# marshmallow gets the records that belong to the ids in this fields and
# creates a list of role objects on the account when we send back the response
# to the client

from . import (Stock, Portfolio, Account, AccountRole)


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    # exclusively ask for one or my columns from a record. Excludes password
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class StocksSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated'
    ))

    class Meta:
        model = Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


