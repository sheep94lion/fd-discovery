import timeit
import jaydebeapi


def test_query(statement, curs):
    start = timeit.default_timer()
    curs.execute(statement)
    stop = timeit.default_timer()
    print(stop - start)

def test_aggregate(curs):
    statement = "select count(A13) from table_12"
    test_query(statement, curs)

if __name__ == "__main__":
    conn = jaydebeapi.connect('org.hsqldb.jdbcDriver', ['jdbc:hsqldb:hsql://localhost/', 'SA', ''],'/home/sheep94lion/Downloads/hsqldb-2.3.3/hsqldb/lib/hsqldb.jar', )
    curs = conn.cursor()
    test_aggregate(curs)

