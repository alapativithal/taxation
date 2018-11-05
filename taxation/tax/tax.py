# file sai_mod.py

foo = 200

def method_1(string):
	print string
	return string


if __name__ == "__main__":
	print 'Executing as Main'
	string =raw_input('Enter a String: ')
	method_1(string)
else:
	print 'Not xecuting as Main'
	# string =raw_input('Enter a String: ')
	# method_1(string)
