import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f.startswith('EYE')
		os.remove(f)