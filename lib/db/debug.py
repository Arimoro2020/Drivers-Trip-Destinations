
# #!/usr/bin/env python3
# from sqlalchemy import create_engine, select, text, func, cast, Float, Integer
# from sqlalchemy.orm import sessionmaker, aliased
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Float
# from models import City

# Base = declarative_base()

# class City(Base):
#     __tablename__ = 'cities'
#     name = Column(String, primary_key=True)
#     latitude = Column(Float)
#     longitude = Column(Float)

# engine = create_engine('sqlite:///trip.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# # Create the initial subquery
# initial_query = session.query(
#     City.name.label('path'),
#     City.latitude.label('last_lat'),
#     City.longitude.label('last_lon'),
#     cast(0, Float).label('total_distance'),
#     cast(1, Integer).label('count_places')
# ).filter(
#     City.name == 'London'
# ).cte(name='travel', recursive=True)

# # Create the recursive subquery
# city_alias = aliased(City, name='city')
# recursive_query = initial_query.union_all(
#     session.query(
#         func.concat(initial_query.c.path, '->', city_alias.name).label('path'),
#         city_alias.latitude.label('last_lat'),
#         city_alias.longitude.label('last_lon'),
#         (initial_query.c.total_distance + func.sqrt(func.power(((city_alias.longitude - initial_query.c.last_lon) * 69.1), 2) + func.power(((city_alias.latitude - initial_query.c.last_lat) * 69.1), 2))).label('total_distance'),
#         (initial_query.c.count_places + 1).label('count_places')
#     ).select_from(initial_query.join(
#         city_alias,
#         func.position(city_alias.name, initial_query.c.path) == 0
#     ))
# )

# # Create the final query
# final_query = session.query(recursive_query).filter(recursive_query.c.count_places == 8).order_by(recursive_query.c.total_distance.asc())

# # Execute the query and fetch the results
# results = final_query.all()

# # Process the results
# for row in results:
#     print(row)

# # Close the session
# session.close()

