"""
SQL Homework done with SQL Alchemy ORM
"""

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float

engine = create_engine('sqlite:///sales.db', echo=False)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


class Provider(Base):
    """
    Providers schema - providers are listed here, Canteens are going to be linked to providers
    in a many-to-one fashion
    """
    __tablename__ = 'PROVIDER'

    id = Column(Integer, primary_key=True)
    providername = Column(String)


class Canteen(Base):
    """
    Canteens schema - list of canteens
    Using Float type for time_open and time_closed columns for easier comparison

    Not using Time i.e. datetime.time() objects to make things easier
    """
    __tablename__ = 'CANTEEN'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    time_open = Column(Float)
    time_closed = Column(Float)
    provider_ID = Column(Integer, ForeignKey('PROVIDER.id'))
    provider = relationship('Provider', back_populates='canteens')

    def __repr__(self):
        return "Canteen( ID: '%s', Name: '%s', Location: '%s', " \
               "Time Open: '%1.2f', Time Closed: '%1.2f', Provider: %s)" \
               "" % (self.id, self.name, self.location, self.time_open,
                     self.time_closed, self.provider.providername)


Provider.canteens = relationship('Canteen', order_by=Canteen.id, back_populates='provider')

"""
Dropping tables before recreating them so that every time 
the program runs the DB is fresh
"""

Provider.__table__.drop(engine)
Canteen.__table__.drop(engine)

Base.metadata.create_all(engine)

p1 = Provider(providername='bitStop Kohvik OÜ', canteens=[
    Canteen(name='bitStop KOHVIK', location='IT College, Raja 4c',
            time_open=9.30, time_closed=16.00)
])

p2 = Provider(providername='Rahva toit', canteens=[
    Canteen(name='Economics- and social science building canteen',
            location='Akadeemia tee 3 SOC- building',
            time_open=8.30, time_closed=18.30),
    Canteen(name='Library canteen', location='Akadeemia tee 1/Ehitajate tee 7',
            time_open=8.30, time_closed=19.00),
    Canteen(name='U06 building canteen', location='U06 building',
            time_open=9.00, time_closed=16.00)
])

p3 = Provider(providername='Baltic Restaurants Estonia AS', canteens=[
    Canteen(name='Main building Deli cafe', location='Ehitajate tee 5 U01 building',
            time_open=9.00, time_closed=16.30),
    Canteen(name='Main building Daily lunch restaurant', location='Ehitajate tee 5 U01 building',
            time_open=9.00, time_closed=16.00),
    Canteen(name='Natural Science building canteen', location='Akadeemia tee 15 SCI building',
            time_open=9.00, time_closed=16.00),
    Canteen(name='ICT building canteen', location='Raja 15/Mäepealse 1',
            time_open=9.00, time_closed=16.00)
])

p4 = Provider(providername='TTÜ Sport OÜ', canteens=[
    Canteen(name='Sports building canteen', location='Männiliiva 7 S01 building',
            time_open=11.00, time_closed=20.00)
])

Session = sessionmaker(bind=engine)
session = Session()

"""
Trying to add first provider by one, the rest all together, rolling back on error
Closing the session after the transactions are completed
"""

print("Adding providers...\n")
try:
    session.add(p1)
    session.add_all([
        p2, p3, p4
    ])
    session.commit()
except Exception:
    session.rollback()
    raise
finally:
    session.close()

"""
Selecting all the canteens that are open from 16.15 to 18.00 (inclusive)
"""

print("Selecting all Canteens with opening times 16.15-18.00")
try:
    result = session.query(Canteen).filter(Canteen.time_open < 16.15, Canteen.time_closed >= 18.00)
    for row in result:
        print(row)
except:
    print("exception encountered")
    session.rollback()
    raise
finally:
    session.close()

"""
Selecting all queries where provider is Rahva Toit
"""

print("Selecting all canteens from Rahva Toit")
try:
    result = session.query(Provider).filter(Provider.providername == 'Rahva toit')
    for row in result:
        print("ID:", row.id, "Name:", row.providername)
        for canteen in row.canteens:
            print(canteen)
except Exception:
    print(Exception)
    session.rollback()
    raise
finally:
    session.close()

"""
Different way of selecting all the Rahva Toit canteens
"""

print("Selecting all canteens from Rahva Toit - different variant")
try:
    result = session.query(Canteen).filter(Canteen.provider.has(Provider.providername == "Rahva toit"))
    for row in result:
        print(row)
except:
    print("exception encountered")
    session.rollback()
    raise
finally:
    session.close()
