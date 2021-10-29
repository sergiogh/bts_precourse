from hotel import Hotel
from room import Room
from guest import Guest

room_101 = Room(101)
room_101.give_keys()
room_102 = Room(102)
room_103 = Room(103)
print(room_101)
room_101.exit_room()
print(room_101)

my_hotel = Hotel([room_101, room_102, room_103])
room_for_customer1 = my_hotel.give_room()
print(my_hotel)
print("My hotel earnings", my_hotel.earnings())
room_for_customer2 = my_hotel.give_room()
print("My hotel earnings", my_hotel.earnings())
my_hotel.checkout(room_for_customer1)
my_hotel.checkout(room_for_customer2)