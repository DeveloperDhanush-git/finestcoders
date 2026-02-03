import re

def process_string(s):
    result_parts = []
    matches = re.findall(r'(\d+)\{(.*?)\}', s)
    
    for num, content in matches:
        num = int(num)
        if len(content) >= 1: 
            result_parts.append(content * num)
        # else: 
        #     result_parts.append(f"{num}{{{content * num}}}")
    
    return "".join(result_parts)

user_input = input("Enter the string: ")
output = process_string(user_input)
print("Output:", output)