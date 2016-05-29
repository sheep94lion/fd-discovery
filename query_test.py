import timeit
import jaydebeapi


def test_query(statement, curs):
    start = timeit.default_timer()
    curs.execute(statement)
    stop = timeit.default_timer()
    print(stop - start)


if __name__ == "__main__":
    conn = jaydebeapi.connect('org.hsqldb.jdbcDriver', ['jdbc:hsqldb:hsql://localhost/', 'SA', ''],'/home/sheep94lion/Downloads/hsqldb-2.3.3/hsqldb/lib/hsqldb.jar', )
    curs = conn.cursor()
    statements1 = ["select max(A2) from table_10",
                    "select count(A2) from table_11",
                    "select count(A2) from table_10",
                    "select min(A7) from table_13",
                    "select min(A3) from table_14"]
    for statement in statements1:
        test_query(statement, curs)
    print("next")
    statements2 = [
        "update table_12 set A13 = 'Tsinghua University' where A14 = '1001 George Wallace Dr'",
        "update table_14 set A3 = '100018816' where A4 = 'Albi'",
        "update table_14 set A5 = 'G' where A4 = 'Albi'",
        "update table_11 set A1 = '11' where A4 = 'Butcher'",
        "update table_11 set A1 = '1' where A11 = 'FM'"
    ]
    for statement in statements2:
        test_query(statement, curs)
    print("next")
    statements3 = [
        "select A3 from (select A3, min(A7) as min_a7 from table_14 group by A3) where min_a7 < 200",
        "select max(con_a2) from (select a7, count(A2) as con_a2 from table_10 group by A7)",
        "select min(con_a2) from (select a7, count(A2) as con_a2 from table_10 group by A7)",
        "select min(max_a2) from (select a7, max(A2) as max_a2 from table_10 group by A7)",
        "select A3 from (select A3, max(A7) as max_a7 from table_14 group by A3) where max_a7 > 800"

    ]
    for statement in statements3:
        test_query(statement, curs)
    print("next")
    statements4 = [
        "select A12,A10 from table_15 where A10 like 'APO%'",
        "select A2,A9 from table_10 where A9 like '0a_'",
        "select A12,A10 from table_15 where A10 like 'Ag%'",
        "select A3,A6 from table_14 where A6 like '%B%g%'",
        "select A3, A4 from table_14 where A4 like '%ild%'"

    ]
    for statement in statements4:
        test_query(statement, curs)
    print("next")
    statements5 = ["select max(A2) from table_0",
                   "select count(A2) from table_0",
                   "select count(A2) from table_0",
                   "select min(A7) from table_0",
                   "select min(A3) from table_0"]
    for statement in statements5:
        test_query(statement, curs)
    print("next")
    statements6 = [
        "update table_0 set A13 = 'Tsinghua University' where A14 = '1001 George Wallace Dr'",
        "update table_0 set A3 = '100018816' where A4 = 'Albi'",
        "update table_0 set A5 = 'G' where A4 = 'Albi'",
        "update table_0 set A1 = '11' where A4 = 'Butcher'",
        "update table_0 set A1 = '1' where A11 = 'FM'"
    ]
    for statement in statements6:
        test_query(statement, curs)
    print("next")
    statements7 = [
        "select A3 from (select A3, min(A7) as min_a7 from table_0 group by A3) where min_a7 < 200",
        "select max(con_a2) from (select a7, count(A2) as con_a2 from table_0 group by A7)",
        "select min(con_a2) from (select a7, count(A2) as con_a2 from table_0 group by A7)",
        "select min(max_a2) from (select a7, max(A2) as max_a2 from table_0 group by A7)",
        "select A3 from (select A3, max(A7) as max_a7 from table_0 group by A3) where max_a7 > 800"

    ]
    for statement in statements7:
        test_query(statement, curs)
    print("next")
    statements8 = [
        "select A12,A10 from table_0 where A10 like 'APO%'",
        "select A2,A9 from table_0 where A9 like '0a_'",
        "select A12,A10 from table_0 where A10 like 'Ag%'",
        "select A3,A6 from table_0 where A6 like '%B%g%'",
        "select A3, A4 from table_0 where A4 like '%ild%'"

    ]
    for statement in statements8:
        test_query(statement, curs)
