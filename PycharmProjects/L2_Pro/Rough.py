# Declare array
#n = int(input("Enter number of students:"))
n = 4
names = ["Prashant","Pallavi","Dheeraj","Shivam"]
score = ["32", "36", "39","41", "40"]
#for i in range(0,n):
#    names.append(input("Enter Name:"))
#    score.append(input("Enter Score:"))

#print("---------------------")

#Display Output
#for i in range(0,n):
#    print(names[i]," ",score[i])

#print("---------------------")

small1 = small2 = min(score)
print("Small1:",small1)

for i in range(0,n,1):
    if score[i] < small2 and score[i] != small1:
            small2 = score[i]

finalStu = []
for i in range(0,n,1):
    if small2 == score[i]:
        finalStu.append(names[i])

finalStu.sort()
print(finalStu)
for i in range(0,len(finalStu),1):
    print(finalStu[i])



