import random


class _Fleet:
    set_marked = set()
    hits = set()
    list_of_ship = list()

    def __init__(self):
        set_marked = set()
        hits = set()
        list_of_ship = list()

    def get_list_of_ship(self):
        return self.list_of_ship

    def set_list_of_ship(self,list):
        for i in list:
            self.get_list_of_ship().append(i)


    def get_hits(self):
        return self.hits

    def get_set_marked(self):
        return  self.set_marked

    def append_ship(self,ship):
        self.list_of_ship.append(ship)

    def add_set_marked(self,new_set):
        self.set_marked = self.set_marked | new_set
    def add_set_hits(self,hit):
        self.hits = self.hits | hit



def is_open_sea(set_loation,fleet):
    if set_loation & fleet.get_set_marked() != set():
        return True
    else:
        return False

def is_sunk(ship):
    if ship.get_location_block_ship() == ship.get_location_block_ship() & ship.get_hits():
        return  True
    else:
        return False

def ok_to_place_ship_at(row,column,horizontal,length,fleet):
    status = True
    if horizontal == True:
        if row + length - 1 <= 9:
            for i in range(row-1,row+length+1):
                if is_open_sea({(i,column-1),(i,column),(i,column+1)},fleet):
                    status = False
        else:
            status = False
    else:
        if column + length -1 <= 9 :
            for i in range(column - 1, column + length + 1):
                if is_open_sea({(row -1,i), (row,i), (row+1,i)},fleet):
                    status = False
        else:
            status = False

    return status

def place_ship_at(row,column,horizontal,length,fleet):
    if horizontal == True:
        for i in range(row, row + length):
            fleet.add_set_marked({(i, column)})
        s = ship(row,column,horizontal,length)
        s.generate_set_block()
        fleet.append_ship(s)
        s.print_artibute()
    else:
        for i in range(column, column +  length):
            fleet.add_set_marked({(row, i)})
        s = ship(row, column, horizontal, length)
        s.generate_set_block()
        fleet.append_ship(s)
        s.print_artibute()

def randomly_place_all_ships():
    fleet = _Fleet()
    lengh_of_ship = [4,3,3,2,2,2,1,1,1,1]

    while lengh_of_ship != []:
        length = lengh_of_ship[0]
        row = random.randrange(0,9)
        column = random.randrange(0,9)
        if {(row,column)} & fleet.get_set_marked() == {(row,column)}:
            pass
        elif ok_to_place_ship_at(row,column,True,length,fleet) == True:
            place_ship_at(row,column,True,length,fleet)
            lengh_of_ship.pop(0)


        elif ok_to_place_ship_at(row,column,False,length,fleet) == True:
            place_ship_at(row,column,False,length,fleet)
            lengh_of_ship.pop(0)


    return fleet



def print_set(self):
    for i in self.set_marked:
        print(i)


def check_if_hits(row,column,fleet):
    if {(row, column)} == {(row, column)} & fleet.get_set_marked():
        return True
    else:
        return False

def hit(row,column,fleet):
    _hit = {(row,column)}
    # print(_hit)
    ship_index = -1
    for i in fleet.get_list_of_ship():
        ship_index = ship_index + 1
        # print("check  ",ship_index)
        # print(i.get_location_block_ship())
        if _hit & i.get_location_block_ship() == _hit:
            # print("in")
            i.add_to_set_hits(_hit)
            break

    return ship_index

def are_unsunk_ships_left(fleet):
    if fleet.get_set_marked() == fleet.get_set_marked() & fleet.get_hits():
        return False
    else:
        return True


class ship:

    def __init__(self,row,column,horizontal,length):

        self.length = length
        self.row = row
        self.column = column
        self.horizontal = horizontal
        self.location_block_ship = set()
        self.set_hits = set()


    def get_length(self):
        return self.length
    def get_location_block_ship(self):
        return self.location_block_ship
    def get_hits(self):
        return self.set_hits
    def add_to_set_hits(self,hit):
        self.set_hits = self.set_hits | hit
    def set_column(self,column):
        self.column = column
    def set_horizontal(self,horizontal):
        self.horizontal = horizontal
    def generate_set_block(self):
        if self.horizontal == True:
            for i in range(self.row,self.row + self.length ):
                self.location_block_ship = self.location_block_ship |{(i,self.column)}
        else:
            for i in range(self.column,self.column + self.length):
                self.location_block_ship = self.location_block_ship |{(self.row,i)}


    def got_hit(self,row,column):
        if {(row,column)} in self.location_block_ship:
            self.set_hits = self.set_hits | {(row,column)}
            return True
        else:
            return False
    def _ship_type(self):
        if self.length == 1:
            self.ship_type = "submarine"
        elif self.length == 2:
            self.ship_type = "destroyer"
        elif self.length == 3:
            self.ship_type = "cruiser"
        elif self.length == 4:
            self.ship_type = "battleship"

        return self.ship_type

    def print_artibute(self):
        print("Ship type =", self._ship_type())
        print("row =",self.row,"  column ",self.column)
        print("horizontal =", self.horizontal)

def main(fleet):

    row = -1
    column = -1
    can_hit = False
    print("Enter the point you want to hit: ")

    while row not in range(0, 10) or column not in range(0, 10) or can_hit == False:
        can_hit = False
        print("Row and column should in range 0 -> 9. Please enter:")
        print("Please enter row :")
        row = int(input())
        print("Please enter column :")
        column = int(input())

        if {(row, column)} & fleet.get_hits() == {(row, column)}:
            print("The square has been hited, please choose another one! ")
        else:
            can_hit = True

    if {(row, column)} & fleet.get_set_marked() == {(row, column)}:
        ship_hit_index = hit(row, column, fleet)
        print(ship_hit_index)
        fleet.get_list_of_ship()[ship_hit_index].print_artibute()

    fleet.add_set_hits({(row,column)})
    return (row,column)



if __name__== "__main__":
    fleet = randomly_place_all_ships()
    while True:
        row,column = main(fleet)
        print("row and colkumn :", row, column)
        print("Hit of all :")
        print(fleet.get_hits())
        print("hit of Ship 0 :")
        print(fleet.get_list_of_ship()[0].get_hits())






