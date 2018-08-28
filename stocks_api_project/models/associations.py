# this is the file where the association between role and account lives
# many: many relationship, any user can have many roles,
import requests
from sqlalchemy import Table, Column, Integer, ForeignKey
# not importing base here from metadata because we are doing this a different way
from .meta import metadata

roles_association = Table(
    'roles_association',
    metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id'))
)
# these lines above is like setting up, but you need
# from .meta import Base above instead of metadata
# class RolesAssociation(Base):
#     __tablename__ = 'roles_association'
#     account_id = Column(Integer, ForeignKey('accounts.id'))
#     role_id = Column(Integer, ForeignKey('account_roles.id'))


