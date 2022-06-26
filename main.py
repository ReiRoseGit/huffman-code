from Compress import *

if __name__ == '__main__':
    c = Compress("input.txt")
    c.write_message()
    print(c.decode_message())
