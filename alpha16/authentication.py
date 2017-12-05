import hashids
from hashids import Hashids
import pyaes


def main():
	numbers_orig = raw_input("Please enter alphanumeric random number: > ").strip()
	digit_length = len(str(numbers_orig))
	#numbers = numbers_orig[:15]

	product_id = raw_input("Please enter the product id: > ").strip()
	serial_number = raw_input("Please enter serial_number: > ").strip()
	batch_number = raw_input("Please enter batch_number: > ").strip()

	key = str(serial_number)+str(batch_number)+str(digit_length)+str(product_id)
	authenticate_lcg(numbers_orig, key, serial_number, batch_number)


def authenticate_lcg(alpha_numbers, key, serial_number, batch_number):
	hashids = Hashids(min_length=16, salt=key)
	hashidEncoded = hashids.decode(alpha_numbers)
	if hashidEncoded == ():
		print 'unauthentic'
		return 0
	else:
		final=str(hashidEncoded).strip('(L,)')
		if len(final) != 16:
			print 'unauthentic'
			return 0
		# final = str(hashidEncoded)[1:16]

		if int(serial_number) <= 9:
			final = final[15:] + final[:15]
			print final

		key_32 = key.zfill(32)
		aes = pyaes.AES(key_32)

		str_random = final[6:]
		plaintext_bytes = [ord(i) for i in str_random.zfill(16)]
		ciphertext = aes.encrypt(plaintext_bytes)
		print ciphertext
		a = 0
		sec_a=""
		sec=""
		ba_num=""
		ser_num=""

		a = sum(ciphertext)
		sec_aes = str(a).zfill(4)
		for i in xrange(2,len(sec_aes)):
			sec_a=sec_a+sec_aes[i]
		for i in xrange(4,len(final)-10):
			sec=sec+final[i]
		for i in xrange(2, len(final) - 12):
			ba_num = ba_num + final[i]

		for i in xrange(0, len(final) - 14):
			ser_num = ser_num + final[i]
		if (sec_a == sec) and (ba_num==batch_number) and (ser_num==serial_number) :
			print 'authentic'
		else:
			print 'unauthentic'



if __name__ == "__main__":
	main()




