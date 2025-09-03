

def dictValuePad(key):
    return "\"" + str(key) + "\""

def make_insert_query(table, dict):
    sql = 'INSERT INTO ' + table
    sql += ' ('
    sql += ', '.join(dict)
    sql += ') VALUES ('
    sql += ', '.join(map(dictValuePad, dict.values()))
    sql += ');'

    return sql


def make_insert_query(table, dict):
    sql = 'INSERT INTO ' + table
    sql += ' ('
    sql += ', '.join(dict)
    sql += ') VALUES ('
    sql += ', '.join(map(dictValuePad, dict.values()))
    sql += ');'

    return sql


def make_select_query(target_date):
    return 'SELECT ' \
           '    id, user_id  ' \
           'FROM ' \
           '    user_live ' \
           'WHERE ' \
           '    role = "buyer" AND id like "%s" order by id;' \
        % (target_date)