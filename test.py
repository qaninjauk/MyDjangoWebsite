import sys

print (sys.version)
print (sys.executable)

def greet(who_to_great):
    greeting = (f"Hello" ,{(who_to_great)} )
    return greeting

print(greet('world'))
print(greet ('Corey'))
