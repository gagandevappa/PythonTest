import pymysql
#pymysql.install_as_MySQLdb()
conn=pymysql.connect(host='192.168.45.2', port=31840, user='root', password='', db='gagan')
c=conn.cursor()
c.execute("""CREATE TABLE employee (
            first varchar(30) NOT NULL,
            id int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY)""")

c.execute("INSERT INTO employee(first) VALUES('Gagan')")
conn.commit()