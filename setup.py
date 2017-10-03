from setuptools import setup

setup(name='grouper',
      version='0.1.1',
      scripts=['bin/Grouper'],
      description='Accurate, Fast and Lightweight Clustering of de novo Transcriptomes using Fragment Equivalence Classes',
      url='https://github.com/COMBINE-lab/Grouper',
      author='Laraib Malik, Fatemeh Almodaresi, Rob Patro',
      author_email='rob.patro@cs.stonybrook.edu',
      license='BSD with attribution',
      packages=['grouper'],
      install_requires=[
          'PyYAML',
          'coloredlogs',
          'click',
          'networkx',
          'numpy',
          'pandas',
          'tqdm'
      ],
      zip_safe=False)