from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import func
import ipdb

engine = create_engine('sqlite:///trip.db')

Session = sessionmaker(bind=engine)
session = Session()



query = text('''
    WITH RECURSIVE travel(path, last_lat, last_lon, total_distance, count_places) AS (
        SELECT cities.name AS path, cities.latitude AS last_lat, cities.longitude AS last_lon,
        CAST(:total_distance AS FLOAT) AS total_distance, CAST(:count_places AS INTEGER) AS count_places
        FROM cities
        WHERE cities.name = :start_city
        UNION ALL
        SELECT travel.path || :delimiter || city.name AS path, city.latitude AS last_lat, city.longitude AS last_lon,
        travel.total_distance + (
            :distance_multiplier_lon * (city.longitude - travel.last_lon) * (city.longitude - travel.last_lon)
            + :distance_multiplier_lat * (city.latitude - travel.last_lat) * (city.latitude - travel.last_lat)
        ) AS total_distance,
        travel.count_places + :count_places_increment AS count_places
        FROM travel
        JOIN cities AS city ON INSTR(travel.path, city.name) > 0
    )
    SELECT travel.path AS travel_path, travel.last_lat AS travel_last_lat, travel.last_lon AS travel_last_lon,
    travel.total_distance AS travel_total_distance, travel.count_places AS travel_count_places
    FROM travel
    WHERE travel.count_places = :num_places
    ORDER BY travel.total_distance ASC
''')



results = session.execute(query, {
    'total_distance': 0.0,
    'count_places': 1,
    'start_city': 'houston',
    'delimiter': '->',
    'distance_multiplier_lon': 69.1,
    'distance_multiplier_lat': 69.1,
    'count_places_increment': 1,
    'num_places': 8
}).all()

print("Query executed successfully.")

for row in results:
    print(row)
ipdb.set_trace()
session.close()
