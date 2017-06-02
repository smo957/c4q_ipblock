#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sungmin Oh

Technical Assessment - IP Block Calculator

"""

import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Check if IP Addesss is in IP block')

# Required positional arguments
parser.add_argument('block', type=str,
                    help='IP Block. Example: 12.23.34.45/15')
parser.add_argument('address', type=str,
                    help='IP Address. Example: 12.22.35.44')

block = parser.parse_args().block
address = parser.parse_args().address

print block
print address

## Check user input
if "/" not in block:
    parser.error("IP Block is missing the backslash.")
if block.count(".") != 3:
    parser.error("IP Block needs exactly three periods.")
if address.count(".") != 3:
    parser.error("IP Address needs exactly three periods.")

# Parse and store IP block and address into arrays
block_array = block.split(".")
address_array = address.split(".")
shared_bits = int(block_array[3].split("/")[1])
block_array[3] = block_array[3].split("/")[0]

# Function to convert a number in string type to 8-bit binary number
def toBin(num):
    temp_bin = "{0:b}".format(int(num))
    return '0' * (8-len(temp_bin)) + temp_bin
#print toBin(12)
#print toBin(80)
#print toBin(100)

# Convert IP block and address to binary numbers
block_binary = ''
address_binary = ''
for num in block_array:
    block_binary += toBin(num)
for num in address_array:
    address_binary += toBin(num)
#print block_binary
#print address_binary


# Compare IP block and address up to the shared_bits
if block_binary[:shared_bits] == address_binary[:shared_bits]:
    print "in block"
else:
    print "not in block"
