import sqlite3

CONN = sqlite3.connect('trip.db')
CURSOR = CONN.cursor()