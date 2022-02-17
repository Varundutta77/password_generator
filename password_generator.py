import string
import random

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
pas=int(input('Enter password length : '))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
print("".join(random.sample(s,pas)))
