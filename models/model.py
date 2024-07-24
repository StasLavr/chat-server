from sqlalchemy import MetaData, Table, Column, Boolean, Integer, String, TIMESTAMP, ForeignKey
import datetime
meta = MetaData()

users = Table(
    'user',
    meta,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('fullname', String, nullable=False),
    Column('email', String, nullable=False),
    Column('registered_time', TIMESTAMP, default=datetime.datetime.utcnow),
    Column('hashed_password', String, default=True,nullable=False),
    Column('is_active', Boolean, default=False, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)