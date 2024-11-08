class ComputerGuessingGame:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.tries = 0

    def guess(self):
        return (self.lower + self.upper) // 2

    def update_range(self, feedback):
        guess = self.guess()
        if feedback == "higher":
            self.lower = guess + 1
        elif feedback == "lower":
            self.upper = guess - 1
        self.tries += 1

    def play(self):
        print(f"Think of a number between {self.lower} and {self.upper} and I'll try to guess it.")
        input("Press Enter when you're ready...")
        
        while self.lower <= self.upper:
            guess = self.guess()
            print(f"My guess is {guess}.")
            feedback = input("Is it 'higher', 'lower', or 'correct'? ").strip().lower()
            
            if feedback == "correct":
                print(f"Yay! I guessed it in {self.tries + 1} tries.")
                break
            elif feedback in ["higher", "lower"]:
                self.update_range(feedback)
            else:
                print("Please respond with 'higher', 'lower', or 'correct'.")

if __name__ == "__main__":
    game = ComputerGuessingGame()
    game.play()
 
 