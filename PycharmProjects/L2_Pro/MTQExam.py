import time
import os
score = 0


def scoreAdd():
    global score
    score += 1
    print("Score: ",score)


def scoreMinus():
    global score
    score -= 1
    print("Score: ",score)


def ques1():
    global score
    print("\nWhere is Fort William located ?")
    time.sleep(1)
    print("a) Chennai")
    print("b) Goa")
    print("c) Kolkata")
    print("d) Mysore")
    answer = str(input("Answer:"))
    if answer == "c":
        scoreAdd()
    else:
        print("Wrong Answer! Correct answer is c")
        scoreMinus()
    ques2()


def ques2():
    os.system("cls")
    global score
    print("Name this Indian Tennis player who has turned Hollywood filmmaker?")
    time.sleep(1)
    print("a) Leander Paes")
    print("b) Mahesh Bhupathi")
    print("c) Vijay Amritraj")
    print("d) Ashok Amritraj")
    answer = str(input("Answer:"))
    if answer == "d":
        scoreAdd()
    else:
        print("Wrong Answer! Correct answer is d")
        scoreMinus()
    ques3()


def ques3():
    os.system('cls')
    global score
    print("Sishu is the literary work of which Indian author?")
    time.sleep(1)
    print("a) Vikram Seth")
    print("b) Jawaharlal Nehru")
    print("c) Rabindranath Tagore")
    print("d) Arundhati Roy")
    answer = str(input("Answer:"))
    if answer is "c":
        scoreAdd()
    else:
        print("Wrong Answer! Correct answer is c")
        scoreMinus()
    ques4()


def ques4():
    os.system('cls')
    global score
    print("Which of these Cities located in the state of Gujarat is famous for zari production?")
    time.sleep(1)
    print("a) Surat")
    print("b) Rajkot")
    print("c) Surendranagar")
    print("d) Ahmedabad")
    answer = str(input("Answer:"))
    if answer == "a":
        scoreAdd()
    else:
        print("Wrong Answer! Correct answer is a")
        scoreMinus()


ques1()