#!/usr/bin/env python3
import crypt

def prRed(k): 
    print("\033[91m {}\033[00m" .format(k))

def testPass(cryptPass):
	salt = cryptPass[0:19] # change depending on salt length in hash
	print(" [=] The password\'s salt: ", salt)
	n = 0
	with open('rockyou.txt', 'r') as infile: # change file name if different
	    for line in infile:
		    w = line.strip('\n')
		    cryptWord = crypt.crypt(w, salt)
		    print(" [=] Tryed:"+ str(n) + " Trying pass... " + w, '\r', end="")
		    n += 1
		    if (cryptWord == cryptPass):
		    	a = ("\n" + " [+] Found password: " + w + "\n")
		    	prRed(a)
		    	return
	    print(" [-] Password not found.\n")
	return
	
def main():
	with open('shadows.txt') as shadowFile:
	    for line in shadowFile.readlines():
		    if ":" in line:
		    	user = line.split(':')[0]
		    	cryptPass = line.split(':')[1].strip(' ')
		    	print(" [+] Cracking Password for: " + user)
		    	testPass(cryptPass)

if __name__ == "__main__":
	main()

