from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
with open('text_chin.txt', 'r') as f:
    text = f.read()

cut_text = " ".join(jieba.cut(text))

wordcloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path="stxingka.ttf",
    background_color='white',
    max_words=2000,
    max_font_size=40
).generate(cut_text)
wordcloud.to_file("rec_chin.jpg")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()