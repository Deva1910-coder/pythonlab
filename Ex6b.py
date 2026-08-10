from collections import deque

text = input("Enter a string: ")
cleaned = ""

for ch in text:
    if ch.isalnum():
        cleaned += ch.lower()

deq = deque(cleaned)
palindrome = True

while len(deq) > 1:
    if deq.popleft() != deq.pop():
        palindrome = False
        break

if palindrome:
    print("Palindrome.")
else:
    print("Not a palindrome.")
