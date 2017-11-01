my_name = 'John C. Beutz'
my_age = 29 # A lie
my_height = 4 # inches
my_weight = 10 # on the moon
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "let's talk about %s" % my_name
print "he's %d fathoms tall." % my_height
print "he's %d pounds heavy on the moon." % my_weight
print "he's got %s eyes and %s hair." % (my_eyes, my_hair)
print "his teeth are %s." % my_teeth

# this line is tricky, try to get it exactly right
print "If it add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_weight + my_weight)
