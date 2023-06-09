from sqlalchemy import create_engine, Column, String, Float, Integer, func, select,text
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base
import click
from models import City

# Define the base class for declarative models
# Base = declarative_base()

# # Define the City model
# class City(Base):
#     __tablename__ = 'cities'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)

# Create the engine and session

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()



@click.command()


# Create the subquery for the recursive part
def routes():
    # """Simple program that ranks the routes between the cities in the database based on distance."""

    # # Define the initial parameters
    # start_city_name = start_city_name
    # max_count_places = 8
    sql = """
WITH RECURSIVE travel(path, last_lat, last_lon,
    total_distance, count_places) AS (
  SELECT
    name, latitude, longitude, ?, ?
    FROM cities
    WHERE name = ?
  UNION ALL
  SELECT
    -- add to the current places_chain
    travel.path || ? || cities.name,
    cities.latitude,
    cities.longitude,
    -- add to the current total_distance
    travel.total_distance +
               sqrt(power(((cities.longitude - last_lon) * ?),?) + power(((cities.latitude - last_lat)* ?),?)),
    travel.count_places + ?
  FROM cities, travel
  WHERE position(cities.name IN travel.path) = 0 
)
SELECT *
FROM travel
WHERE count_places = ? """.format(0, 1, 'houston', '->', 69.1, 2, 69.1, 2, 1, '%', '%', 8, 8)
    # parameters =  (0, 1, 'houston', '->', 69.1, 2, 69.1, 2, 1, '%', '%', 8, 8)
    
#     # Create the recursive CTE query
#     included_cities = session.query(
#         City.name.label('path'),
#         City.latitude.label('last_lat'),
#         City.longitude.label('last_lon'),
#         func.literal(0).label('total_distance'),
#         func.literal(1).label('count_places')
#     ).filter(
#         City.name == start_city_name
#     ).cte(recursive=True)

#     included_alias = aliased(included_cities, name='travel')
#     cities_alias = aliased(City, name='cities')

#     recursive_subquery = session.query([
#     (included_alias.c.path.op('||')('->') + func.concat('->', cities_alias.name)).label('path'),
#     cities_alias.latitude.label('last_lat'),
#     cities_alias.longitude.label('last_lon'),
#     (included_alias.c.total_distance +
#      func.sqrt(
#          func.power(((cities_alias.longitude - included_alias.c.last_lon) * 69.1), 2) +
#          func.power(((cities_alias.latitude - included_alias.c.last_lat) * 69.1), 2))
#     ).label('total_distance'),
#     (included_alias.c.count_places + 1).label('count_places')
# ]).select_from(
#     included_alias.join(
#         cities_alias,
#         ~func.concat(included_alias.c.path, '->').contains(func.concat(cities_alias.name, '->'))
#     )
# ).where(
#     included_alias.c.count_places < max_count_places
# )

#     # Create the final query
#     final_query = session.query([
#         recursive_subquery.c.path,
#         recursive_subquery.c.last_lat,
#         recursive_subquery.c.last_lon,
#         recursive_subquery.c.total_distance,
#         recursive_subquery.c.count_places
#     ]).where(
#         recursive_subquery.c.count_places == max_count_places
#     ).order_by(
#         recursive_subquery.c.total_distance
#     )

#     # Execute the final query
    results = session.execute(text(sql))
    for user_obj in results.scalars():
        print(f"{user_obj.path} {user_obj.total_distance}")


#     # Print the results
#     for row in results:
#         print(row)

session.close()



if __name__ == '__main__':
    routes()
    
