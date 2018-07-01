from distutils.core import setup, Extension
from distutils.dir_util import remove_tree
from distutils import ccompiler
import os.path

c_args = []
compiler = ccompiler.get_default_compiler()
if compiler == 'unix':
    c_args.append('-O3')

src_path = os.path.join(os.path.dirname(__file__), 'cgeo.c')
cgeo = Extension('cgeo', [src_path], extra_compile_args=c_args)

setup(name='cgeo', version='1.0', ext_modules=[cgeo])

if os.path.isdir("build"):
    remove_tree("build", 1)
