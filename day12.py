# #FOR LOOP PROBLEMS
# #basic understanding
# #1. print numbers from 1 to 10 in one line
for i in range(1, 11):
    print(i, end=' ')
print()
# #2. print even numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end=' ')
# print()
# #3. print odd numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end=' ')
print()
# #4. print numbers divisible by 5 from 1 to 30 in one line
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end=' ')
print()
# #5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=' ')
print()
# #6. sum of numbers from 10 to 25 
for i in range(10, 26):
    sum = 0
    sum += i
    print(sum, end=' ')
print()

# #7. sum of numbers in any list
num=[9,6,7,4,7,8]
total = 0
for i in num:
    total += i
print(total)
#8. multiplication table of a number 
for i in range(1, 11):
    print(f"9 x {i} = {9*i}")
print()


#interview problems
#9. factorial 

#10. fibonacci 
#11. reverse a string
#12. count vowels in a string
# string="bindhu"
# for ch in string:
#     if ch in"aeiou":
#         print(ch,end=' ')
# print()
#13. count z's and y's in a string
string="zzyyyuvz"
for ch in string:
    if ch in "zy":
        print(ch,end=' ')
print()
#14. check whether a number is prime number or not 




#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
#print even numbers from 1 to 10
#print numbers divisible by both 5 and 7 from 1 to 500 

#interview problems
#count digits
#reverse a number
#palindrome number 
#palindrome string (without slicing, built in function)
#armstrong number
