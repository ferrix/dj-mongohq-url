dj-mongohq-url
~~~~~~~~~~~~~~~

.. image:: https://secure.travis-ci.org/ferrix/dj-mongohq-url.png?branch=master

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``MONGOURL_URL`` environment variable to configure your Django application.

This is a slight adaptation of the dj-database-url_ by Kenneth Reitz. It is
compatible with django-nonrel_ and can be used to dig up the URL setting for
other purposes as well.

.. _dj-database-url: http://github.com/kennethreitz/dj-database-url/
.. _django-nonrel: https://github.com/django-nonrel/mongodb-engine/

Usage
-----

Configure your database in ``settings.py`` from ``DATABASE_URL`` 
(``default`` is optional)::

    DATABASES = {'default': dj_mongohq_url.config(default='mongodb://...')}

Parse an arbitrary Database URL::

    DATABASES = {'default': dj_mongohq_url.parse('mongodb://...')}

If you are not using Django with nonrel capabilities and merely want to
dig up the MongoDB settings, use another variable::

    MONGODB = dj_mongohq_url.config()

Supported databases
-------------------

Support currently exists for MongoDB.

Installation
------------

Installation is simple too::

    $ pip install dj-mongohq-url
