import click
from datetime import datetime, timedelta
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Driver




engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()



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

    print(f""" Count is: {len(results)}
          There are {len(results)} drivers that will turn {age} in a year or less.
          """)
    
    for result in results:
        print(f"""
          id: {result.id},
          name: {result.name},
          date_of_birth: {result.date_of_birth}
        """)                        
session.close()                    

if __name__ == '__main__':
    years_to_retirement()

    
