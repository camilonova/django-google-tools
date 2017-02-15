from setuptools import setup, find_packages


setup(
    name='django-google-tools',
    version='1.1.0',
    description='Django app for managing Google Analytics and Site Verification codes.',
    keywords='django, analytics, google analytics, verification code, site verification',
    author='Orne Brocaar, Camilo Nova',
    author_email='camilo.nova@gmail.com',
    url='http://github.com/camilonova/django-google-tools',
    license='MIT',
    include_package_data=True,
    packages=find_packages(
        exclude=[
            'googletools.tests',
        ]
    ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
