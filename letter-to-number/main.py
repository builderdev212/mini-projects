#This program takes the normal alphabet and transfers it into numbers. It also changes thoes numbers with the key you give to it in the input. Then it prints the alphabet according to the changed cipher.
w = {chr(n+ord('a')): n+1 for n in range(26)}
#letter and number symbols
doing = input('Would you like to either 1, encrypt you message, or 2, decrypt you message?\n')
inkey = input('Enter your key.\n')
message = input('Enter your message here.\n')
#key input
def makekey(inkey):
   key = inkey
   key = int(key)+int(key)
   key = int(key)*int(key)
   key = key*9
   key = key-65
   return key
#key encription
key = makekey(inkey)
print('The key you entered was '+str(key)+'.\n')
for letter, num in w.items():
   key = int(key)
   num += key
   letter = str(letter)
   num = str(num)
   print('{0} - {1}'.format(letter, num))
   
