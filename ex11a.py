print '\nWhat\'s your name ?',
name = raw_input('-->')
print '\nHow old are you, %s' % name,
age = int(raw_input('-->'))
print '\nHow tall are you (in cm), %s' % name
height = int(raw_input('-->'))
print '\nHow much do you weight (in kg), %s' %name
weight = int(raw_input('-->'))

print '\nSo, %s is %d years old, %d cm tall and weighs %d kg.\n' % (
	name, age, height, weight)
