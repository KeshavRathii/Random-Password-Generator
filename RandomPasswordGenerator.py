import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# list comprehension
password ="".join([random.choice(charValues) for i in range(pass_len)]) 

print("Your random password is:",password)