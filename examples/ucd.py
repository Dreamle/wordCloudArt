#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

#INPUTTEXT = 'text/alice.txt'
INPUTTEXT = 'text/maria_text_all.txt'

INPUTMASK = "img/bear_honey_mask8x10.png"
#INPUTMASK = "img/alice_mask.png"
#INPUTMASK = "img/page_mask_72.png"

OUTPUTFILE = "output/bear_full_teal.pdf"

# Read the whole text.
text = open(path.join(d, INPUTTEXT)).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, INPUTMASK)))

print("read in image and mask file");

wordToRemove = ("end", "citep", "Figure", "figure", "fig", "used", "using", "cc",
	"xx", "ref", "table", "text", "c", "g", "H", "B", "t", "cdot", 
        "includegraphics")


def maria_color_fun(word=None, font_size=None, position=None,
                      orientation=None, font_path=None, random_state=None):
    """Random hue color generation.

    Default coloring method. This just picks a random hue with value 80% and
    lumination 50%.

    Parameters
    ----------
    word, font_size, position, orientation  : ignored.

    random_state : random.Random object or None, (default=None)
        If a random object is given, this is used for generating random numbers.

    """
    if random_state is None:
        random_state = Random()
    rv = random_state.randint(0, 4)
    H = random_state.randint(170, 190)
    S = random_state.randint(95, 100)
    B = random_state.randint(50, 80)
    return "hsl(%d, 80%%, 50%%)" % random_state.randint(160, 220)
    #return "hsl(%d, %d%%, %d%%)" % (H, S, B)
    if rv == 0:
	return "hsl(179, 96%, 55%)"
    elif rv == 1:
        return "hsl(187, 99%, 56%)"
    elif rv == 2 :
        return "hsl(174, 100%, 66%)"
    elif rv == 3:
        return "hsl(176, 99%, 76%)"
    else :
        return "hsl(63, 22%, 95%)"
    #return "hsl(%d, 80%%, 50%%)" % random_state.randint(0, 255)
    

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS.update(wordToRemove), color_func=maria_color_fun,
               min_font_size=8)

print("going to generate the cloud")
# generate word cloud
wc.generate(text)
print(wc.max_words)
# store to file
wc.to_file(path.join(d, OUTPUTFILE))

# show
plt.imshow(wc)
#plt.axis("off")
#plt.figure()
#plt.imshow(alice_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
