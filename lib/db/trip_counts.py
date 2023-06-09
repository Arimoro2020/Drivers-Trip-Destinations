import click
from datetime import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, aliased
from models import Trip

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option('--date_time', prompt='Enter the datetime in format %Y-%m-%d %H:%M:%S%',
              help='The date you want to start counting driver trips from')
def counts(date_time):
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
        print(f"driver_id: {result.driver_id}, trip_count: {result.trip_count}")

    session.close()

if __name__ == '__main__':
    counts()
