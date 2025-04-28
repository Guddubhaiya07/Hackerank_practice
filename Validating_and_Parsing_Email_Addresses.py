import email.utils
import re
n=int(input())
valid =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
for i in range(n):
    email_string = input()
    email_string_to_check = (email.utils.parseaddr(email_string))
    if re.search(valid, str(email_string_to_check[1])):
        print(email_string)
