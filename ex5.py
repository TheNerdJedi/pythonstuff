name = 'Shajed'
age = 18
height = 83.0
weight = 220.0 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilogram_weight = weight * 0.45
centimeters_height = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth is usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + 	weight)

print "Now let's convert the pounds to kilograms and the inchs to centimeters."
print "%d pounds is equal to %d kilograms" % (weight, kilogram_weight) 
print "%d inches is equal to %d centimeters"% (height, centimeters_height)

# %s, %r, %d are formatters
