#WordCloud.py
import wordcloud # need module matplotlib
import jieba
import imageio
#from scipy.misc import imread              scipy.misc.imread()被弃用, 使用imageio.imread()


mask = imageio.imread('star.png')


filename = '新时代中国特色社会主义.txt'

f = open(filename, 'r', encoding='UTF-8')
t = f.read()
f.close()




w = wordcloud.WordCloud(\
                        font_path = 'msyh.ttc', \
                        mask = mask, \
                        width = 1000, height = 700, \
                        background_color = 'white', \
                        max_words = 15 \
                        )

w.generate(' '.join(jieba.lcut(t)))# 加载文本

w.to_file('outfile.png') #输出文件

