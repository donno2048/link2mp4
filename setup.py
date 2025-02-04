from setuptools import setup, find_packages
setup(
    name='link2mp4',
    version='1.0.2',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description='Download videos as MP4 files',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Hamagnivim/link2mp4',
    platforms="any",
    project_urls={
        'Documentation': 'https://github.com/Hamagnivim/link2mp4#readme',
        'Bug Reports': 'https://github.com/Hamagnivim/link2mp4/issues',
        'Source Code': 'https://github.com/Hamagnivim/link2mp4',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    install_requires=['selenium>=4.1.0', 'selenium-wire>=4.6.4', 'ffmpeg-python>=0.2.0', 'questionary>=1.10.0', 'm3u8>=2.0.0'],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'link2mp4=link2mp4.__main__:main' ] }
)
