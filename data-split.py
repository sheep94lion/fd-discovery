from thirdnf_split import *
import jaydebeapi


def split_data(file_data, schemas, prefix):
    conn = jaydebeapi.connect('org.hsqldb.jdbcDriver', ['jdbc:hsqldb:hsql://localhost/', 'SA', ''],'/home/sheep94lion/Downloads/hsqldb-2.3.3/hsqldb/lib/hsqldb.jar',)
    curs = conn.cursor()
    for i, s in enumerate(schemas):
        statement = get_create_table_statement(s, i, prefix)
        print(statement)
        curs.execute(statement)
    for tuple_data in file_data:
        for i, schema in enumerate(schemas):
            split_tuple = get_split_tuple(tuple_data, schema)
            statement = get_insert_statement(i, split_tuple)
            print (statement)
            try:
                curs.execute(statement)
            except:
                pass



def get_split_tuple(tuple_data, schema):
    split_tuple = []
    for i in schema:
        split_tuple.append(tuple_data[i])
    return split_tuple


def get_create_table_statement(s, i, prefix):
    statement = "CREATE TABLE table_" + prefix + str(i) + "("
    st_key = ""
    for a in s:
        st_part = "A"+str(a)+" varchar(50)"+","
        statement += st_part
    for a in s:
        st_key += "A" + str(a) + ","
    st_key = st_key[:-1]
    statement += "PRIMARY KEY ("
    statement += st_key
    statement += "))"
    return statement


def get_insert_statement(i_table, tuple):
    statement = "INSERT INTO table_"+str(i_table)+" VALUES("
    st_part = "','".join(tuple)
    statement = statement + "'" + st_part + "');"
    print (statement)
    return statement

if __name__ == '__main__':
    file_data = read_file()
    schemas = bcnf_generate_input()
    #schemas = [[12, 11, 4, 5], [1, 2, 12, 9], [8, 11, 12], [2, 11, 4, 12], [11, 12, 5, 6], [9, 12, 6], [1, 2, 3]]
    print(schemas)
    #split_data(file_data, schemas, "0")
