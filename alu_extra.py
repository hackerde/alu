'''Program to simulate the action of a n-bit ALU using python programming language. Determines number of ALUs required (n) based on user-input. Each ALU is created as an object. By Anway De. 11/03/2017'''

from blogic import *

class ALU:

	def __init__(self):																#initializes the ALU object with it's control and input lines
		self.F_0 = None
		self.F_1 = None
		self.INVA = 0
		self.ENA = 1
		self.ENB = 1
		self.Carry_In = None
		self.A = None
		self.B = None
		self.Carry_Out = None
		self.Output = None
		self.connected_to = None													#holds the next ALU that is connected to it

	def set_input(self, A, B):
		'''Sets the input lines of the ALU'''
		self.A = band(self.ENA, bxor(self.INVA, A))
		self.B = band(B, self.ENB)

	def set_control_lines(self, F_0, F_1, INVA=0, ENA=1, ENB=1, INC=0):
		'''Sets the control lines of the ALU'''
		self.F_0 = F_0
		self.F_1 = F_1
		self.INVA = INVA
		self.ENA = ENA
		self.ENB = ENB
		self.Carry_In = INC

	def set_connection(self, other):
		'''Establishes connection with another ALU'''
		self.connected_to = other

	def execute(self):
		'''The 'alu' fucntion is named 'execute here. It performs the same action of the 'alu' function'''
		A_and_B = band(band(self.A, self.B), band(bnot(self.F_0), bnot(self.F_1)))
		A_or_B = band(bor(self.A, self.B), band(bnot(self.F_0), self.F_1))
		not_B = band(bnot(self.B), band(self.F_0, bnot(self.F_1)))
		A_sum_B = band(bxor(self.Carry_In, bxor(self.A, self.B)), band(self.F_0, self.F_1))
		self.Carry_Out = bor(band(self.Carry_In, bxor(self.A, self.B), band(self.F_0, self.F_1)), band(self.A, self.B, band(self.F_0, self.F_1)))
		self.Output = bor(A_and_B, A_or_B, not_B, A_sum_B)

		if self.connected_to:
			self.connected_to.set_control_lines(self.F_0, self.F_1, INC = self.Carry_Out)
			self.connected_to.execute()												#starts execution of the ALU connected to it


#main
print("*********n-bit ALU Simulator***********")
print("This is a program to simulate the behaviour of an n-bit ALU. You control the output of the ALU by selecting the desired function.\n")
print("Menu:\n1. Perform bitwise AND between two numbers\n2. Perform bitwise OR between two numbers\n3. Generate 2's complement of a negative number\n4. Add two non-negative numbers\n")

'''Getting all the necessary inputs for the ALU's and avoiding stray inputs'''
while True:

	try:
		choice = int(input("Enter choice: "))
		if choice!=1 and choice!=2 and choice!=3 and choice!=4:
			raise ValueError()
	except:
		print("\nInvalid input! Try again.\n")
		continue

	if choice==1 or choice==2:
		while True:	
			try:
				A = int(input("Enter first number: "))
				break
			except:
				print("\nInvalid input! Try again.\n")
				continue
		while True:	
			try:
				B = int(input("Enter second number: "))
				break
			except:
				print("\nInvalid input! Try again.\n")
				continue
		break

	elif choice==4:
		while True:	
			try:
				A = int(input("Enter first non-negative number: "))
				if A<0:
					raise ValueError()
				break
			except:
				print("\nInvalid input! Try again.\n")
				continue
		while True:	
			try:
				B = int(input("Enter second non-negative number: "))
				if B<0:
					raise ValueError()
				break
			except:
				print("\nInvalid input! Try again.\n")
				continue
		break

	elif choice==3:
		A = 0
		while True:
			try:
				B = int(input("Enter negative number: "))
				if B>=0:
					raise ValueError()
				B = abs(B)
				break
			except:
				print("\nInvalid input! Try again.\n")
				continue
		break

n = max(len(bin(A)), len(bin(B))) - 2													#determines the number of ALUs required based on the size of user-input

'''Setting the control lines'''
if choice==1 or choice==2:
	F_0 = 0
else:
	F_0 = 1

if choice==1 or choice==3:
	F_1 = 0
else:
	F_1 = 1

'''Creating the list of ALUs or the 'CPU' '''
CPU = []
for i in range(n):
	new_alu = ALU()
	new_alu.set_control_lines(F_0, F_1)
	new_alu.set_input((A >> i) & 1, (B >> i) & 1)
	if i-1>=0:
		CPU[i-1].set_connection(new_alu)												#every ALU is connected to its following ALU
	CPU.append(new_alu)

CPU[0].execute()																		#executing the first triggers the execution of all the others

if choice==3:
	for alu in CPU:
		alu.set_input(0, alu.Output)
	CPU[0].set_control_lines(1, 1, INC = 1)												#adding 1 to the LSB to get the 2's complement result
	CPU[0].execute()

result = ""

for i in range(n-1, -1, -1):
	if choice==4 and i==n-1 and CPU[i].Carry_Out==1:
		result += str(CPU[i].Carry_Out)
	result += str(CPU[i].Output)														#constructing the output from the output bits

if choice==3:
	result = '1' + result																#Adding the MSB for 2's complement representation

print()
print ("The result of the operation in the ALUs yield:", result)

if choice==4:
	print("The sum of the two numbers is", int(result, 2))
