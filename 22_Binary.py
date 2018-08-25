
# ================
# 22_Binary.py
# ================

# we will now see how to read and write binary files in python
# There are two main reasons why you want to deal with binary
# (1) Processing binary data like an image file
# (2) May want to store variables in our program so we can load them back later.

# The basic principles of reading and writing text files can be applied here
# We will write binary data and then read it back again

# Its similar to text file but we need to specify mode as 'b' for binary and then "r" or "w"
# NOTE that "strings" and "integers" cannot be written directly to binary file,
# but need to be converted to "bytes" format
#
# Python has several methods of doing this including:
# (1) "bytes" built in function
# (2) Two underscore bytes objects of integer objects that does that


# ==========
# "bytes"
# ==========

# "bytes" is a built in function that converts numbers to binary format

# We will start by writing the numbers 0 to 16 to a binary file and then reading them back again.
# binary file will be called "binary_file1"
# Specify 'bw' to show we are writing a binary file. if you only use 'w', it will assume its a text file

# This code: "bin_file.write(bytes[i])" we are converting number in position i to byte format
# and then writing it to file bin_file

# Code to write to binary file named "binary_file1"
# "bytes" is a python inbuilt function to convert data (in this case integers) to binary

with open("binary_file1", 'bw') as bin_file:
    for i in range(17):  # we specify range 17 because we want 0 to 16 to be printed
        print("{} in binary is {}".format(i, bytes([i]))) # we print the output or each iteration in bytes
        bin_file.write(bytes([i]))  # bytes inbuilt function converts numbers to binary and writes them to bin_file. We pass list [i] position to bytes function.


print("="*50)

# you need to convert input to bytes to be able to save it in a binary file like binary_file1
# Code to read binary_file1 that we wrote above


print("Now we read binary_file1")
print()

with open("binary_file1", 'br') as binFile:  # now we use "br"  for binary read
    for b in binFile:
        print(b)  # This prints a two straight lines because there is only one \n

print("="*50)

# Note that we pass a list [i] to byte function ==> bytes([i]), because if you pass an integer to it,
# it creates that many bites all sets then all to zero e.g. pass it 3, it creates 3 bytes and sets to 0
# Pass it 7 and it creates 7 bytes and sets them to zero

print()
print(bytes(1))  # shows results of bytes when passed an integer
print(bytes(2))
print(bytes(3))
print(bytes(7))

print("="*50)


# A Better way to write above code with one less line is passing range() to bytes and removing the for loop


with open("binary_file1", 'bw') as bin_file:
    print("0 to 17 in binary is:  {}".format(bytes(range(17)))) # we pass the range to bytes function and print
    bin_file.write(bytes(range(17)))  # pass range to bytes function and write it to bin_file

# you need to convert input to bytes to be able to save it in a binary file like binary_file1
# Code to read binary_file1 that we wrote above

print()
print("Now we read binary_file1")
print()

with open("binary_file1", 'br') as binFile:  # now we use "br"  for binary read
    for b in binFile:
        print(b)  # This prints a two straight lines because there is only one \n

print("="*50)


# ==============================
# "to_bytes" and "from_bytes"
# ==============================

# "to_bytes" converts integers to binary
# "from_bytes" converts binary back to integers

# A good use of binary files is writing numerical values in binary
# The integer method has a two underscore byte method that allows us to do that

# in this example, we will write the value out of 4 values and allow us to read those values back again.

a = 65534       # FF FE  (2 bytes)
b = 65535       # FF FF  (2 bytes)
c = 65536       # 00 01 00 00  (4 bytes) (we need 3 bytes but we usually use even number bytes in binary)
x = 2998302     # 00 2D C0 1E  (4 bytes) (we need 3 bytes but we usually use even number bytes in binary)

# This will print above variables in hexadecimal

print("== print in hexadecimal ===")
print()
print("{:>04x}".format(a))  # > is right justified and < is left justified
print("{:>04x}".format(b))
print("{:>08x}".format(c))
print("{:>08x}".format(x))
print()

# This code will write the the binary numbers to "binary_file2"

# It converts integers to binary using "to_bytes"
# "big" and "little" referred to here is indian i.e. how computer manufacturers store numbers
# "big" indian stores the most significant byte first, with the remaining bytes of the number following in order
# "little" indian stores the least significant byte first

with open("binary_file2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))  # we convert a to binary, give it 2 bytes space, then add it to bin_file
    bin_file.write(b.to_bytes(2, 'big'))  # we convert b to binary, give it 2 bytes space, then add it to bin_file
    bin_file.write(c.to_bytes(4, 'big'))  # we convert c to binary, give it 4 bytes space, then add it to bin_file
    bin_file.write(x.to_bytes(4, 'big'))  # we convert x to binary, it 4 bytes space, then add it to bin_file
    bin_file.write(x.to_bytes(4, 'little'))  # we convert x to binary, it 4 bytes space then add it to bin_file

# Now we use this code to read back "binary_file2
# NOTE: we use "from_bytes" to convert binary to integers
# We will assign numbers from a, b, c, x (big), x(little) to e, f, g, h, i

# from the results, first four (a. b, c, d) represent the numbers (a, b, c, x (big) as it was originally
# but i gives result 515910912 which is different from original x of 2998302
# This is because we saved it in "little" indian format and then tried to read it in "big" indian format
# so the bytes were in reverse order because they were initially written in "little" indian and we are no
# trying to read them in big format
# so it is important to understand the structure of a binary data in a file if you are to attempt to read it successfully

print("==== read back from binary ======")
print()

with open("binary_file2", "br") as bin_file:  # open binary_file2 and add content to variable bin_file
    e = int.from_bytes(bin_file.read(2), 'big')  # we read from bin_file
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')  # we will change this to big instead of little
    print(i)

print("="*50)
