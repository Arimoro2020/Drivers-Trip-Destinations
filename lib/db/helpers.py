#!/usr/bin/env python3
import click
import click
from sqlalchemy import create_engine, func
from sqlalchemy import and_
from sqlalchemy.sql.expression import cast
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Driver,Trip, City
from sqlalchemy.orm import aliased
from sqlalchemy import or_
from datetime import datetime, timedelta

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()



@click.command()
@click.option('--id', prompt='Enter id value',
              help='The driver id .')
def find_driver(id):
    """Simple program that finds a drivers record by means of the id."""
    result = session.query(Driver).filter(Driver.id == int(id)).first()
    click.echo(f"""

          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
    """)


@click.command()
@click.option('--name', prompt='Enter driver name',
              help='The driver name.')
    
def find_driver_by_name(name):
    """Simple program that finds a drivers record by means of the name."""
    results = session.query(Driver).filter(Driver.name.like(f'%{name}%')).limit(5)
    
    for result in results:
        click.echo(f"""

          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
        """)

@click.command()
@click.option('--age', prompt='Enter age to consider',
              help=' The age in years - a number .')
    
def years_to_retirement(age):
    """Simple program that get the drivers that will turn a given age in a year or less."""

    current_date = datetime.now().date()

    # Calculate the future date one year from now
    future_date = current_date + timedelta(days=365)

    # Calculate the date when the person turns 60
    sixty_years_date = current_date - timedelta(days=365 * int(age))

    # Query persons who will be 60 or older in one year or less
    results = session.query(Driver).filter(
        Driver.date_of_birth <= sixty_years_date).all()

    # Execute the query and get the results
    

# Print the results

    click.echo(f""" Count is: {len(results)}
          There are {len(results)} drivers that will turn {age} in a year or less.
          """)
    
    for result in results:
        click.echo(f"""
          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
        """)     


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
        click.echo(f""" 
              driver_id: {result.driver_id}, destinations: {result.destinations}"""     
        )



@click.command()
@click.option('--date_time', prompt='Enter the datetime in format %Y-%m-%d %H:%M:%S%',
              help='The date you want to start counting driver trips from')
def trip_counts(date_time):
    """Simple program that gets 10 highest trip counts for drivers from a given date."""

    date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

    included_trips = session.query(
        Trip.id,
        Trip.city_id,
        Trip.driver_id,
        Trip.destinations,
        Trip.created_at,
        Trip.updated_at
    ).filter(Trip.created_at >= date_time).cte(name="included_trips", recursive=True)

    incl_alias = aliased(included_trips, name="trp")
    trips_alias = aliased(Trip, name="t")
    included_trips = included_trips.union_all(
        session.query(
            trips_alias.id,
            trips_alias.city_id,
            trips_alias.driver_id,
            trips_alias.destinations,
            trips_alias.created_at,
            trips_alias.updated_at
        ).filter(trips_alias.driver_id == incl_alias.c.driver_id)
    )

    trip_query = session.query(
        included_trips.c.driver_id,
        included_trips.c.id,
        func.count(included_trips.c.id).label('trip_count')
    ).group_by(included_trips.c.driver_id).order_by(func.count(included_trips.c.id).desc()).limit(10).all()

    for result in trip_query:
        click.echo(f"driver_id: {result.driver_id}, trip_count: {result.trip_count}")

    