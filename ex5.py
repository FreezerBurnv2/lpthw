name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 #inches converted to cm by 2.54
weight = 180 * .45 # lbs converted to kilo by .45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r cm tall." % height
print "He's %r kilo heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % round (
	age, height, weight, age + height + weight)