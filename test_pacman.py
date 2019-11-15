import unittest
from pacman import Pacman

class TestPacman(unittest.TestCase):

    def setUp(self):
        pm1 = Pacman(2, 3, "NORTH")
        pm2 = Pacman(1, 2, "WEST")
        pm3 = Pacman(2, 1, "SOUTH")
        pm4 = Pacman(3, 2, "EAST")

        self.list = [pm1, pm2, pm3, pm4]
        pass

    def test_update(self):

        for pm in self.list:
            pm.update(-1)

        # Tests if pacman can turn left
        self.assertEqual(self.list[0].f, "WEST")
        self.assertEqual(self.list[1].f, "SOUTH")
        self.assertEqual(self.list[2].f, "EAST")
        self.assertEqual(self.list[3].f, "NORTH")

        for pm in self.list:
            pm.update(1)

        # Tests if pacman can turn right
        self.assertEqual(self.list[0].f, "NORTH")
        self.assertEqual(self.list[1].f, "WEST")
        self.assertEqual(self.list[2].f, "SOUTH")
        self.assertEqual(self.list[3].f, "EAST")

        for pm in self.list:
            pm.update(2)

        # Tests if update() can ignore invalid arguments
        self.assertEqual(self.list[0].f, "NORTH")
        self.assertEqual(self.list[1].f, "WEST")
        self.assertEqual(self.list[2].f, "SOUTH")
        self.assertEqual(self.list[3].f, "EAST")

    def test_move(self):

        for pm in self.list:
            pm.move()

        # Tests if pacman moves correctly
        self.assertEqual(self.list[0].x, 2)
        self.assertEqual(self.list[0].y, 4)
        self.assertEqual(self.list[1].x, 0)
        self.assertEqual(self.list[1].y, 2)
        self.assertEqual(self.list[2].x, 2)
        self.assertEqual(self.list[2].y, 0)
        self.assertEqual(self.list[3].x, 4)
        self.assertEqual(self.list[3].y, 2)

        for pm in self.list:
            pm.move()

        # Tests if pacman ignores moves correctly
        self.assertEqual(self.list[0].x, 2)
        self.assertEqual(self.list[0].y, 4)
        self.assertEqual(self.list[1].x, 0)
        self.assertEqual(self.list[1].y, 2)
        self.assertEqual(self.list[2].x, 2)
        self.assertEqual(self.list[2].y, 0)
        self.assertEqual(self.list[3].x, 4)
        self.assertEqual(self.list[3].y, 2)



if __name__ == "__main__":
    unittest.main()
