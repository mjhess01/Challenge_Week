def reverse_string(string):
    return(string[::-1])


string = input("Type a string: ").lower()
string = string.replace(" ", "")


def is_palindrome(string):
    word = reverse_string(string)
    if word == string:
        print("True")
    else:
        print("False")

is_palindrome(string)