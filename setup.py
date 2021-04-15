import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name='twarc-timelines',
    version='0.0.1',
    url='https://github.com/docnow/twarc-timelines',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    py_modules=['twarc_timelines'],
    description='A twarc plugin to collect the timelines of a list of users',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.3',
    install_requires=['twarc'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points='''
        [twarc.plugins]
        timelines=twarc_timelines:timelines
    '''
)
