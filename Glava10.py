import json

file = "files/sigma.txt"
with open(file, 'r') as txt_file:
    for line in txt_file:
        print(line.rstrip())
        
with open(file, 'r') as txt_file:
    lines = txt_file.readlines()
print(lines)

message = "I love cats and dogs!"
message = message.replace('dog', 'cat')
print(message)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filename = "files/numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)
    
numbers1 = []
    
with open(filename) as f:  #можно использовать для сохраниния данных и использовании через .json-ы
    numbers1 = json.load(f)
print(numbers1)