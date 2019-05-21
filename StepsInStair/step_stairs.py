# Given a stair with a number of steps and an array of possible movements, how many ways do we have of reaching the top


class Stair:

    def __init__(self, number_steps):
        self.steps = number_steps

    # Doesn't have to be list
    def num_ways(self, possible_steps: list, starting_point=0):
        # kill duplicates
        possible_steps = list(dict.fromkeys(possible_steps))
        
        # I don't like having an external variable, but it's the simplest way to count
        self.total_ways = 0
        self.count_ways(possible_steps, 0)
        self.partial_solutions = []

        return self.count_ways_performant(possible_steps, self.steps)

    def count_ways(self, possible_steps, starting_point):

        for x in possible_steps:
            new_position = starting_point + x
            
            #End of recursion
            if new_position == self.steps:
                self.total_ways = self.total_ways + 1
            
            #Trigger the recursion
            elif new_position < self.steps:
                self.count_ways(possible_steps,new_position)

    # we can save the partial solutions as this is a fibonacci. WIP
    def count_ways_performant(self, possible_steps, steps):

        if steps == 0:
            return 1

        # Here we will store the partial solutions so we don't compute them again
        partial_solutions = [None] * (steps + 1)
        partial_solutions[0] = 1

        for i in range(1,steps+1):
            total = 0
            for step in possible_steps:
                if step <= i:
                    total = total + partial_solutions[i - step]
            partial_solutions[i] = total 
        print(str(partial_solutions))
        return partial_solutions[steps]

