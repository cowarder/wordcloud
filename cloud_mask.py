from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

with open("text_eng.txt", 'r') as f:
    text = f.read()

mask = np.array(Image.open("./image/star.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue').generate(text)

wc.to_file("cloud_mask.png")

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()