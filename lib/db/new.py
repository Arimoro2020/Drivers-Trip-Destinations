# /Users/yemiarimoro/Development/code/phase-3/Drivers-Trip-Destinations/lib/db

# Make sure to replace `'your_database_connection_string'` with the actual connection string for your database, `'your_city_name'` with the desired city name, and `'cities'` with the actual table name if it's different.

# This code creates two subqueries using SQLAlchemy's Common Table Expressions (CTE). The first subquery represents the initial query that selects the starting city. The second subquery represents the recursive query that performs the union with the initial query and recursively selects the next cities based on the conditions.

# Finally, the final query is created by selecting from the recursive query and applying the filtering and ordering conditions. The query is executed, and the results are fetched and processed accordingly.

# Note: The code assumes you have the necessary imports (`Column`, `String`, `Float`, etc.) from SQLAlchemy. Please adjust the imports based on your setup.