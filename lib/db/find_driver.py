import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Driver




engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option('--id', prompt='Enter id value',
              help='The driver id .')
def find_driver(id):
    """Simple program that finds a drivers record by means of the id."""
    result = session.query(Driver).filter(Driver.id == int(id)).first()
    print(f"""

          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
    """)



if __name__ == '__main__':
    find_driver()
    
    



