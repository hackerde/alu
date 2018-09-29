'''Program to simulate the action of a 1-bit ALU using python programming language. Generates outputs for all possible input combinations. By Anway De. 10/29/2017'''

from blogic import *

def alu(F_0, F_1, INVA, ENA, ENB, Carry_In, A, B):
	'''Basic function 'alu' to take in 8 inputs and give two outputs based on the 1-bit ALU circuit.'''
	A = bxor(band(A, ENA), INVA)
	B = band(B, ENB)
	A_and_B = band(band(A, B), band(bnot(F_0), bnot(F_1)))
	A_or_B = band(bor(A, B), band(bnot(F_0), F_1))
	not_B = band(bnot(B), band(F_0, bnot(F_1)))
	A_sum_B = band(bxor(Carry_In, bxor(A, B)), band(F_0, F_1))
	A_carry_B = bor(band(Carry_In, bxor(A, B), band(F_0, F_1)), band(A, B, band(F_0, F_1)))
	Output = bor(A_and_B, A_or_B, not_B, A_sum_B)

	output = int(str(Output)+str(A_carry_B), 2)											#convert output and carry-out to integer

	return output																		#returns an integer

def print_call(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
	'''Basic function 'print_call' to take in the input for the 'alu' function and generate one line of output with proper formatting.'''
	value = alu(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)							#receiving output from alu function
	print ("alu(", arg1, ", ", arg2, ", ", arg3, ", ", arg4, ", ", arg5, ", ", arg6, ", ", arg7, ", ", arg8, ") --> ", value, sep='')

def print_section(F_0, F_1, INVA, ENA, ENB):
	'''Basic function 'print_section' to call 'print_call' 8 times with 1 input for the 5 control lines. Prints out a 8-line long section of output with proper formatting.'''
	print ("\nF0=", F_0, ", F1=", F_1, ", INVA=", INVA, ", ENA=", ENA, ", ENB=", ENB, sep='')
	for i in range(8):
		binary = int(bin(i)[2:], 2)														#using loop control variable 
		Carry_In = (binary >> 2) & 1													#to generate input
		A = (binary >> 1) & 1															#for the three input lines
		B = (binary >> 0) & 1
		print_call(F_0, F_1, INVA, ENA, ENB, Carry_In, A, B)

#main
for i in range(32):
	binary = int(bin(i)[2:], 2)															#using loop control variable 
	F_0 = (binary >> 4) & 1																#to generate input
	F_1 = (binary >> 3) & 1																#for the five control lines
	INVA = (binary >> 2) & 1
	ENA = (binary >> 1) & 1
	ENB = (binary >> 0) & 1
	print_section(F_0, F_1, INVA, ENA, ENB)