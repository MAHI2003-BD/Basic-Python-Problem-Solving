actual_price=20
guess_count = 0
guess_limit=5
while guess_count<guess_limit:
    guess=int(input('Guess the price:'))
    guess_count += 1
if guess == actual_price :
    print("you've won!")