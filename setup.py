from setuptools import setup, find_packages

from setuptools_scm import get_version

setup(
    name='django-admin-dashboard',
    version=get_version(),
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools-scm'],
    include_package_data=True,
    install_requires=[],
    description='A modern django dashboard built with daisyui',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://https://github.com/nsgorlew/django-admin-dashboard',
    author='Nicholas Gorlewski',
    author_email='nicholas.gorlewski@teknikoyazilimcozumleri.com',
    license='Proprietary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Proprietary Software License',
        'Operating System :: OS Independent',
    ],
)
