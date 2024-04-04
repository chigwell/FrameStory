from setuptools import setup, find_packages

setup(
    name='FrameStory',
    version='0.1.3',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A Python package for creating video descriptions by analyzing and extracting significant frames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/FrameStory',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25,<3',
        'opencv-python>=4.0,<5',
        'numpy>=1.19,<2',
        'Pillow>=8.0,<9',
        'transformers>=4.0,<5',
        'tqdm>=4.0,<5'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Video',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
