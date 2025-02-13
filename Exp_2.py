def count_vowel_consonant(file_name):
  vowel_count = 0
  consonant_count = 0
  vowels = 'aeiouAEIOU'
  consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
  with open(file_name,'r') as file:
    for line in file:
      for char in line:
        if char in vowels:
          vowel_count += 1
        elif char in consonants:
          consonant_count += 1
          
  print(f"vowels count : {vowel_count}")
  print(f"consonant count : {consonant_count}")
  
file = 'sample.txt'
count_vowel_consonant(file)