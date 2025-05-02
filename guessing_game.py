import random
while True:
#number = random.randint(1, 10)
#print("Guess a number between 1 and 10")
number = random.randint(1, 75)
print("Guess a number between 1 and 75")
guess = int(input())
if guess == number:
 print("You win!")
else:
 if guess < number;
        print("Tool low"
              elif guess > number;
              print("Tool high!")
print(f"Wrong! The number was {number}")
print("Play again? (y/n)")
    if input().lower() != 'y':
        break
        import time
start_time = time.time()
# (At the end)
print(f"Time taken: {time.time() - start_time:.2f}s")
