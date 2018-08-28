from .meta import Base
from sqlalchemy.orm import relationship
from .associations import roles_association
import requests

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)


class AccountRole(Base):
    """ autoincrement=True as an arg is implied if there's a primary key
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')
