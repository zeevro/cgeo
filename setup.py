try:
    from setuptools import setup, Extension
except ImportError:
    from distutils import setup, Extension

setup(name='cgeo',
      version='1.0',
      ext_modules=[Extension('cgeo._cgeo', ['cgeo.c'])])
