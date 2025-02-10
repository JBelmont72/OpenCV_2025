'''
https://gamedevacademy.org/python-struct-tutorial-complete-guide/

struct library_defines the structure of our binary data. Each character represents a specific type of data, and there can be optional prefixes.
'''
# importing struct module
import struct
# use 'b' format to tell we are using bytes
print(struct.pack('b', 15))