#question 1
hours = int(input("enter your value: "))
hours = hours * 60
print(hours)

#question 2
decision = input("do you want to convert from hours to minutes (type 'yes' or 'no'): ")

time = int(input("input time to convert: "))

if decision == "yes": print(time * 60)
else: print(time/60)

#question 3

word = input("write a word: ")
size = len(word)
print("the word has ", size, "letters")