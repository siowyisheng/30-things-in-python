import pprint
import textacy
import textacy.keyterms

text = ("""\
Pit vipers, pythons, and some boas have infrared-sensitive receptors 
in deep grooves on the snout, which allow them to "see" the radiated heat 
of warm-blooded prey. In pit vipers, the grooves are located between the 
nostril and the eye in a large "pit" on each side of the head. Other 
infrared-sensitive snakes have multiple, smaller labial pits lining the 
upper lip, just below the nostrils.

Snakes use smell to track their prey. They smell by using their forked 
tongues to collect airborne particles, then passing them to the vomeronasal organ 
or Jacobson's organ in the mouth for examination. The fork in the tongue gives 
snakes a sort of directional sense of smell and taste simultaneously. 
They keep their tongues constantly in motion, sampling particles from the air, 
ground, and water, analyzing the chemicals found, and determining the presence 
of prey or predators in the local environment. In water-dwelling snakes, such 
as the anaconda, the tongue functions efficiently underwater.""")

print('--------------------------------------------------')
print('TEXT')
print('--------------------------------------------------')
print(text)

doc = textacy.Doc(text)
print('--------------------------------------------------')
print('KEY TERMS')
print('--------------------------------------------------')
pprint.pprint(
    textacy.keyterms.sgrank(
        doc, ngrams=(1, 2, 3, 4), normalize='lower', n_keyterms=0.1))

ts = textacy.TextStats(doc)
print('--------------------------------------------------')
print('READABILITY')
print('--------------------------------------------------')
pprint.pprint(ts.readability_stats)