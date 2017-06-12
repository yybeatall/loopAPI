import csv
def set_token(input_value):
   value = input_value
   file = open("token.txt", "w")
   file.write(value)
   file.close()

def get_token():
    file = open('token.txt', 'r')
    value = file.read()
    return value