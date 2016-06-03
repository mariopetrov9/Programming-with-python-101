from base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    server = Column(String, nullable=True)
    visited_at = Column(DateTime, nullable=True)

    def __str__(self):
        return self.url


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    domain_id = Column(Integer, ForeignKey(Domain.id))
    domain = relationship(Domain, backref='links')
    visited_at = Column(DateTime, nullable=True)

    def __str__(self):
        return self.url

    def __repr__(self):
        return str(self)
