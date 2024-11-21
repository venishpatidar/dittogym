from setuptools import setup

setup(
    name='dittogym',
    version='0.1',
    packages=['dittogym'],
    install_requires=['opencv-python', 'gym', 'numpy', 'taichi'],
    include_package_data=True,
    package_data={
        'dittogym': ['bg/*'],  # Include specific directories
    },
)
