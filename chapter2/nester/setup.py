#setup.py
from distutils.core import setup

setup(
    name = 'firstDIstribution',
    version = '1.2.0',
    py_modules = ['nester'],
    author = 'yizhishi',
    author_email = '283620911@qq.com',
    url = 'https://github.com/yizhishi',
    description = 'first distribution',
)
'''
python setup.py sdist

python setup.py install

pip install twine

twine upload dist/*

嘿嘿
'''
