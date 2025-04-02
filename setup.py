from setuptools import setup, find_packages

setup(
    name='EmotionDetection',             # ✅ 包名
    version='0.1',
    description='Emotion detection using Watson NLP API',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),           # 自动查找所有含 __init__.py 的包
    install_requires=['requests'],      # 声明依赖
)