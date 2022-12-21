from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

exts = [
    Extension(name="darkflow.cython_utils.nms", sources=["darkflow/cython_utils/nms.pyx"],
              include_dirs=[np.get_include()]),
    Extension(name="darkflow.cython_utils.cy_yolo_findboxes",
              sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
              include_dirs=[np.get_include()]),
    Extension(name="darkflow.cython_utils.cy_yolo2_findboxes",
              sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
              include_dirs=[np.get_include()]),
]

setup(
    packages=[
        "darkflow.cython_utils.nms",
        "darkflow.cython_utils.cy_yolo_findboxes",
        "darkflow.cython_utils.cy_yolo2_findboxes",
    ],
    package_dir={
        "darkflow": "/content/darkflow",
    },
    ext_modules=cythonize(
        module_list=exts,
        compiler_directives={"language_level": "3"},
    )
)