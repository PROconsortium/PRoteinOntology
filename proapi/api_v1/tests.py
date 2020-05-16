from django.test import TestCase

# Create your tests here.

from .sparql import SparqlSearch

class SparlSearchTests(TestCase):

    def test_sparql_query_ok(self):
        """
        Test query against sparql endpoint
        :return: 200: OK
        """
        ss = SparqlSearch()
        query = "select ?s, ?p, ?o where {?s ?p ?o .} limit 2"
        result, error = ss.executeQuery(query)
        self.assertEqual(error, None)

    def test_sparql_query_notok(self):
        """
        Test query against sparql endpoint
        :return: 400 and error message
        """
        ss = SparqlSearch()
        query = "select ?s, ?p, ?o here {?s ?p ?o .} limit 2"
        result, error = ss.executeQuery(query)
        # print(error.code)
        # print(error.message)
        self.assertNotEqual(error.code, 200)