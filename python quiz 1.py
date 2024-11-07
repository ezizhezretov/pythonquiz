def quiz():
    print("Welcome to my fun fact quiz, please type in your letter in Uppercase (ex. A)")
    score = 0

    print("What is the fastest animal in the world?")
    print("A: Horse")
    print("B: Peregrine Falcon")
    print("C: Cheetah")
    print("D: Lion")
    answer = input("Answer: ")
    if answer == "B":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    print("Which planet is known as the Red Planet?")
    print("A: Venus")
    print("B: Mars")
    print("C: Jupiter")
    print("D: Saturn")
    answer = input("Answer: ")
    if answer == "B":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    print("How many wheels does a normal car have?")
    print("A: 6")
    print("B: 2")
    print("C: 8")
    print("D: 7")
    answer = input("Answer: ")
    if answer == "C":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    print("What's the biggest ocean?")
    print("A: Atlantic Ocean")
    print("B: Indian Ocean")
    print("C: Southern Ocean")
    print("D: Pacific Ocean")
    answer = input("Answer: ")
    if answer == "D":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print("Your score is " + str(score) + "/4.")
    print("Thanks for playing")



quiz()