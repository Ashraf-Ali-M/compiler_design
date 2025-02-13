def file_count(file_name):
  char_count = 0
  word_count = 0
  line_count = 0
  with open(file_name,'r') as file:
    for line in file:
      line_count += 1
      char_count += len(line)
      words = line.split()
      word_count += len(words)
      
  print(f"character count : {char_count}")
  print(f"word count : {word_count}")
  print(f"line count : {line_count}")
  
file = 'sample.txt'
file_count(file)