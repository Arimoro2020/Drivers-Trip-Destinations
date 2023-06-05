from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///trip.db')

Base = declarative_base()

city_driver = Table(
    'city_drivers',
    Base.metadata,
    Column('city_id', ForeignKey('city.id'), primary_key=True),
    Column('driver_id', ForeignKey('driver.id'), primary_key=True),
    extend_existing=True,
)

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    latitude = Column(Float())
    longitude = Column(Float())

    drivers = relationship('Driver', secondary=city_driver, back_populates='cities')
    trips = relationship('Trip', backref=backref('city'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'City(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'latitude={self.latitude}, ' + \
            f'longitude={self.longitude})'
    

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    date_of_birth = Column(String())

    cities = relationship('City', secondary=city_driver, back_populates='drivers')
    trips = relationship('Trip', backref=backref('driver'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Driver(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'date_of_birth={self.date_of_birth})'
    

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer(), primary_key=True)
    city_id = Column(Integer(), ForeignKey('cities.id'))
    driver_id = Column(Integer(), ForeignKey('drivers.id'))
    destinations = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())


    def __repr__(self):
        return f'Trip(id={self.id}, ' + \
            f'driver_id={self.driver_id}, ' + \
            f'destinations={self.destinations}, ' + \
            f'created_at={self.created_at}, ' + \
            f'updated_at={self.updated_at}, ' + \
            f'city_id={self.city_id})'



            
