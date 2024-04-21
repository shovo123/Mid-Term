class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self.show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()
        Star_Cinema().entry_hall(self)
    
    def _initialize_seats(self):
        seats = [['free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[self._hall_no] = seats
    
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
    
    def book_seats(self, id, seat_tuples):
        if id not in [show[0] for show in self.show_list]:
            print("Invalid show ID.")
            return
        
        seats = self._seats[self._hall_no]
        
        for row, col in seat_tuples:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Invalid seat ({row}, {col}).")
                continue
            
            if seats[row][col] == 'booked':
                print(f"Seat ({row}, {col}) is already booked.")
                continue
            
            seats[row][col] = 'booked'
        
        self._seats[self._hall_no] = seats
        print("Seats booked successfully!")
    
    def view_show_list(self):
        print("Show List:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
    
    def view_available_seats(self, id):
        if id not in [show[0] for show in self.show_list]:
            print("Invalid show ID.")
            return
        
        seats = self._seats[self._hall_no]
        
        print("Available seats:")
        for i in range(self._rows):
            for j in range(self._cols):
                if seats[i][j] == 'free':
                    print(f"Row: {i}, Col: {j}")
        print("End of available seats.")


def main():
    while True:
        print("\nWelcome to Star Cinema!")
        print("1. Add Hall")
        print("2. Add Show to Hall")
        print("3. Book Seats")
        print("4. View Show List")
        print("5. View Available Seats")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            hall_no = input("Enter hall number: ")
            hall = Hall(rows, cols, hall_no)
            print(f"Hall {hall_no} added successfully!")
        
        elif choice == '2':
            hall_no = input("Enter hall number: ")
            id = input("Enter show ID: ")
            movie_name = input("Enter movie name: ")
            time = input("Enter show time: ")
            
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    hall.entry_show(id, movie_name, time)
                    break
            else:
                print("Hall not found.")
        
        elif choice == '3':
            id = input("Enter show ID: ")
            hall_no = input("Enter hall number: ")
            row_col_str = input("Enter seat row and column (e.g., '1,2 2,3'): ")
            seat_tuples = [tuple(map(int, seat.split(','))) for seat in row_col_str.split()]
            
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    hall.book_seats(id, seat_tuples)
                    break
            else:
                print("Hall not found.")
        
        elif choice == '4':
            hall_no = input("Enter hall number: ")
            
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    hall.view_show_list()
                    break
            else:
                print("Hall not found.")
        
        elif choice == '5':
            id = input("Enter show ID: ")
            hall_no = input("Enter hall number: ")
            
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    hall.view_available_seats(id)
                    break
            else:
                print("Hall not found.")
        
        elif choice == '6':
            print("Thank you for using Star Cinema Booking System!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
