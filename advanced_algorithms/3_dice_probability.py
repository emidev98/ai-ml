import random

class DiceProbability:

    def __init__(self):        
        self.number_of_rolls = int(input("How many times do you want to roll the dice? "))
        self.number_of_tries = int(input("How many times do you want to run the simulation? "))
        self.total_number_of_execturions = self.number_of_rolls * self.number_of_tries;

        self.roll_dices()

    def roll_dices(self):
        total_dice_rolls_results = [] 

        for _ in range(self.number_of_tries):
            dice_rolls_results = self.roll_dice()
            total_dice_rolls_results.append(dice_rolls_results)

        parsed_probabilities = self.parse_probabilities(total_dice_rolls_results) # key = (1,2,3,4,5,6) value = number of times
        self.print_result(parsed_probabilities)

    def roll_dice(self):
        dice_rolls_results = []
        
        for _ in range(self.number_of_rolls):
            roll = random.choice(range(1,7))
            dice_rolls_results.append(roll)

        return dice_rolls_results

    def parse_probabilities(self,total_rolls_results):
        total_results = {}

        for rolls_result in total_rolls_results:
            for roll_result in rolls_result:
                if total_results.get(roll_result) is None:
                    total_results[roll_result] = 1
                else:
                    total_results[roll_result] += 1
        
        return total_results

    def print_result(self,parsed_probabilities):
        for parsed_probability in parsed_probabilities.items(): # tuple 0 = dice face | tuple 1 = number of times
            print(f"The probability to roll {parsed_probability[0]} is {parsed_probability[1] / self.total_number_of_execturions}")

if __name__ == '__main__':
    DiceProbability()