# Declare array
#n = int(input("Enter number of students:"))
n = 5
names = ["Harry","Berry","Tina","Akriti","Harsh"]
score = ["37.21", "37.21", "37.2","41", "39"]
#for i in range(0,n):
#    names.append(input("Enter Name:"))
#    score.append(input("Enter Score:"))

#print("---------------------")

#Display Output
#for i in range(0,n):
#    print(names[i]," ",score[i])

#print("---------------------")

small = min(score)
print(small)
flag = score[0]
print(flag)
for i in range(1,n,1):
    if flag == small:
        continue
    if flag < small:
        if flag < score[i]:
            flag = score[i]

print(flag)
finalStu = []
for i in range(0,n,1):
    if flag == score[i]:
        finalStu.append(names[i])

finalStu.sort()
for i in range(0,len(finalStu),19):
    print(finalStu[i])



