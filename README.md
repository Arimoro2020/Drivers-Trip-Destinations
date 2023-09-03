# Drivers-Trip-Destinations-CLI-App


# App Description:

 A helpful CLI app for performing complex queries on a database that allows non-technical users to complete many of the same tasks from the Python shell without very much training at all.



# Basic Directory Structure


<img width="486" alt="Screen Shot 2023-06-10 at 17 33 47 PM" src="https://github.com/Arimoro2020/Drivers-Trip-Destinations-CLI-App/assets/73043768/5f2c9637-2259-4c45-b399-0cb2a442636e">




# Entity Relationship Diagram (ERD) for Database Tables and schemas 


<img width="1102" alt="ERD" src="https://github.com/Arimoro2020/Drivers-Trip-Destinations-CLI-App/assets/73043768/15f3f381-98bd-4eb7-b93d-3bc9575e05ed">






# cli.py: an interactive script run with python cli.py, containing several import statements, an if __name__ == "__main__" block and several function calls inside of that block kept in helpers.py.





# models.py:  Inheritance from Base, a declarative_base object, allows us to avoid rewriting code, and three related (associated) tables.






# MVP:


  
  # -find_driver.py: Simple program that finds a driver's record using the id.


  # -find_driver_by_name.py: Simple program that finds a driver's record using the name.


  # -years_to_retirement.py: This simple program gets the drivers who will turn a certain age in a year or less.


  # -driving_dangerously.py: Simple program that finds possible culprits for reported unsafe driving.


  # -trip_counts.py: Simple program that gets the 10 highest trip counts for drivers from a given date.


# Probable New Features to Consider:
Features to help in determining the best routes for a trip to certain cities, to determine the distance between 2 cities, and for performing CRUD operations. 



