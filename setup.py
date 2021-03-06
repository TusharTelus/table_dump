from setuptools import setup, find_packages
import os
here = os.path.abspath(os.path.dirname(__file__))

README = "Table-DUMP"

requires = [
    'pyramid==1.10.4',
    'redis==3.4.1',
    'google-cloud-bigquery',
    'requests==2.23.0',
    'rq==1.4.2',
    'google-cloud-storage',
    'googleapis_common_protos'
]

setup(name='table_dump_application',
    version=0.1,
    description='table_dump_application',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web services",
    author='telus',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    paster_plugins=['pyramid'],
    entry_points="""\
    [paste.app_factory]
    main = src:main
    [console_scripts]
    table_dump_start = src.get_big_query
    """,
)
