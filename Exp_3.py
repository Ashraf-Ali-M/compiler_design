def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def concatenate(s1, s2):
    return s1 + s2  

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def is_palindrome(s):
    return s == reverse_string(s)

def find_substring(s, sub):
    for i in range(string_length(s) - string_length(sub) + 1):
        if s[i:i + string_length(sub)] == sub:
            return i
    return -1

def compare_strings(s1, s2):
    if s1 == s2:
        return 0
    return 1 if s1 > s2 else -1

def count_char(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != ' ':
            result += ch
    return result

s1 = "hello"
s2 = "world"
test_string = "hello world"
test_substring = "world"

print("1. Length of string:", string_length(s1))  
print("2. Concatenation:", concatenate(s1, s2))  
print("3. Reverse string:", reverse_string(s1))  
print("4. Convert to uppercase:", to_upper(s1)) 
print("5. Convert to lowercase:", to_lower("HELLO"))  
print("6. Check palindrome:", is_palindrome("madam"))  
print("7. Find substring:", find_substring(test_string, test_substring))  
print("8. Compare strings:", compare_strings("abc", "abd"))  
print("9. Count occurrences of 'o':", count_char(test_string, 'o'))  
print("10. Remove spaces:", remove_spaces(test_string))  
