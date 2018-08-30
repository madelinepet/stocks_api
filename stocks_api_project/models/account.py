from .meta import Base
from sqlalchemy.orm import relationship
from .role import AccountRole
from .associations import roles_association
from .portfolio import Portfolio
from datetime import datetime as dt
# cryptacular gives ability to hash and check a PW
from cryptacular import bcrypt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)
manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # these relationships do not exist in the db, it allows us to use dot
    # notation in an instance to access the roles that belong to this account
    # in the db. This is sqlalchemy magic
    # back_populates allows us to get back user that owns the accounts instance,
    # matches the attribute name on the portfolio model
    portfolios = relationship(Portfolio, back_populates='accounts')
    # back_populates point to an attribute on Accountrole
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        """ Fix this to hash the password before storing it in the db!!!!
        """
        self.email = email
        # salt 10 gives us ability to hash password
        self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        """ Register a new user, if not session, raise error, create a user
        class with username and password, add to db, get the user record and
        hand it back out of this method
        """
        if not request.dbsession:
            raise DBAPIError
        user = cls(email, password)
        request.dbsession.add(user)
        # assigns a role or permissions to a user
        # default role is admin-- this isn't very safe
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()
        user.roles.append(admin_role)
        # next line completes the transaction by committing in, if we don't
        # flush, admin role doesn't save
        request.dbsession.flush()
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """ Validate that the user exists and that they are who they are
        """
        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()

        except DBAPIError:
            return None

        if account is not None:
            # check to see if the passwords match!
            if manager.check(account.password, password):
                return account

        # otherwise, handle this on view side
        return None
