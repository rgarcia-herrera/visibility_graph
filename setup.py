from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

    
setup(name='visibility_graph',
      version='0.2',
      description='From time series to graph thru visibility algorithm.',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
      ],
      url='http://github.com/CSB-IG/visibility_graph',
      author='Rodrigo Garcia',
      author_email='rgarcia@inmegen.gob.mx',
      license='GPLv3',
      packages=['visibility_graph'],
      install_requires=[ 'networkx' ],
      scripts=['bin/series2edgelist.py'],
      include_package_data=True,
      zip_safe=False)
