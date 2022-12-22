import csv

#A. Structures de données : Airport
#implémentation de la class Airport :
class Airport:
    name : str
    code : str
    lat : float
    long : float
    def __init__(self) -> None : 
        return None

#B. Structures de données : Flight       
#implémentation de la class Flight 
class Flight:
    src_code : str
    dst_code : str
    duration : float
    def __init__(self) -> None :
       return None

#C. Structures de données : FlightMap
#implémentation de la class FlightMap :
class FlightMap:
    airports = []
    flights = []
    def __init__(self):
        return None

    def import_airports(self, csv_file : str) -> None :
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, code, lat, long = row
                airport = Airport(name, code, float(lat), float(long))
                self.airports[code] = airport
        return None
                
    def import_flights(self, csv_file : str) -> None :
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                src_code, dst_code, duration = row
                flight = Flight(src_code, dst_code, float(duration))
                if src_code not in self.flights:
                    self.flights[src_code] = []
                self.flights[src_code].append(flight) 
        return None

#D. Accès simples
    def airports(self, csv_file) -> list[Airport]:
        with open(csv_file) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'code', 'lat', 'long'])

    def flights(self, csv_file) -> list [Flight]:
        with open(csv_file) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['src_code', 'dst_code', 'duration']) 

#E. Recherches simple d'aéroport
    def airport_find(self, airport_code : str) -> Airport :
        for airport in self.airports:
            if airport_code == airport_code:
                return airport
            return None

#F Vol direct entre deux aéroports
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) :
        for flight in self.flights :
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
            return False


#G. Recherche des vols et aéroports accessibles à partir d'un aéroport donné
    def flights_where(self, airport_code : str) -> list[Flight]:
        return [flight for flight in self.flights if flight.src_code == airport_code 
        or flight.dst_code == airport_code]

    def airports_from(self, airport_code: str) -> list [Airport]:
        return 