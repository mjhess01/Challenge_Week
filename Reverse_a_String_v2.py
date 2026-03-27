def reverse_string(string):
    for i in string[::-1]:
        print(i, end='')

string = input("Type a string: ")
reverse_string(string)