import argparse
import datetime as dt

from data_report import make_report, Insight

parser = argparse.ArgumentParser(description='Make a snake population report.')
parser.add_argument(
    '--move',
    action='store_true',
    help='move the images into the report\'s directory')
parser.add_argument(
    '--monthend', action='store_true', help='creates a monthend report')
args = parser.parse_args()

insights = [
    Insight(
        title='No. of purple snakes - increased 27%',
        text="""\
There are over 2,900 species of snakes ranging as far northward as the Arctic Circle 
in Scandinavia and southward through Australia.[18] Snakes can be found on every 
continent except Antarctica, in the sea, and as high as 16,000 feet (4,900 m) in the 
Himalayan Mountains of Asia.[18][31]:143 There are numerous islands from which snakes 
are absent, such as Ireland, Iceland, and New Zealand[4][31] (although New Zealand's 
waters are infrequently visited by the yellow-bellied sea snake and the banded sea krait).[32]
""",
        img='i1.png',
        source='https://en.wikipedia.org/wiki/Snake'),
    Insight(
        title='There are legless lizards, which are not snakes',
        text="""\
While snakes are limbless reptiles, which evolved from (and are grouped with) lizards, there are 
many other species of lizards which have lost their limbs independently and superficially look 
similar to snakes. These include the slowworm and glass snake.
""",
        img='i2.png',
        source='https://en.wikipedia.org/wiki/Snake'),
]

make_report(
    insights,
    date=dt.date(2018, 10, 5),
    move=args.move,
    month_end=args.monthend)
