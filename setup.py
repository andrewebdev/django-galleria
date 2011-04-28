from distutils.core import setup

setup(
    name="django-galleria",
    description="A django app that plugs the galleria javascript gallery into your project. (Requires Django 1.3+)",
    version="0.1",
    url="",
    author="Andre Engelbrecht",
    author_email="andre@teh-node.co.za",
    packages=['galleria'],
    package_dir={'': 'src'},
)
