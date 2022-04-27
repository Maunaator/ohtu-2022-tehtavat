from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or
class QueryBuilder:
    def __init__(self, *query):
        if query:
            self._query_object = And(*query)
        else:
            self._query_object = All()
    
    def build(self):
        return self._query_object

    def oneOf(self, query1, query2):
        return QueryBuilder(self._query_object, Or(query1, query2))

    def playsIn(self, team):
        return QueryBuilder(self._query_object, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._query_object, HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._query_object, HasFewerThan(value, attr))
