#Create a string with single Quotes
string1= 'Welcome to the Geeks World'
print("I'm a Geek")
print(string1)

#Create a String with double Quotes
string2 = "I'm a Geek"
print(string2)

#Create a String with triple Quotes
string3 = '''"I'm a Geek and I live in a world of "Geeks"'''
print(string3)

#Create String with triple Quotes allows multiple lines
string4 = '''Geeks
            For
            Life'''
print(string4)

# __doc__ : 
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply.__doc__)
