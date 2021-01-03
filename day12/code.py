"""
Advent of Code Problem 12

See Readme for details

"""
import math

class ship():
    """
    Represents ship with:
    - current heading (direction we are facing)
    - [x,y] position on a coordinate grid
    """

    # Turn Left verse Right multiplier
    turn_multiplier = {"L":-1,"R":1}

    # Degrees to heading conversions
    heading2degrees = {"N":0,"E":90,"S":180,"W":270,}
    degrees2heading = {0:"N",90:"E",180:"S",270:"W",
                    -90:"W",-180:"S",-270:"E",-360:"N"}

    def __init__(self, part, direction, waypoint, verbose=0):
        # Other than initial heading,
        # Assume starting positon of (0,0)
        self.part = part # 1 or 2
        self.heading = direction
        self.wp = waypoint  # Waypoint as [x,y]
        self.starting_pos = [0,0]
        self.x = 0
        self.y = 0
        self.verbose = verbose


    def move(self, direction, steps):
        """
        Moves the ship in a 2-D plane accordingly
        """

        # Part1 is a simple processing of the action
        if self.part == 1:
            # If direction is forward, update to be current heading:
            if direction == "F":
                direction = self.heading

            # Process action by updating ship's position    
            if direction == "N":
                self.y += steps
            elif direction == "S":
                self.y -= steps
            elif direction == "E":
                self.x += steps
            elif direction == "W":
                self.x -= steps
            else:
                print("ERROR: Unexpected direction in ship.move(), no action taken.")
        
        # Part2 requires us to repeated apply the waypoints position to our position
        if self.part == 2:
            for i in range(steps):
                self.x += self.wp[0]
                self.y += self.wp[1]


    def turn(self, direction, degrees):
        """
        (PART1 only) Turns ship:

        - "L": Right
        - "R": Right
        """

        # Get new heading in degrees
        # Needs to be positive value
        old_heading = self.heading  # Debugging only
        new_heading = (self.heading2degrees[self.heading] + (self.turn_multiplier[direction]*degrees)) % 360
        self.heading = self.degrees2heading[new_heading]
        # Debugging output
        if self.verbose >= 1:
            print(f"TURN {direction}{degrees} | old: {old_heading} | new: {self.degrees2heading[new_heading]}")

    

    def update_waypoint(self, action_type, steps):
        """(PART2) Processes a waypoint update"""

        if action_type in ["L","R"]: 
            # Rotates the point about the axis
            # NOTE: This is clockwise rotation. That is why signs are how they are
            angle = math.radians(steps * self.turn_multiplier[action_type])
            x_new = round(self.wp[0]*math.cos(angle) + self.wp[1]*math.sin(angle))
            y_new = round(self.wp[1]*math.cos(angle) - self.wp[0]*math.sin(angle))
            self.wp = [x_new,y_new]
        
        elif action_type in ["N","S","E","W"]: 
            if action_type == "N":
                self.wp[1] += steps
            elif action_type == "S":
                self.wp[1] -= steps
            elif action_type == "E":
                self.wp[0] += steps
            elif action_type == "W":
                self.wp[0] -= steps
        else: 
            print(f"ERROR: Unrecognized action '{action}', no action taken.")


    def process_action(self, action):
        """Processes an action and turns or moves the ship accordingly"""

        # Assuming action is of form (N|S|E|W|L|R|F)[0-9]{1,3}
        action_type = action[0]
        steps = int(action[1:])

        if self.verbose >= 1:
            print("="*50)
            print(f"Current position: [{self.x},{self.y}] | Action: {action} | Waypoint: {self.wp}")

        if self.part == 1:
            if action_type in ["L","R"]: 
                self.turn(action_type,steps)
            elif action_type in ["N","S","E","W","F"]: 
                self.move(action_type,steps)
            else: 
                print(f"ERROR: Unrecognized action '{action}', no action taken.")
        if self.part == 2:
            if action_type in ["F"]: 
                self.move(action_type,steps)
            elif action_type in ["N","S","E","W","R","L"]: 
                self.update_waypoint(action_type,steps)
            else: 
                print(f"ERROR: Unrecognized action '{action}', no action taken.")        

        if self.verbose >= 1:
            print(f"New position: [{self.x},{self.y}] | Waypoint: {self.wp}")

    def dist_traveled(self):
        """Calculates Manhatten Distance between starting position and current position"""

        # Since starting position was set to (0,0)
        # Manhatten distance is simply absolute some of x & y position
        m_dist = abs(self.x) + abs(self.y)
        print(f"Ship has moved Manhatten Distance: {m_dist}")


def read_input(filename, verbose=0):
    """
    Read in Input

    Requires:
    - file to be in current working directory
    """
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())
    return data


def part1(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    s = ship(1, "E", [0,0], verbose=verbose)
    for d in data:
        s.process_action(d)
    s.dist_traveled()
    

def part2(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)      
    s = ship(2, "E", [10,1], verbose=verbose)
    for d in data:
        s.process_action(d)
    s.dist_traveled()
    

def main(verbose=0):
    # part1(verbose=verbose)
    part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)