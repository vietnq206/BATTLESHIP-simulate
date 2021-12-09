import unittest

import battleships as battle


class MyTestCase(unittest.TestCase):

    Fleet = battle._Fleet()

    ship1 = battle.ship(0, 0, True, 4)
    ship2 = battle.ship(0, 2, True, 3)
    ship3 = battle.ship(0, 4, True, 3)
    ship4 = battle.ship(0, 6, True, 2)
    ship5 = battle.ship(0, 8, True, 2)
    ship6 = battle.ship(5, 0, True, 2)
    ship7 = battle.ship(5, 2, True, 1)
    ship8 = battle.ship(5, 4, True, 1)
    ship9 = battle.ship(5, 6, True, 1)
    ship10 = battle.ship(5, 8, True, 1)

    list_ship = [ship1,ship2,ship3,ship4,ship5,ship6,ship7,ship8,ship9,ship10]
    for i in list_ship:
        i.generate_set_block()
        Fleet.add_set_marked(i.get_location_block_ship())

    Fleet.set_list_of_ship(list_ship)


    def test_is_sunk(self):
        self.ship1.add_to_set_hits({(0,0)})
        self.assertEqual(battle.is_sunk(self.ship1), False)
        self.ship1.add_to_set_hits({(1,0),(2,0),(3,0)})
        self.assertEqual(battle.is_sunk(self.ship1),True)

    def test_ship_type(self):

        self.assertEqual(self.ship1._ship_type(), "battleship")
        self.assertEqual(self.ship2._ship_type(), "cruiser")
        self.assertEqual(self.ship4._ship_type(), "destroyer")
        self.assertEqual(self.ship7._ship_type(), "submarine")


    def test_is_open_sea(self):

        self.assertEqual(battle.is_open_sea({(9,4)},self.Fleet),False)
        self.assertEqual(battle.is_open_sea({(5,0)}, self.Fleet),True)

    def test_ok_to_place_ship_at(self):
        self.assertEqual(battle.ok_to_place_ship_at(7,2,True,3,self.Fleet),True)
        self.assertEqual(battle.ok_to_place_ship_at(0, 0, True, 4, self.Fleet),False)

    def test_check_if_hits(self):

        self.assertEqual(battle.check_if_hits(0,0,self.Fleet),True)
        self.assertEqual(battle.check_if_hits(4, 1, self.Fleet), False)
        self.assertEqual(battle.check_if_hits(5,8,self.Fleet),True)
    def test_hits(self):
        self.assertEqual(battle.hit(0,0,self.Fleet),0)
        self.assertEqual(battle.hit(1,4, self.Fleet), 2)
        self.assertEqual(battle.hit(5, 6, self.Fleet), 8)
    def test_are_unsunk_ships_left(self):
        self.assertEqual(battle.are_unsunk_ships_left(self.Fleet),True)
if __name__ == '__main__':
    unittest.main()
