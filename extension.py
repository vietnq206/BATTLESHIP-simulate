import battleships as battle


fleet = battle.randomly_place_all_ships()

battle_fleet = [
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


while battle.are_unsunk_ships_left(fleet) == True:
    print("    0 1 2 3 4 5 6 7 8 9 ")
    print("------------------------")
    count = 0
    for i in battle_fleet:
        print(count,"|",i[0], i[1],i[2], i[3],i[4], i[5],i[6], i[7],i[8], i[9] )
        count +=1
    
    row,column = battle.main(fleet)
    ship_shit_name = ""

    for i in fleet.get_list_of_ship():
        if {(row,column)} == {(row,column)} & i.get_location_block_ship():
            ship_shit_name = i._ship_type()
            break

    if ship_shit_name == "":
        display = "*"
    elif ship_shit_name == "submarine":
        display = "S"
    elif ship_shit_name == "destroyer":
        display = "D"
    elif ship_shit_name == "cruiser":
        display = "C"
    elif ship_shit_name == "battleship":
        display = "B"

    battle_fleet[row][column] = display
    

print("GAME FINISH!!!!")

