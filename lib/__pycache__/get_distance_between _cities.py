import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import City




engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option('--name_1', prompt='Enter city name',
              help='The first city to find distance from')
@click.option('--name_2', prompt='Enter the second city name',
              help='The second city to find distance to')
def get_distance_between_cities(name_1, name_2):
    """Simple program that finds the distance between two cities in the database."""
    # result = session.query(Driver).filter(Driver.id == int(id)).first()
    # print(f"""
    #         id : {result.id}
    #         name : {result.name}
    #         date_of_birth : {result.date_of_birth}v
    #      """
    # )
    
                                             
                        

if __name__ == '__main__':
    find_driver_by_id()
    
