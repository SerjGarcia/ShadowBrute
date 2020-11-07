# ShadowBrute
  A password cracker for linux shadow hashes.

# Important Notes
  You will need to fill a file named shadows.txt of shadow hashes.
  
  Passwords list needs to be in the same directory.
  
  [line:8] cryptPass[0:19] you may need to change the length depending on salt size $6$...................$
  
  [line:11] 'rockyou.txt' change to the name of your password list.

# Requirements
  Python3
  
  Crypt

# Run
  python3 ShadowBrute.py
