import sqlite3
import settings
from prettytable import PrettyTable


class DB:
    def __init__(self, db, cursor):
        self.db = db
        self.c = cursor

    def get_movie_name_from_id(self, movie_id):
        self.c.execute('''SELECT movies.name , movies.rating
                          FROM movies
                          WHERE movies.movie_id = ?''', (movie_id,))
        for row in self.c.fetchall():
            return row["name"], row["rating"]

    def get_movies(self):
        return self.c.execute('''SELECT movie_id, name, rating
                                 FROM movies
                                 ORDER BY rating DESC''')

    def get_movie_projections_from_id(self, movie_id):
        return self.c.execute('''SELECT projections.projection_id, projections.date, projections.time, projections.type
                                 FROM projections
                                 JOIN movies
                                 ON projections.movie_id = movies.movie_id
                                 WHERE movies.movie_id = ?
                                 ORDER BY projections.date''', (str(movie_id),))

    def get_movie_projections_from_id_and_date(self, movie_id, date):
        return self.c.execute('''SELECT projections.projection_id, projections.time, projections.type
                                 FROM projections
                                 JOIN movies
                                 ON projections.movie_id = movies.movie_id
                                 WHERE movies.movie_id = ? AND projections.date = ?
                                 ORDER BY projections.date''', (str(movie_id), str(date)))

    def get_free_seats_for_projection(self, chosen_proj_id):
        return self.c.execute('''SELECT COUNT(r.projection_id)
                                 FROM projections as p
                                 JOIN reservations as r
                                 ON p.projection_id = r.projection_id
                                 WHERE p.projection_id = ?''', (chosen_proj_id,))

    def get_rows_cols(self, proj_id):
        return self.c.execute('''SELECT row, col
                                 FROM Reservations
                                 WHERE projection_id = ?''', (proj_id, ))

    def finalize(self, final_data):
        self.c.executemany('''INSERT INTO reservations(username, projection_id, row, col)
                                 VALUES (?,?,?,?)''', final_data)
        self.db.commit()

    def cancel_reservation(self, name):
        self.c.execute('''DELETE
                          FROM reservations
                          WHERE reservations.username = ?''', (name,))
        self.db.commit()


class Logic:
    def __init__(self, db):
        self.db = db

    def generate_table(self, *args):
        movie_id = args[0][0]
        print(args[0][1])
        if args[0][1] is not None:
            date = args[0][1]
            table = PrettyTable(["projection_id", "time", "type"])
            for row in self.db.get_movie_projections_from_id_and_date(movie_id, date):
                table.add_row([row["projection_id"], row["time"], row["type"]])
            return table
        else:
            table = PrettyTable(["projection_id", "date", "time", "type"])
            for row in self.db.get_movie_projections_from_id(movie_id):
                table.add_row([row["projection_id"], row["date"], row["time"], row["type"]])
            return table

    def show_free_seats(self, chosen_movie_id):
        free_seats = ""
        list_proj_id = []
        counted_seats = []
        count = 0
        for row in self.db.get_movie_projections_from_id(chosen_movie_id):
            list_proj_id.append(row["projection_id"])
        for ids in list_proj_id:
            counted_seats.append(self.count_seats(ids))
        for row in self.db.get_movie_projections_from_id(chosen_movie_id):
            free_seats += "[{}] {} {} {} ------ {} seats available\n".format(row["projection_id"], row["date"], row["time"], row["type"], counted_seats[count])
            count += 1
        return free_seats

    def count_seats(self, p_id):
            number_of_seats = 0
            for row in self.db.get_free_seats_for_projection(p_id):
                number_of_seats = settings.MAX_SEATS_IN_CINEMA - row['COUNT(r.projection_id)']
            return number_of_seats

    def generate_cinema(self, proj_id):
        rows = settings.CINEMA_ROWS
        cols = settings.CINEMA_COLS
        db_data = self.db.get_rows_cols(proj_id)
        cinema = []

        row_headers = [" " if x == 0 else str(x) for x in range(rows + 1)]
        cinema.append(row_headers)

        for row in range(rows):
            cinema.append([str(row + 1) if col == 0 else "." for col in range(cols+1)])

        for row in db_data:
            cinema[row["row"]][row["col"]] = "X"

        return cinema

    def confirmed_seat(self, chosen_seat, proj_id):
        chosen_seat = chosen_seat.replace(")", "")
        chosen_seat = chosen_seat.replace("(", "")
        seat_coords = chosen_seat.split(",")
        row = int(seat_coords[0])
        col = int(seat_coords[1])
        len_cinema = len(self.generate_cinema(proj_id))
        if len_cinema < row or len_cinema < col:
            print(CLI.message_lol_no())
            return False
        elif self.generate_cinema(proj_id)[row][col] == "X":
            print(CLI.message_already_taken_seat())
            return False
        else:
            return True

    def finalize(self, list_Seats, client_name, proj_id):
        list_tuples = []
        for seat in list_Seats:
            seat = seat.replace("(", "")
            seat = seat.replace(")", "")
            seats = seat.split(',')
            row = int(seats[0])
            col = int(seats[1])
            list_tuples.append((client_name, proj_id, row, col))
        return self.db.finalize(list_tuples)


class CLI:

    @staticmethod
    def message_lol_no():
        return "LoL NO.."

    @staticmethod
    def message_already_taken_seat():
        return "This seat is already taken!!"

    @staticmethod
    def message_show_movies():
        return "Currents movies: \n"

    def __init__(self, db, logic):
        self.db = db
        self.reserved_tickets = 1
        self.tickets_seat = []
        self.logic = logic
        self.__active = True
        self.commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "make_reservation": self.make_reservation,
            "exit": self.exit,
            "help": self.help,
            "cancel_reservation": self.cancel_reservation,
        }

    def cancel_reservation(self, *args):
        name = args[0]
        self.db.cancel_reservation(name)
        return "Reservation cancelled!"

    def help(self, *args):
        com = "Availiable commands:\n"
        for command in self.commands:
            if command != "help":
                com += command + "\n"
        return com

    def exit(self, *args):
        self.__active = False
        return "BYE BYE"

    def start(self):
        while self.__active is True:
            command = None
            date = None
            requested_id = None

            user_input = input("Enter a command: ")
            commands = user_input.split()
            command = commands[0]
            try:
                requested_id = commands[1]
                date = commands[2]
                print(self.commands[command](requested_id, date))
            except IndexError:
                print(self.commands[command](requested_id, date))

    def print_map(self, proj_id):
        current_cinema_map = ""
        for row in self.logic.generate_cinema(proj_id):
            for col in row:
                current_cinema_map += col + " "
            current_cinema_map += "\n"
        return current_cinema_map

    def give_up_input(self, user_input):
        if user_input == "give_up":
            self.tickets_seat = []
            self.reserved_tickets = 1
            return False
        return True

    def enter_client_name(self):
        client_name = input("Step 1 (User):Choose name> ")
        return client_name

    def enter_number_tickets(self):
        chosen_number_tickets = int(input("Step 2 (user): Choose number of tickets> "))
        return chosen_number_tickets

    def enter_chosen_movie_id(self):
        chosen_movie_id = input("Step 2 (Movie): Choose a movie> ")
        return chosen_movie_id

    def enter_proj_id(self):
        proj_id = int(input("Step 3 (Projection): Choose a projection> "))
        return proj_id

    def enter_chosen_seat(self, proj_id):
        chosen_seat = input("Step 4 (Seats):Choose seat {}> ".format(self.reserved_tickets))
        if (self.logic.confirmed_seat(chosen_seat, proj_id)):
            self.tickets_seat.append(chosen_seat)
            self.reserved_tickets += 1
        return chosen_seat

    def enter_finalize(self, client_name, proj_id):
        finalize = input("Step 5 :(Confirm - type 'finalize') > ")
        if finalize == 'finalize':
            return self.logic.finalize(self.tickets_seat, client_name, proj_id)
        return finalize

    def make_reservation(self, *args):
        client_name = self.enter_client_name()
        if not self.give_up_input(client_name):
            return
        chosen_number_tickets = self.enter_number_tickets()
        if not self.give_up_input(chosen_number_tickets):
            return
        print(self.show_movies())
        chosen_movie_id = self.enter_chosen_movie_id()
        if not self.give_up_input(chosen_movie_id):
            return
        print(self.logic.show_free_seats(chosen_movie_id))
        proj_id = self.enter_proj_id()
        if not self.give_up_input(proj_id):
            return
        print(self.print_map(proj_id))
        while self.reserved_tickets <= chosen_number_tickets:
            chosen_seat = self.enter_chosen_seat(proj_id)
            if not self.give_up_input(chosen_seat):
                return
        print(self.message_current_reserv(chosen_movie_id,))
        finalize = self.enter_finalize(client_name, proj_id)
        if not self.give_up_input(finalize):
            return

    def message_current_reserv(self, m_id):
        m_name = self.db.get_movie_name_from_id(m_id)
        seats = self.tickets_seat
        for row in self.db.get_movie_projections_from_id(m_id):
            date_time = "{} {} ({})".format(row['date'], row['time'], row['type'])
        return "This is your reservation\nMovie: {}\nDate and Time: {}\nSeats: {}".format(m_name, date_time, seats)

    def show_movie_projections(self, *args):
        movie_id = args[0][0]
        print(self.message_get_name_from_id(movie_id))
        return self.logic.generate_table(args)

    def message_get_name_from_id(self, movie_id):
        return "Projections for movie '{}'".\
                format(self.db.get_movie_name_from_id(movie_id))

    def show_movies(self, *args):
        print(self.message_show_movies())
        table = PrettyTable(["movie_id", "name", "rating"])
        for row in self.db.get_movies():
            table.add_row([row["movie_id"], row["name"], row["rating"]])
        return table


def main():
    db = sqlite3.connect("cinema_reservation.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    db = DB(db, cursor)
    logic = Logic(db)
    cli = CLI(db, logic)
    cli.start()


if __name__ == '__main__':
    main()
