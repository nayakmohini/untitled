import hashids
from hashids import Hashids
import pyaes


def main():
	numbers = raw_input("Please enter number of random numbers: > ").strip()
	numbers = int(numbers)
	product_id = raw_input("Please enter the product id: > ").strip()
	serial_number = raw_input("Please enter serial_number: > ").strip()
	batch_number = raw_input("Please enter batch_number: > ").strip()

	if int(serial_number) <= 9:
		serial=str(serial_number).zfill(2)
	else:
		serial = serial_number

	if int(batch_number) <= 9:
		batch=str(batch_number).zfill(2)
	else:
		batch = batch_number


	digit_length = raw_input("Please enter number of digits in the alphanumeric number: > ").strip()
	key = str(serial) + str(batch) + str(digit_length) + str(product_id)
	key_32 = key.zfill(32)
	aes = pyaes.AES(key_32)
	generate_lcg(numbers, aes,key, serial, batch)



def generate_lcg(num_iterations, aes,key, serial_number, batch_number):
	"""LCG RANDU- generates as many random numbers as requested by user, using a Linear Congruential Generator LCG uses the formula: X_(i+1) = (aX_i + c) mod m. This LCG uses the RANDU initial setting, a=65539; c=0; m=2^31.
	:param num_iterations: int - the number of random numbers requested
	:return: void
   """
	x_value = 1  # Our seed, or X_0 = 123456789
	a = 1103515245   # Our "a" base value
	c = 12345  # Our "c" base value
	m = 2 ** 31  # Our "m" base value

	# counter for how many iterations we've run
	counter = 0
	# Open a file for output
	outFile = open("lgc_RANDU_output1.txt", "wb")
	# Perfom number of iterations requested by user2
	while counter < num_iterations:
		# Store value of each iteration
		x_value = (a * x_value + c) % m
		x_value_10 = str(x_value).zfill(16)
		plaintext_bytes = [ord(i) for i in x_value_10]
		a_sum = 0
		# plaintext_bytes = [ ord(c) for c in plaintext_16 ]
		# # 32 byte key (256 bit)
		# key = "100115manipal digital"
		# key_32 = key.zfill(32)
		# # Our AES instance
		# aes = pyaes.AES(key_32)
		# # Encrypt!
		ciphertext = aes.encrypt(plaintext_bytes)
		#print ciphertext

		#sum = 0
		# for value in plaintext_bytes:
		# 	sum = sum + value
		a_sum = sum(ciphertext)
		sec = str(a_sum).zfill(4)

		if int(serial_number) <= 9:
			number = serial_number[1] + batch_number + sec[2]+sec[3] + str(x_value).zfill(10) + serial_number[0]
		else:
			number = serial_number + batch_number + sec[2]+ sec[3] + str(x_value).zfill(10)

		hashids = Hashids(min_length = 16, salt = key)
		hashidEncoded = hashids.encode(int(number))
		#final_Str = hashidEncoded + sec[2]
		final_Str = hashidEncoded
		#print final_Str

		# hashids = Hashids(min_length = 14, salt = key)
		# hashDecoded = hashids.decode(hashidEncoded)
		# print hashDecoded
		outFile.write(final_Str + "\n")
		# writeValue = int(x_value)
		# outFile.write(str(x_value).zfill(8) + "\n")
		counter = counter + 1
	outFile.close()

	print "Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_RANDU_output.txt'."
#
#
if __name__ == "__main__":
	main()

# import sys
#
#
# def main():
# 	for x in sys.argv:
# 		print "Argument: ", x
#
# if __name__ == "__main__":
# 	main()

# 16 byte block of plain text
# plaintext = "1234567890"
# plaintext_16 = plaintext.zfill(16)
# plaintext_bytes = [ ord(c) for c in plaintext_16 ]
# # 32 byte key (256 bit)
# key = "100115manipal digital"
# key_32 = key.zfill(32)
# # Our AES instance
# aes = pyaes.AES(key_32)
# # Encrypt!
# ciphertext = aes.encrypt(plaintext_bytes)
# print ciphertext
# # Decrypt!
# decrypted = aes.decrypt(ciphertext)
# # True
# print decrypted == plaintext_bytes


# from hashids import Hashids
#
# hashids = Hashids(min_length=15,salt='090116manipal digital')
# hashidEncoded = hashids.encode(901312345678900)
# print hashidEncoded
#
# hashids = Hashids(min_length=15,salt='090116manipal digital')
# hashDecoded = hashids.decode(hashidEncoded)
# print hashDecoded


# def main():
# 	number_observations = raw_input("Please enter number of random numbers: > ").strip()
# 	number_observations = int(number_observations)
# 	number_digits = raw_input("Please enter number of digits in random number: > ").strip()
# 	number_digits = int(number_digits)
# 	generate_lcg(number_observations, number_digits)
#
#
# def generate_lcg(num_iterations, num_digits):
# 	"""
# 	LCG RANDU- generates as many random numbers as requested by user, using a Linear Congruential Generator
# 	LCG uses the formula: X_(i+1) = (aX_i + c) mod m.
# 	This LCG uses the RANDU initial setting, a=65539; c=0; m=2^31.
#
# 	:param num_iterations: int - the number of random numbers requested
# 	:return: void
#    """
#
# 	x_value = 123456789  # Our seed, or X_0 = 123456789
# 	a = 101429  # Our "a" base value
# 	c = 321  # Our "c" base value
# 	m = 2 ** 24  # Our "m" base value
#
# 	# x_value = 1  # Our seed, or X_0 = 123456789
# 	# a = 101429  # Our "a" base value
# 	# c = 321  # Our "c" base value
# 	# m = 2 ** 28  # Our "m" base value
#
# 	# counter for how many iterations we've run
# 	counter = 0
# 	# Open a file for output
# 	outFile = open("lgc_RANDU_output.txt", "wb")
#
# 	# Perfom number of iterations requested by user2
#
# 	while counter < num_iterations:
# 		# Store value of each iteration
# 		x_value = (a * x_value + c) % m
# 		writeValue = str(x_value).ljust(num_digits, '0')
# 		outFile.write(writeValue + "\n")
# 		# writeValue = int(x_value)
# 		# outFile.write(str(x_value).zfill(8) + "\n")
# 		counter = counter + 1
# 	outFile.close()
# 	print "Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_RANDU_output.txt'."
#
#
# if __name__ == "__main__":
# 	main()


