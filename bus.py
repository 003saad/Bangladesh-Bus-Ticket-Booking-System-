class Bus:
    def __init__(self,number,route,total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    def availabble_seats(self):
        return self.total_seats - self.booked_seats
    def book_seat(self):
        if self.availabble_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self,name,phone,bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
        def __init__(self):
            self.username = "admin"
            self.password = "12345"
        def login(self,username,password):
            if username == self.username and password == self.password:
                return True
            return False


class Bus_Managing:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()
        self.log_in_status = False
    def add_bus(self,number,route,seats):
        if self.log_in_status:
            self.buses.append(Bus(number,route,seats))
            print("Bus added successfully.")
        else:   
            print("Please log in to add a bus.")
    def find_bus(self,number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None
    def book_ticket(self,bus_number,name,phone):
        bus = self.find_bus(bus_number)
        if bus:
            if bus.book_seat():
                self.passengers.append(Passenger(name,phone,bus))
                print("Ticket booked successfully.")
            else:
                print("No seats available.")
        else:
            print("Bus not found.")
    def show_buses(self):
        if self.buses:
            print("Available buses:")
            for bus in self.buses:
                print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.availabble_seats()}")
        else:
            print("No buses available.")
    

def main():
    app_name = Bus_Managing()

    while True:
        print("\n_____Bus Ticket Booking System_____")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if app_name.admin.login(username,password):
                app_name.log_in_status = True
                print("\nLogin successful.")
                while app_name.log_in_status:
                    print("\n_____Admin Menu_____")
                    print("1. Add Bus")
                    print("2. View Buses")
                    print("3. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        number = input("Enter bus number: ")
                        route = input("Enter bus route: ")
                        seats = int(input("Enter total seats: "))
                        
                        if seats>0:
                            app_name.add_bus(number, route, seats)
                        else:
                            print("Invalid number of seats.")
                    elif admin_choice == '2':
                        app_name.show_buses()
                    elif admin_choice == '3':
                        app_name.log_in_status = False
                        print("Logged out successfully.")
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid credentials.")
            
        elif choice == '2':
            bus_number = input("Enter bus number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")

            app_name.book_ticket(bus_number, name, phone)
        
        elif choice == '3':
            app_name.show_buses()

        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
        



    
