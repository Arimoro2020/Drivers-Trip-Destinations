import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Driver




engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()



@click.command()
@click.option('--name', prompt='Enter driver name',
              help='The driver name.')
    
def find_driver_by_name(name):
    """Simple program that finds a drivers record by means of the name."""
    results = session.query(Driver).filter(Driver.name.like(f'%{name}%')).limit(5)
    
    for result in results:
        print(f"""

          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
        """)
                                           
                        

if __name__ == '__main__':
    find_driver_by_name()
    


