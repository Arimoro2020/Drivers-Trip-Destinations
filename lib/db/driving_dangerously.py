import click
from sqlalchemy import create_engine, func
from sqlalchemy import and_
from sqlalchemy.sql.expression import cast
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Driver,Trip, City
import find_driver
from sqlalchemy.orm import aliased
from sqlalchemy import or_
from datetime import datetime



engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option('--city', prompt='Enter the city name the unsafe driving was witnessed:',
              help=' The city the unsafe driving was')
@click.option('--date_time', prompt='Enter the datetime in formate %Y-%m-%d %H:%M:S%:',
              help=' The datetime the unsafe driving was sighted')
    
def driving_dangerously(city, date_time):
    """Simple program that finds possible culprits for reported unsafe driving."""

    date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

    query = session.query(City.id).filter(City.name == city).first()

    results = session.query(Trip).filter(Trip.created_at <= date_time).filter(date_time<= Trip.updated_at).\
        filter(Trip.city_id == query[0]).\
            filter(Trip.destinations.contains(city))



    
        
    for result in results:
        print(f""" 
              driver_id: {result.driver_id}, destinations: {result.destinations}"""     
        )

      
         
    
session.close()                    

if __name__ == '__main__':
    driving_dangerously()
