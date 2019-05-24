#!/usr/bin/env python

from PIL import Image
import random
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
from wordcloud import WordCloud, STOPWORDS

text = open('thesnakesofeurope.txt').read()

mask = np.array(Image.open("pythonlogo.png"))

stopwords = set(STOPWORDS)


def blue_color_func(word,
                    font_size,
                    position,
                    orientation,
                    random_state=None,
                    **kwargs):
    return "hsl({}, {}%, {}%)".format(
        random.randint(185, 205), 100, random.randint(30, 35))


wc = WordCloud(
    max_words=200,
    mask=mask,
    stopwords=stopwords,
    width=600,
    height=600,
    scale=4,
    background_color='yellow',
    color_func=blue_color_func).generate(text)

# store to file
wc.to_file("snakes.png")