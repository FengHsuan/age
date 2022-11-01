driving = input('have you ever driven a car before?')
if driving != 'yes' and driving != 'no':
	print('please answer yes or no')
	raise SystemExit

age = input('how old are you？')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('you have passed the test')
	else:
		print('you have broken the law')
elif driving == 'no':
	if age >= 18:
		print('you are able to get a car license')
	else:
		print('you still have few years to wait')
else:
	print('please answer yes or no')