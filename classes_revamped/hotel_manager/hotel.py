class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms
        
    def give_room(self):
        for individual_room in self.rooms:
            if individual_room.is_empty:
                individual_room.give_keys()
                return individual_room.number
        return "All rooms are full"
            
    def checkout(self, number):
        for individual_room in self.rooms:
            if individual_room.number == number:
                individual_room.exit_room()
                
                
    def earnings(self):
        count = 0
        for individual_room in self.rooms:
            if not individual_room.is_empty:
                count += 1
        return count * 100
                
    def __str__(self):
        return " ------ ".join([str(x) for x in self.rooms])
         