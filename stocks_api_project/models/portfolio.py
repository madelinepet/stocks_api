from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from .stocks import Stock
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base


class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    # accounts below has to match the back_populates in the class Account
    accounts = relationship('Account', back_populates='portfolios')
    stocks = relationship(Stock, back_populates='portfolios')

    @classmethod
    def new(cls, request=None, **kwargs):
        """ A post method, if the request cannot access the db, raise imported error
        """
        if request.dbsession is None:
            raise DBAPIError
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

    @classmethod
    def one(cls, request=None, pk=None):
        """ grabs one record with a unique id
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)


