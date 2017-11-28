import pymysql.cursors
import configparser as cparser
import os 

# ======== Reading db_config.ini setting ===========

#base_dir = os.getcwd()
base_dir = os.path.dirname(os.path.dirname(__file__))
print(type(base_dir))
print(base_dir)
file_path = base_dir + '/db_config.ini'
print(file_path)

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf','host')
print(host)
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "dbb_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================

class DBB():
    def __init__(self):
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    
                                    db=db,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def clear(self,table_name):
        real_sql = 'delete from ' + table_name + ';'
        print(real_sql)
        self.cur.execute(real_sql)
        self.conn.commit() 

    def insert(self,table_name,table_data):
        key1 = table_data.keys()
        print(key1)
        for key in table_data:
            table_data[key]="'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        print(key)
        print(value)
        real_sql = 'insert into ' + table_name + '(' + key + ') values(' + value + ')' + ';'
        print(real_sql) 
        self.cur.execute(real_sql)
        self.conn.commit()
       

    def close(self):
         self.conn.close()

if __name__ == '__main__':
    db = DB()
    db.clear(table_name)
    db.insert(table_name,data)
    db.close()
