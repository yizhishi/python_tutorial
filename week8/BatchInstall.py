#BatchInstall.py
import os

'''
pip install numpy # N维数据表示和运算
pip install matplotlib #二维数据可视化
pip install pillow # 图像处理
pip install sklearn # 机器学习和数据挖掘
pip install jieba
pip install beautifulsoup4 # HTML和XML解析器
pip install wheel # 第三方库文件打包工具
pip install pyinstaller # python 打包源文件为可执行文件
pip install django # web开发框架
pip install flask # 轻量级web开发框架
pip install werobot # 微信机器人开发框架
pip install sympy # 数学符号计算
pip install pandas # 高效数据分析和计算
pip install networkx # 复杂网络和图结构的建模与分析
pip install pyqt5 # 基于Qt的专业级GUI开发框架
pip install pyopengl # 多平台OpenGL开发接口
pip install pypdf2 # PDF提取与处理
pip install docopt # 命令行解析
pip install pygame # 简单小游戏开发
'''

libs = {'numpy', 'matplotlib', 'pillow', 'sklearn', 'jieba', 'beautifulsoup4', \
       'wheel', 'pyinstaller', 'django', 'flask', 'werobot', 'sympy', 'pandas', \
       'networkx', 'pyqt5', 'pyopengl', 'pypdf2', 'docopt', 'pygame'}

try:
    for lib in libs:
        print('lib: {} installed'.format(lib))

        os.system('pip install ' + lib)
        print('lib: {} installed'.format(lib))
    else:
        print('install end')
except:
    print('install fail')

