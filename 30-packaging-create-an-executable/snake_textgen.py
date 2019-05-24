import random

adjectives = ['slimey', 'slithery', 'sneaky']
noun = ['snake', 'legless reptile', 'serpent']

text = ''
for i in range(50):
    text += 'A {} {}\n'.format(random.choice(adjectives), random.choice(noun))

with open('out.txt', 'w') as f:
    f.write(text)
