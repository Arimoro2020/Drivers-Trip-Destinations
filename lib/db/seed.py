#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import City, Driver, Trip
from faker import Faker
import random


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()




fake = Faker()

drivers = [
    Driver(
        name=fake.name(),
        date_of_birth=fake.date()
    )
for i in range(50)]

session.add_all(drivers)
session.commit()

city_list = ['houston', 'dallas', 'austin', 'plano', 'arlington', 'odessa', 'conroe', 'waco']
lat_long = [[-95.369804, 29.760427], [-96.796989, 32.776665], [-97.7475016, 30.2642643],[-96.699255, 33.021829],[-97.10835, 32.7356333],[2.3246044, 48.8415356],[-95.4581224, 30.3126309],[-97.1299889, 31.558389]]

cities = [
    City(
        name=city_list[i],
        longitude=lat_long[i][0],
        latitude=lat_long[i][1]
    )
for i in range(0,8)]

session.add_all(cities)



trips = [
    Trip(
         city_id= fake.random.randint(1, 9),
         driver_id= fake.random.randint(1, 49),
         destinations = str(fake.random.choices(city_list, k=4)),
         created_at = fake.date_between(start_date=datetime(2022,1,1), end_date=datetime(2022,1,4)),
         updated_at = fake.date_between(start_date=datetime(2022, 1, 5), end_date=datetime(2022, 1,8)),
    )
for i in range(50)]


session.add_all(trips)

session.commit()