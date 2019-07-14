#BatchInstall.py
import os

'''
numpy # N维数据表示和运算
matplotlib #二维数据可视化
pillow # 图像处理
sklearn # 机器学习和数据挖掘
jieba # 中文分词
beautifulsoup4 # HTML和XML解析器
wheel # 第三方库文件打包工具
pyinstaller # python 打包源文件为可执行文件
django # web开发框架
pyramid # 中型web开发框架
flask # 轻量级web开发框架
werobot # 微信机器人开发框架
sympy # 数学符号计算
pandas # 高效数据分析和计算
networkx # 复杂网络和图结构的建模与分析
pyqt5 # 基于Qt的专业级GUI开发框架
pyopengl # 多平台OpenGL开发接口
pypdf2 # PDF提取与处理
docopt # 命令行解析
pygame # 简单小游戏开发
puspider # web页面爬取
goose # 提取web信息
aip # 百度AI
myqr # 二维码
wxpython # 跨平台GUI
pygobject # Gkt+Gui
quads # 迭代, 像素风
ascii_art # ascII
tabulate #  二维表格输出
'''

libs = {'numpy', 'matplotlib', 'pillow', 'sklearn', 'jieba', 'beautifulsoup4', \
       'wheel', 'pyinstaller', 'django', 'flask', 'werobot', 'sympy', 'pandas', \
       'networkx', 'pyqt5', 'pyopengl', 'pypdf2', 'docopt', 'pygame', 'puspider', \
        'goose', 'pyramid', 'aip', 'myqr', 'wxpython', 'pygobject', 'quads', 'ascii_art', \
        'tabulate'}

try:
    for lib in libs:
        os.system('pip install ' + lib)
        print('lib: {} installed'.format(lib))
    else:
        print('install end')
except:
    print('install fail')

