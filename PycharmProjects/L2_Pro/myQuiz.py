def ques1():
    print("Where is Fort William located ?")
    print("a) Chennai")
    print("b) Goa")
    print("c) Kolkata")
    print("d) Mysore")
    answer = str(input("Answer:"))
    if answer == "c":
        ques2()
    else:
        print("Wrong Answer! Try Later")


def ques2():
    print("Name this Indian Tennis player who has turned Hollywood filmmaker?")
    print("a) Leander Paes")
    print("b) Mahesh Bhupathi")
    print("c) Vijay Amritraj")
    print("d) Ashok Amritraj")
    answer = str(input("Answer:"))
    if answer == "d":
        ques3()
    else:
        print("Wrong Answer! Try Later")

def ques3():
    print("Sishu is the literary work of which Indian author?")
    print("a) Vikram Seth")
    print("b) Jawaharlal Nehru")
    print("c) Rabindranath Tagore")
    print("d) Arundhati Roy")
    answer = str(input("Answer:"))
    if answer is "c":
        ques4()
    else:
        print("Wrong Answer! Try Later")

def ques4():
    print("Which of these Cities located in the state of Gujarat is famous for zari production?")
    print("a) Surat")
    print("b) Rajkot")
    print("c) Surendranagar")
    print("d) Ahmedabad")
    answer = str(input("Answer:"))
    if answer == "a":
        print("You have answered all the questions correctly ! Good Job :)")
    else:
        print("Wrong Answer! Try Later")


ques1()