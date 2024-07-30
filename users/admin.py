from month_4.lesson_4.file_manager import airplane_manager, flight_manager, airport_manager
from month_4.lesson_4.users.logs import log_decorator


class Airplane:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity


@log_decorator
def create_plane():
    try:
        plane_id = int(input("Enter the plane ID:"))
        plane_name = input("Enter the plane name: ")
        plane_capacity = int(input("Enter the plane capacity: "))

        plane = Airplane(plane_id, plane_name, plane_capacity)
        airplane_manager.add_data(plane.__dict__)
        print(f"Plane {plane_name} created successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_planes():
    try:
        planes = airplane_manager.read()
        if planes:
            print("Planes:")
            for plane in planes:
                print(f"ID: {plane['id']},\nName: {plane['name']},\nCapacity: {plane['capacity']}\n")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def edit_plane():
    try:
        plane_id = int(input("Enter the plane ID to edit: "))
        planes = airplane_manager.read()
        if planes:
            for plane in planes:
                if plane['id'] == plane_id:
                    plane['name'] = input("Enter the new plane name: ")
                    plane['capacity'] = int(input("Enter the new plane capacity: "))
                    airplane_manager.write(planes)
                    print(f"Plane with ID {plane_id} has been updated successfully.")
                    return True
        else:
            print("No planes found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_plane():
    try:
        plane_id = int(input("Enter the plane ID to delete: "))
        planes = airplane_manager.read()
        if planes:
            for plane in planes:
                if plane['id'] == plane_id:
                    planes.remove(plane)
                    airplane_manager.write(planes)
                    print(f"Plane with ID {plane_id} has been deleted successfully.")
                    return True
        else:
            print("No planes found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class Airport:
    def __init__(self, name, country):
        self.name = name
        self.country = country


def create_airport():
    try:
        airport_name = input("Enter the airport name: ")
        airport_country = input("Enter the airport country: ")

        airport = Airport(airport_name, airport_country)
        airport_manager.add_data(airport.__dict__)
        print(f"Airport {airport_name} created successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_airports():
    try:
        airports = airport_manager.read()
        if airports:
            print("Airports:")
            for airport in airports:
                print(
                    f"Name: {airport['name']},\nCountry: {airport['country']},\n")
        else:
            print("No airports found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def edit_airport():
    try:
        airport_name = input("Enter the airport name to edit: ")
        airports = airport_manager.read()
        if airports:
            for airport in airports:
                if airport['name'] == airport_name:
                    airport['name'] = input("Enter the new airport name: ")
                    airport['country'] = input("Enter the new airport country: ")
                    airport_manager.write(airports)
                    print(f"Airport {airport_name} has been updated successfully.")
                    return True
        else:
            print("No airports found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_airport():
    try:
        airport_name = input("Enter the airport name to delete: ")
        airports = airport_manager.read()
        if airports:
            for airport in airports:
                if airport['name'] == airport_name:
                    airports.remove(airport)
                    airport_manager.write(airports)
                    print(f"Airport {airport_name} has been deleted successfully.")
                    return True
        else:
            print("No airports found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class Flight:
    def __init__(self, plane, from_airport, to_airport, flight_time, landing_time, tickets, price):
        self.plane = plane
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.flight_time = flight_time
        self.landing_time = landing_time
        self.tickets = tickets
        self.price = price


def check_tickets(ticket):
    planes = airplane_manager.read()
    for plane in planes:
        if plane["capacity"] < ticket:
            print(f"There are not enough tickets for the selected flight. Number of tickets on the selected flight:"
                  f"{plane["capacity"]}")
        return False
    else:
        return True


@log_decorator
def create_flight():
    global from_airports, to_airports
    try:
        planes = airplane_manager.read()
        airports = airport_manager.read()

        if planes and airports:
            plane_id = int(input("Enter the plane ID: "))
            from_airport_name = input("Enter the name of the country: ").capitalize().strip()
            if from_airport_name == "exit":
                return False
            else:

                to_airport_name = input("Enter the name of the country: ").capitalize().strip()
            flight_time = input("Enter the flight time (HH:MM): ")
            landing_time = input("Enter the landing time (HH:MM): ")
            tickets = int(input("Enter the tickets: "))
            check_tickets(tickets)
            price = float(input("Enter the price per ticket: "))
            for plane in planes:
                if plane['id'] == plane_id:
                    for airport in airports:
                        if airport['country'] == from_airport_name:
                            from_airports = airport
                        if airport['country'] == to_airport_name:
                            to_airports = airport
                    flight = Flight(plane, from_airports, to_airports, flight_time, landing_time, tickets, price)
                    flight_manager.add_data(flight.__dict__)
                    print("Flight created successfully.")
                    return True
        else:
            print("No planes or airports found.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_flights():
    try:
        flights = flight_manager.read()
        if flights:
            print("Flights:")
            for flight in flights:
                print(
                    f"Plane: {flight['plane']['name']},\nFrom: {flight['from_airport']['country']},\n"
                    f"To: {flight['to_airport']['country']},\nFlight Time: {flight['flight_time']},\n"
                    f"Landing Time: {flight['landing_time']},\nTickets: {flight['tickets']},\n"
                    f"Price per ticket: {flight['price']}\n")
        else:
            print("No flights found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
