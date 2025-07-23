import random

class RandomNumber:
    def __init__(self):
        self.user = 0
        self.random_number = 0
        self.user2 = 0
        self.total_attempts = 0  # Counter for total attempts
        self.correct_attempts = 0  # Counter for correct attempts
        self.percentage = 0

    def choice(self):
        user_input = input("Enter a number between 1 to 10: or stop to game :")
        if user_input.lower() == 'stop':
            print("Game stopped.")
            print(f"Total attempts: {self.total_attempts}, Correct attempts: {self.correct_attempts}")
            print(f"game ratio : {(self.correct_attempts / self.total_attempts)*100} %")
            return None

        try:
            self.user = int(user_input)
            if 1 <= self.user <= 10:
                self.random()
            else:
                print("Please enter a number between 1 and 10.")
                self.choice()
        except ValueError:
            print("Invalid input. Please enter a number or type 'stop'.")
            self.choice()

    def random(self):
        self.random_number = random.randint(1, 100)
        print("Random number generated:", self.random_number)
        self.result()

    def result(self):
        try:
            if self.random_number > 50:
                self.user2 = int(input(f"Guess the result {self.random_number} - {self.user}: "))  # Convert guess to integer
            else:
                self.user2 = int(input(f"Guess the result {self.random_number} + {self.user}: "))  # Convert guess to integer

            self.total_attempts += 1
            self.declare()
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.result()

    def declare(self):
        if 0 <= self.random_number <= 50:
            if self.user2 == self.random_number + self.user:
                print("You won!")
                self.correct_attempts += 1
            else:
                print("You lost.")
        elif 51 <= self.random_number <= 100:
            if self.user2 == self.random_number - self.user:
                print("You won!")
                self.correct_attempts += 1
            else:
                print("You lost.")
        else:
            print("Something went wrong.")
        self.choice()  # Restart the game

    def attempts(self):
        return self.total_attempts, self.correct_attempts

    def ratio(self):
        return (self.correct_attempts / self.total_attempts)*100

choice_info = RandomNumber()
choice_info.choice()


