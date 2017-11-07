'''
How to read and write a file
'''
fw = open('sample.txt', 'w')

fw.write('Wrinting in my file\n')
fw.write('I like candies\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()