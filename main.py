import time

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle_plate = None
        self.start_time = None

    def park_vehicle(self, vehicle_plate):
        if not self.is_occupied:
            self.is_occupied = True
            self.vehicle_plate = vehicle_plate
            self.start_time = time.time()
            print(f"Vehicle {vehicle_plate} parked in spot {self.spot_id}.")
        else:
            print(f"Spot {self.spot_id} is already occupied.")

    def remove_vehicle(self):
        if self.is_occupied:
            end_time = time.time()
            duration = end_time - self.start_time
            fee = self.calculate_fee(duration)
            print(f"Vehicle {self.vehicle_plate} removed from spot {self.spot_id}. Duration: {duration:.2f} seconds. Fee: ${fee:.2f}")
            self.is_occupied = False
            self.vehicle_plate = None
            self.start_time = None
        else:
            print(f"Spot {self.spot_id} is already empty.")

    def calculate_fee(self, duration):
        # Assuming $0.01 per second for simplicity
        return duration * 0.01

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.spots = [ParkingSpot(i+1) for i in range(total_spots)]

    def display_status(self):
        print("\nParking Lot Status:")
        for spot in self.spots:
            status = "Occupied" if spot.is_occupied else "Available"
            print(f"Spot {spot.spot_id}: {status}")

    def park_vehicle(self, vehicle_plate):
        for spot in self.spots:
            if not spot.is_occupied:
                spot.park_vehicle(vehicle_plate)
                return
        print("Parking lot is full. No available spots.")

    def remove_vehicle(self, vehicle_plate):
        for spot in self.spots:
            if spot.is_occupied and spot.vehicle_plate == vehicle_plate:
                spot.remove_vehicle()
                return
        print(f"Vehicle {vehicle_plate} not found in the parking lot.")

    def find_vehicle(self, vehicle_plate):
        for spot in self.spots:
            if spot.is_occupied and spot.vehicle_plate == vehicle_plate:
                print(f"Vehicle {vehicle_plate} is parked in spot {spot.spot_id}.")
                return
        print(f"Vehicle {vehicle_plate} not found in the parking lot.")

if __name__ == "__main__":
    parking_lot = ParkingLot(total_spots=5)

    parking_lot.park_vehicle("ABC123")
    parking_lot.park_vehicle("XYZ789")
    parking_lot.park_vehicle("LMN456")

    parking_lot.display_status()

    parking_lot.remove_vehicle("XYZ789")

    parking_lot.display_status()

    parking_lot.park_vehicle("DEF456")
    parking_lot.park_vehicle("GHI789")
    parking_lot.park_vehicle("JKL012")

    parking_lot.display_status()

    parking_lot.find_vehicle("LMN456")
    parking_lot.find_vehicle("XYZ789")