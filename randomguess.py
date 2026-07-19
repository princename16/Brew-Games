import random
lap = 1
a = random.randint(1,1000)
b = -1
limit = 15

while b != a:
    print("What number do you want to guess? 1 - 1000")

    try:
        b = int(input(" "))
    except ValueError:
        print("WHY now i must")
        print("Running a lap!", lap + 1)
        continue
    limit -= 1

    if limit == 0:
        print("Too many guesses, you lose!! The answer is", a)
        break

    if b < a:
        print("Too low, try again —", limit, "more chances")
    elif b > a:
        print("Too big, try again —", limit, "more chances")
    else:
        print("You win!")
