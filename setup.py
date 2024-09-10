from setuptools import Extension, setup


setup(ext_modules=[Extension('cgeo._cgeo', ['cgeo.c'], py_limited_api=True)])
