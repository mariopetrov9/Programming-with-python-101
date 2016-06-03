from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from controller import *
from views import MainView

from settings import DB_CONNECTION_STRING


engine = create_engine(DB_CONNECTION_STRING)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# main_controller = MainController(session)
reg_controller = RegisterController(session)
log_controller = LoginController(session)
main_view = MainView(reg_controller, log_controller)

main_view.main_menu()
