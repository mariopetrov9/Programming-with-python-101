from sqlalchemy import Column, Integer, String, Float, ForeignKey,\
                       DateTime
from sqlalchemy.orm import relationship
from base import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float)
    message = Column(String)
    salt = Column(String)


class Login_attempts(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    client = relationship(Client, backref="login_attempts")
    # za da moje client.login_attempts
    attempt_status = Column(String)
    time = Column(DateTime)


class Blocked_users(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    client = relationship(Client, backref="blocked_users")
    block_start = Column(DateTime)
    block_end = Column(DateTime)

