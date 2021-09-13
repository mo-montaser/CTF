# CSAW CTF 2021

## checker challenge


![challenge image](https://myoctocat.com/assets/images/base-octocat.svg)

Checker.py has 5 functions (up, down, right, left, encode). The first four functions make the encoding process by doing some operations on the string. The last one "encode" calls the previous ones and return the final encoded string.

###### up function

It's itrate on every charachter in the string and make 2 operations on this char. The first one is to "Unicode" encode it. Then, shift lift the encoded char by 1 (shift lift by 1 equals the encoded value * 2 ^ 1).

######  down function

This function just does one thing. It toggles between 1 and 0. 

###### right function

It takes 2 arguments "x" (the string) and "d" is an intger. Then, it changes the value of the string to make it starts from the "d" char to the end and then concatenates to it the remaining value. 

###### left function

It calls "right" function first. Then it reverses the output string from "right".
