# we need to count how many people accomodate in flight
# we dont want to overbook flight. also we can use list for storing people name.
#max people 3 can go on flight
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity-len(self.passengers)
        
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print("Added ", person ,"to flight successfully.")
    else:
        print("No available seats for ",person)
"""
output
Added  Harry to flight successfully.
Added  Ron to flight successfully.
Added  Hermione to flight successfully.
No available seats for  Ginny
"""