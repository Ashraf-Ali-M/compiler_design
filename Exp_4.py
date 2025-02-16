import re

def categorize_tokens(expression):
    keywords = {"if", "else", "while", "for", "return"}
    operators = {'+', '-', '*', '/', '=', '==', '!=', '>', '<', '>=', '<='}
    
    tokens = re.findall(r'\d+|\w+|[^\w\s]', expression)
    categorized = {"keywords": [], "identifiers": [], "operators": [], "numbers": [], "symbols": []}

    for token in tokens:
        if token in keywords:
            categorized["keywords"].append(token)
        elif token in operators:
            categorized["operators"].append(token)
        elif token.isdigit():
            categorized["numbers"].append(token)
        elif token.isidentifier():
            categorized["identifiers"].append(token)
        else:
            categorized["symbols"].append(token)
    
    return categorized

with open('sample2.txt','r') as file:
  for line in file:
    print(f"--> {line}\n")
    result = categorize_tokens(line)
    for key in result:
      print(f"{key} : {result[key]}")
    print('\n\n')
