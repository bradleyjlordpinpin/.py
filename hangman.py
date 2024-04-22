import time, random

fruit_list = ["apple", "banana", "orange", "mango", "grape", "pineapple", "watermelon", "kiwi", "papaya", "lemon", "lime", "pear", "peach", "plum", "apricot", "blueberry", "raspberry", "blackberry", "cherry", "strawberry", "avocado", "coconut", "dragonfruit", "guava", "kiwifruit", "mulberry", "pomegranate", "passionfruit", "fig"]
print("----------Welcome to Guess Game----------\nTopic: Fruit")

timer = 30 #timer
fruit = random.choice(fruit_list)
start_time = time.time()
time_sum = start_time + timer
print(fruit)
def run():
    max_guess = 3
    while max_guess != 0:
        guess = str(input("Enter your guess: "))
        if time.time() < time_sum:
            if guess.lower() == fruit:
                print("Your answer is correct!")
                break
            else:
                max_guess -= 1
                print("Wrong! You have ", max_guess, " chances left.")
                if max_guess == 0:
                    print("You lose! The answer is ",fruit)
                    break
                else:
                    continue
        else:
            print("Time's up! Sorry your guess was not recorded")


run()
        
        