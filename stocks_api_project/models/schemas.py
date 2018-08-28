from marshmallow_sqlalchemy import ModelSchema

from . import (Stocks, Portfolio)


class StocksSchema(ModelSchema):
    class Meta:
        model = Stocks


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio

