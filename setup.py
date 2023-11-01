from setuptools import setup, find_packages

setup(
    name='pyCapture',
    version='1.0.0',
    description=(
        "Writeup Code Similarity Audit Tool"
    ),
    author="d1ag0n",
    author_email="1094093288@qq.com",
    maintainer="d1ag0n",
    maintainer_email="1094093288@qq.com",
    packages=find_packages(),
    url="https://github.com/D1ag0n-Young/pyCapture",
    install_requires=[
        'pandas',
        'Levenshtein',
        'scikit-learn',
        'markdown',
        'markdown-it-py',
        'bs4'
    ],
    package_data={
        'pyCapture': ['*.ini']
        # 包含其他文件或目录
    }
)

# python setup.py bdist_wheel
# pip wheel -r requirements.txt -w pycapture-wheels -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install --no-index --find-links=pycapture-wheels/ pyCapture