import re

for _ in range(int(input())): 
    for hex_code in re.findall(r"(?<=.)#[\dA-Fa-f]{3,6}", input()):
         print(hex_code) 
    
