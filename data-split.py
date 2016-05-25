from fd_discovery import *
import jaydebeapi


def split_data(file_data, schemas):
    conn = jaydebeapi.connect('org.hsqldb.jdbcDriver',['jdbc:hsqldb:hsql://localhost/','SA',''],'/home/sheep94lion/Downloads/hsqldb-2.3.3/hsqldb/lib/hsqldb.jar',)
    curs = conn.cursor()
    for i, s in enumerate(schemas):
        statement = get_create_table_statement(s, i)
        print(statement)
        curs.execute(statement)
    for tuple_data in file_data:
        for i, schema in enumerate(schemas):
            split_tuple = get_split_tuple(tuple_data, schema)
            statement = get_insert_statement(i, split_tuple)
            print (statement)
            curs.execute(statement)


def get_split_tuple(tuple_data, schema):
    split_tuple = []
    for i in schema:
        split_tuple.append(tuple_data[i])
    return split_tuple


def get_create_table_statement(s, i):
    statement = "CREATE TABLE table_"+str(i)+"("
    for a in s:
        st_part = "A"+str(a)+" varchar(50)"+","
        statement += st_part
    statement = statement[:-1]
    statement += ");"
    return statement


def get_insert_statement(i_table, tuple):
    statement = "INSERT INTO table_"+str(i_table)+" VALUES("
    st_part = ",".join(tuple)
    statement = statement + st_part + ");"
    print (statement)
    return statement

if __name__ == '__main__':
    file_data = read_file()
    split_data(file_data, [[1, 2, 3], [1, 4, 5]])
