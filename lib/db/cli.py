#!/usr/bin/env python3
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
from helpers import (find_driver,
find_driver_by_name, years_to_retirement,
driving_dangerously,trip_counts)

click.echo('Starting session...')
engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()
click.echo('Session started...')

@click.group()
def cli():
    pass
@click.command()
def closing_session():
    """Simple program that closes the session."""
    session.close()
    click.echo('session closed...')

cli.add_command(find_driver)
cli.add_command(find_driver_by_name)
cli.add_command(years_to_retirement)
cli.add_command(driving_dangerously)
cli.add_command(trip_counts)
cli.add_command(closing_session)





if __name__ == '__main__':
    cli()
    find_driver()
    find_driver_by_name()
    years_to_retirement()
    driving_dangerously()
    trip_counts()
    closing_session()
    