import sys

#caller function that accepts a string and a callback function
def handle_request(input, callback):
    callback(input)
print(handle_request(sys.argv[1]))
