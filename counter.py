#intro
print("-------------------------------")
print("| Text Counter by Derin Durak |")
print("-------------------------------")
import loader
print()
print()

#define the file
file_name = "example.txt"
f = open(file_name, "r")

#define content
content = f.read()

#define letter variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let_counter = 0

vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
vow_counter = 0

consonants = ["b", "c", "d","f", "g", "h", "j", "k", "l", "m", "n","p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N","P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
con_counter = 0

#define number variables
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numb_counter = 0

#define word count variables
word_deli = " " #change here to change delimeter
word_counter = 0

# define line variables
lines = content.split("\n")
line_counter = 0

#functions (operations) Note: you don't have to use functions
def liness():
    global line_counter
    for i in lines:
        if i:
            line_counter += 1

def letterss():
    global let_counter
    for i in content:
        if i in letters:
            let_counter += 1

def wordss():
    global word_counter
    for i in content:
        if i in word_deli:
            word_counter += 1
        
def numberss():
    global numb_counter
    for i in content:
        if i in numbers:
            numb_counter += 1

def vowelss():
    global vow_counter
    for i in content:
        if i in vowels:
            vow_counter +=1

def consonantss():
    global con_counter
    for i in content:
        if i in consonants:
            con_counter +=1

# MAIN CODE
liness()
letterss()
wordss()
numberss()
vowelss()
consonantss()

#adding line count to word count
word_counter += line_counter

#printing part  
message = "In {} there are {} letters ( {} consonants and {} vowels ); {} numbers; {} words and {} lines."
print(message.format(file_name,let_counter,con_counter,vow_counter,numb_counter,word_counter,line_counter))