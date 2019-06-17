import unittest

from mars_rover import Rover, Direction, Move, Turn


class Mars(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # This is the landscape, being 0,0 the top left position, and being 0 a place without obstacles. Both are 0 based
    landscape = ((0, 0, 0, 1, 0, 0),
                 (0, 0, 0, 0, 0, 0),
                 (0, 1, 0, 1, 0, 0),
                 (0, 0, 0, 0, 1, 1),
                 (0, 0, 1, 0, 1, 0),
                 (0, 0, 0, 1, 0, 0))

    def test_can_init_with_given_values(self):
        mars = Rover(self.landscape, (0, 0), Direction.N)
        self.assertTrue(mars.is_direction(Direction.N))
        self.assertTrue(mars.is_position((0, 0)))

    def test_position_has_obstacles(self):
        mars = Rover(self.landscape, (0, 0), Direction.N)
        self.assertTrue(mars.can_move((4, 0)))
        self.assertFalse(mars.can_move((0, 3)))

    def test_cant_move_outside_boundaries(self):
        mars = Rover(self.landscape, (0, 0), Direction.N)
        self.assertFalse(mars.can_move((-4, 0)))
        self.assertFalse(mars.can_move((0, 12)))
        self.assertFalse(mars.can_move((11, 3)))
        self.assertFalse(mars.can_move((4, -2)))

    def test_turn_left(self):
        mars = Rover(self.landscape, (0, 0), Direction.N)
        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.W))
        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.S))
        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.E))
        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.N))

    def test_turn_right(self):
        mars = Rover(self.landscape, (0, 0), Direction.N)
        mars.turn_right()
        self.assertTrue(mars.is_direction(Direction.E))
        mars.turn_right()
        self.assertTrue(mars.is_direction(Direction.S))
        mars.turn_right()
        self.assertTrue(mars.is_direction(Direction.W))
        mars.turn_right()
        self.assertTrue(mars.is_direction(Direction.N))

    def test_move_forward_changes_position(self):
        mars = Rover(self.landscape, (0, 0), Direction.E)
        self.assertTrue(mars.move_forward())
        self.assertTrue(mars.is_position((0, 1)))
        self.assertTrue(mars.move_forward())
        self.assertTrue(mars.is_position((0, 2)))

    def test_move_backwards_changes_position(self):
        mars = Rover(self.landscape, (0, 2), Direction.E)
        self.assertTrue(mars.move_backwards())
        self.assertTrue(mars.is_position((0, 1)))
        self.assertTrue(mars.move_backwards())
        self.assertTrue(mars.is_position((0, 0)))

    def test_move_stops_on_edge_negative(self):
        mars = Rover(self.landscape, (0, 0), Direction.E)
        self.assertFalse(mars.move_backwards())
        self.assertTrue(mars.is_position((0, 0)))

        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.N))
        self.assertFalse(mars.move_forward())
        self.assertTrue(mars.is_position((0, 0)))

    def test_move_stops_on_edge_overflow(self):
        mars = Rover(self.landscape, (5, 5), Direction.E)
        self.assertFalse(mars.move_forward())
        self.assertTrue(mars.is_position((5, 5)))

        mars.turn_left()
        self.assertTrue(mars.is_direction(Direction.N))
        self.assertFalse(mars.move_backwards())
        self.assertTrue(mars.is_position((5, 5)))

    def test_move_stops_on_obstacle(self):
        mars = Rover(self.landscape, (1, 3), Direction.N)
        self.assertFalse(mars.move_forward())
        self.assertTrue(mars.is_position((1, 3)))
        self.assertFalse(mars.move_backwards())
        self.assertTrue(mars.is_position((1, 3)))

    def test_little_journey(self):
        landscape = ((0, 0, 0, 1, 0, 0),
                     (0, 1, 0, 0, 0, 0),
                     (0, 0, 0, 1, 0, 0),
                     (0, 0, 0, 0, 0, 1),
                     (0, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0))

        mars = Rover(landscape, (0, 0), Direction.E)

        # We move two to the right, but the next one finds an obstacle
        self.assertTrue(mars.move_forward())
        self.assertTrue(mars.move_forward())
        self.assertFalse(mars.move_forward())
        
        self.assertTrue(mars.is_direction(Direction.E))
        self.assertTrue(mars.is_position((0,2)))

        # We turn to the South and move three spaces, the next is an obstacle
        mars.turn_right()
        self.assertTrue(mars.move_forward())
        self.assertTrue(mars.move_forward())
        self.assertTrue(mars.move_forward())
        self.assertFalse(mars.move_forward())

        self.assertTrue(mars.is_direction(Direction.S))
        self.assertTrue(mars.is_position((3,2)))

        # We turn to the West and move backwards two spaces, the next is an obstacle
        mars.turn_right()
        self.assertTrue(mars.move_backwards())
        self.assertTrue(mars.move_backwards())
        self.assertFalse(mars.move_backwards())

        self.assertTrue(mars.is_direction(Direction.W))
        self.assertTrue(mars.is_position((3,4)))

    def test_command_only_moves_till_it_stops(self):
        landscape = ((0, 0, 0, 1, 0, 0),
                     (0, 1, 0, 0, 0, 0),
                     (0, 0, 0, 1, 0, 0),
                     (0, 0, 0, 0, 0, 1),
                     (0, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0))

        mars = Rover(landscape, (0, 0), Direction.E)

        # We move two to the right, but the next one finds an obstacle
        mars.command("F-F-F")
       
        self.assertTrue(mars.is_direction(Direction.E))
        self.assertTrue(mars.is_position((0,2)))

    def test_command_little_journey(self):
        landscape = ((0, 0, 0, 1, 0, 0),
                     (0, 1, 0, 0, 0, 0),
                     (0, 0, 0, 1, 0, 0),
                     (0, 0, 0, 0, 0, 1),
                     (0, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0))

        mars = Rover(landscape, (0, 0), Direction.E)

        # We move two to the right, but the next one finds an obstacle
        mars.command("F-F-F")
             
        self.assertTrue(mars.is_direction(Direction.E))
        self.assertTrue(mars.is_position((0,2)))

        # We turn to the South and move three spaces, the next is an obstacle
        mars.command("R-F-F-F-F")

        self.assertTrue(mars.is_direction(Direction.S))
        self.assertTrue(mars.is_position((3,2)))

        # We turn to the West and move backwards two spaces, the next is an obstacle
        mars.command("R-B-B-B")

        self.assertTrue(mars.is_direction(Direction.W))
        self.assertTrue(mars.is_position((3,4)))

