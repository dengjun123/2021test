from sqlalchemy import creat_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'stuq.ceshiren.com'
user = 'hogwarts_python'
password = 'hogwarts_python'
db = 'hogwarts_python'
charset = 'utf8mb4'

Base = declarative_base()

class User(Base):
    __tablename__ = 'seveniruby_user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)


def test_orm():
    engine = creat_engine(
        'mysql+pymysql://{user}:{password}@{host}/{db}'.format(host=host, db=db, user=user, password=password),
        echo=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    u1 = User(
        username="seveniruby",
        password="password",
        email="seveniruby@ceshiren.com"
    )
    session.add(u1)
    session.commit()
    u2 = session.query(User).filter_by(usernmae="seveniruby").first()
    print(u2.username)

    assert u1.username == u2.username
