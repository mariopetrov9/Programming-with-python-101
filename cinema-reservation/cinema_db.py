import sqlite3

db = sqlite3.connect("cinema_reservation.db")
cursor = db.cursor()

create_movies_table = '''CREATE TABLE IF NOT EXISTS movies(
                    movie_id INTEGER PRIMARY KEY,
                    name VARCHAR(256) NOT NULL,
                    rating DOUBLE NOT NULL)'''

create_projections_table = '''CREATE TABLE IF NOT EXISTS projections(
                    projection_id INTEGER PRIMARY KEY,
                    movie_id INTEGER NOT NULL,
                    type VARCHAR(256) NOT NULL,
                    date DATE NOT NULL,
                    time TIME NOT NULL,
                    FOREIGN KEY(movie_id) REFERENCES movies(movie_id))'''

create_reservations_table = '''CREATE TABLE IF NOT EXISTS reservations(
                    reserve_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(256) NOT NULL,
                    projection_id INTEGER NOT NULL,
                    row INTEGER NOT NULL,
                    col INTEGER NOT NULL,
                    FOREIGN KEY (projection_id) REFERENCES projections(projection_id))'''

movies = [(1, "THe hunder games", 7.9),
          (2, "Wreck-it Ralph", 7.8),
          (3, "Her", 8.3)]

projections = [(1, 1, "3D", "2014-04-01", "19:10"),
               (2, 1, "2D", "2014-04-01", "19:00"),
               (3, 1, "4DX", "2014-04-02", "21:00"),
               (4, 3, "2D", "2014-04-05", "20:20"),
               (5, 2, "3D", "2014-04-02", "22:00"),
               (6, 2, "2D", "2014-04-02", "19:30")]

reservations = [("RADORADO", 1, 2, 1),
                ("RADORADO", 1, 3, 5),
                ("RADORADO", 1, 7, 8),
                ("IVO", 3, 1, 1),
                ("IVO", 3, 2, 2),
                ("MYSTERIOUS", 5, 2, 3),
                ("MYSTERIOUS", 5, 2, 4)]


cursor.execute(create_movies_table)
cursor.execute(create_projections_table)
cursor.execute(create_reservations_table)

db.commit()

cursor.executemany('''INSERT INTO movies(movie_id,name,rating)
                  VALUES (?, ?, ?)''', movies)

cursor.executemany('''INSERT INTO projections(projection_id,movie_id,type,date,time)
                  VALUES (?, ?, ?, ?, ?)''', projections)

cursor.executemany('''INSERT INTO reservations(reserve_id,username,projection_id,row,col)
                  VALUES (?, ?, ?, ?, ?)''', reservations)

db.commit()


