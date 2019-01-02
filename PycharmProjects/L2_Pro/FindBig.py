#Declare List
list = [6,6,6,6,6,6,6,6,6,5]
#Print List
print("Print the entire list",list)
#Find biggest Element in the list
big1 = max(list)
#print("Largest Element:",big1)
#Remove Largest Element
#list.remove(big1)
#print("Print the entire list",list)
#Now find the bigest number
#big2 = max(list)
#print("Biggest Number",big2)
#Add back the big1 to the list
#list.append(big1)
#print("Final List",list)
list.sort()
print(list)
print(len(list))
start = len(list)-1
for i in range(start,-1,-1):
    if list[i] == big1:
        print("In continue block, Index:",i,"Element",list[i])
        continue
    if list[i] != big1:
        print("In break block, index:",i,"Element",list[i])
        big1 = list[i]
        break
print("Second Biggest",big1)
