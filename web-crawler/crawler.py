from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def evaluate_path(elem, path):
    beautiful_path = "http://"
    nachalo = urlparse(elem)
    o = urlparse(path)
    if o.netloc is '':
        beautiful_path += nachalo.netloc
    else:
        beautiful_path += o.netloc

    if o.path is '':
        if nachalo.path is '':
            beautiful_path += '/'
        beautiful_path += nachalo.path
    else:
        beautiful_path += o.path
    if o.params is '':
        beautiful_path += nachalo.params
    else:
        beautiful_path += o.params
    beautiful_path += '?'
    if o.query is '':
        beautiful_path += nachalo.query
    else:
        beautiful_path += o.query
    if o.fragment is '':
        beautiful_path += nachalo.fragment
    else:
        beautiful_path += o.fragment
    # print(beautiful_path)
    return beautiful_path


engine = create_engine("sqlite:///data.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

httplinks = HTTP_links(http_links='http://register.start.bg')
session.add(httplinks)


list_column = session.query(HTTP_links.http_links).all()

for elem in list_column:
    try:
        response = requests.get(url=elem[0], timeout=10)
        content = response.content
    except requests.exceptions.ConnectionError:
        print("Connection refused")

    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        current_link = link.get('href')
        if current_link is not None and current_link is not '#top':
            new_link = evaluate_path(elem[0], current_link)
            new_linkk = HTTP_links(http_links=new_link)
            print(new_link)
            list_column.append((new_link,))
            session.add(new_linkk)
    session.commit()

                # get_server(httplinks)




# evaluate_path('http://register.start.bg/', '/link.php?id=54959')


