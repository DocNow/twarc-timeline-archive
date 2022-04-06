import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name='twarc-timeline-archive',
    version='0.1.3',
    url='https://github.com/docnow/twarc-timeline-archive',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    py_modules=['twarc_timeline_archive'],
    description='A twarc plugin to collect the timelines of a list of users',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.3',
    install_requires=['twarc>=2.0.8'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points='''
        [twarc.plugins]
        timeline-archive=twarc_timeline_archive:timeline_archive
    '''
)
