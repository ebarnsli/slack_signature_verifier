# from distutils.core import setup
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='slack_signature_verifier',  # How you named your package folder (MyLib)
    packages=['slack_signature_verifier'],  # Chose the same as "name"
    version='0.3',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Verify your request from slack with your slack signing secret',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Give a short description about your library
    author='Erik Barns',  # Type in your name
    author_email='ebarns@labelinsight.com',  # Type in your E-Mail
    url='https://github.com/ebarnsli/slack_signature_verifier',
    # Provide either the link to your github or to your website
    download_url='https://github.com/ebarnsli/slack_signature_verifier/archive/0.0.5.tar.gz',  # I explain this later on
    keywords=['SLACK', 'SIGNING', 'SIGNATURE'],  # Keywords that define your package best
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package    'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License',
        # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
    ],
)
