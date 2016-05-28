import timeit
import jaydebeapi


def test_query(statement, curs):
    start = timeit.default_timer()
    curs.execute(statement)
    stop = timeit.default_timer()
    print(stop - start)

def test_aggregate():
    statements = []

if __name__ == "__main__":
    conn = jaydebeapi.connect('org.hsqldb.jdbcDriver', ['jdbc:hsqldb:hsql://localhost/', 'SA', ''],'/home/sheep94lion/Downloads/hsqldb-2.3.3/hsqldb/lib/hsqldb.jar', )
    curs = conn.cursor()
    statement = "select count(*) from table_0"
    test_query(statement, curs)


