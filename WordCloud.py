from wordcloud import STOPWORDS, WordCloud
import numpy as np
import matplotlib.pyplot as plot
import PIL.Image

text = open('text asset path goes here','r').read()

VaporeonMask = np.array(PIL.Image.open("picture asset path goes here"))

wc = WordCloud(stopwords=STOPWORDS, mask=VaporeonMask, background_color="white", min_font_size=1).generate(text)
plot.imshow(wc)
plot.axis("off")
plot.show()