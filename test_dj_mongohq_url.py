# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import unittest

import dj_mongohq_url


POSTGIS_URL = 'postgis://uf07k1i6d8ia0v:wegauwhgeuioweg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722r2kuvn'


class DatabaseTestSuite(unittest.TestCase):

    def test_truth(self):
        assert True

    def test_mongodb_parsing(self):
        url = 'mongodb://heroku:wegauwhgeuioweg@linus.mongohq.com:10031/app4523234'
        url = dj_mongohq_url.parse(url)

        assert url['ENGINE'] == 'django_mongodb_engine'
        assert url['NAME'] == 'app4523234'
        assert url['HOST'] == 'linus.mongohq.com'
        assert url['USER'] == 'heroku'
        assert url['PASSWORD'] == 'wegauwhgeuioweg'
        assert url['PORT'] == 10031

    def test_empty_string_parsing(self):
        url = ''
        url = dj_mongohq_url.parse(url)

        try:
            url['ENGINE'] == None
            assert False
        except KeyError:
            assert True

        assert url['NAME'] == ''
        assert url['HOST'] == None
        assert url['USER'] == None
        assert url['PASSWORD'] == None
        assert url['PORT'] == None

    def test_invalid_type_parsing(self):
        urls = [None, 123, {0: 1}, [1, 2, 3]]

        for url in urls:
            url = dj_mongohq_url.parse(url)

            try:
                url['ENGINE'] == None
                assert False
            except KeyError:
                assert True

            assert url['NAME'] == ''
            assert url['HOST'] == None
            assert url['USER'] == None
            assert url['PASSWORD'] == None
            assert url['PORT'] == None

    def test_mongodb_url(self):
        a = dj_mongohq_url.config()
        assert not a

        os.environ['MONGOHQ_URL'] = 'mongodb://heroku:wegauwhgeuioweg@linus.mongohq.com:10031/app4523234'

        url = dj_mongohq_url.config()

        assert url['ENGINE'] == 'django_mongodb_engine'
        assert url['NAME'] == 'app4523234'
        assert url['HOST'] == 'linus.mongohq.com'
        assert url['USER'] == 'heroku'
        assert url['PASSWORD'] == 'wegauwhgeuioweg'
        assert url['PORT'] == 10031

if __name__ == '__main__':
    unittest.main()
