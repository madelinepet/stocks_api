from .meta import Base
from sqlalchemy.orm import relationship
from .role import AccountRole
from .associations import roles_association
from .stocks import Stock
import requests
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime,
)


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # these relationships do not exist in the db, it allows us to use dot
    # notation in an instance to access the roles that belong to this account
    # in the db. This is sqlalchemy magic
    # back_populates allows us to get back user that owns the stock instance
    stocks = relationship(Stock, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        """ Fix this to hash the password before storing it in the db!!!!
        """
        self.email = email
        self.password = password  # NOTE: THIS ISN'T SAFE!!!!! TODO: fix it tomorrow!!!

    @classmethod
    def new(cls, request, email=None, password=None):
        """ Register a new user, if not session, raise error, create a user class with username and password, add to db, get the user record and hand it back out of this method
        """
        if not request.dbsession:
            raise DBAPIError
        user = cls(email, password)
        request.dbsession.add(user)
        # TODO: assign a role or permissions to a user
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """ Validate that the user exists and that they are who they are
        """
        # TODO: complete this part tomorrow!
        pass


