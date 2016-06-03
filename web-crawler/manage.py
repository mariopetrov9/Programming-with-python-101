import sys
from base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from settings import *


COMMANDS = ['createdb', 'crawl', 'collect', 'seed']

if len(sys.argv[1:]) == 0:
    sys.exit('Provide one of the following: {}'.format(", ".join(COMMANDS)))

command = sys.argv[1]

if command not in COMMANDS:
    sys.exit('{} not found'.format(command))


engine = create_engine(DB_CONNECTION_STRING)


def createdb():
    Base.metadata.create_all(engine)


def collect():
    pass


def seed():
    Session = sessionmaker(bind=engine)
    session = Session()

    domain1 = models.Domain(url='http://register.start.bg/')

    link1 = models.Link(url=domain1.url,
                        domain=domain1)

    session.add(domain1)
    session.add(link1)

    session.commit()

func = globals()[command]
func()
