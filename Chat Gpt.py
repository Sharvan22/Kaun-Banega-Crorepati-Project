#1st question
from itertools import count

a=int(input("Enter the number:"))
b=int(input("Enter the number"))
print(f"The sum of {a} and {b} is:",a+b)
print(f"The difference of {a} and {b} is:",a-b)
print(f"The product of {a} and {b} is:",a*b)
print(f"The quotient of {a} and {b} is:",a//b)
#2nd question
#A
n = int(input("Enter the number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Your number is not a prime number")
            break
    else:
        print("Your number is a prime number")
#B
def fib(n):
 a=0
 b=1
 if n==0:
     print(a)
 else:
     print(a)
     print(b)
     for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c)
fib(3)
# Ans 3 Factorial of given number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))
# b part
def is_palindrome(s):
   s = s.lower().replace(" ", "").replace(",", "").replace("'", "")  # Normalize input
   return s == s[::-1]
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
#Ans 4 A

l = ["Rook", "Knight", "Bishop", "Pawn", "King"]
largest = l[0]
smallest =l[0]

for word in l:
    if len(word) > len(largest):
        largest = word
    if len(word) < len(smallest):
        smallest = word
print("The largest piece by length is:", largest)
print("The smallest piece by length is:", smallest)

#4B
list1=["red","yellow","pink","blue"]
list2=["moksh","shubham","dev","vedic"]
list1.sort()
list2.sort()
print(list1)
print(list2)
list3= list1 + list2
print(list3)
#Ans 5
def word_frequency(sentence):
    words = sentence.split()  # Split sentence into words
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1  # Increment count
    return frequency

# Test the function
sentence = "hello world hello"
print(word_frequency(sentence))
#5B
def invert_dict(original_dict):
    inverted_dict = {v: k for k, v in original_dict.items()}
    return inverted_dict

original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)
#6A
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

try:
   if a % b==1:
       print("The remainder is 1")
   else :
       if a % b==0:
           print("The remainder is 0")
except:
    raise IndexError("Your remainder is more than 0 and 1")
#6B
def average(g):
    try:
        if len(g) == 0:  # Check if the list is empty
            return "List is empty. Cannot calculate the average!"

        avg = sum(g) / len(g)  # Calculate the average
        return avg  # Return the calculated average

    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

# Example usage
g = [7, 8, 9, 5, 3, 6]
print(average(g))  # Outputs: 6.333333333333333















