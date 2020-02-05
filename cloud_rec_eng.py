import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open("text_eng.txt", 'r') as f:
    text = f.read()

wordcloud = WordCloud(max_font_size=40).generate(text)
wordcloud.to_file("rec_eng.jpg")

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()