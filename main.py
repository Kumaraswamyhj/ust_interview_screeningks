# Python program to demonstrate main() function
from word_requency import frequency_word
from getdata import read_data

def main():
    filename = "inputdata\data.txt"
    inputdata = read_data(filename)
    result = frequency_word(inputdata)
    print(result)

if __name__=="__main__":
    main()