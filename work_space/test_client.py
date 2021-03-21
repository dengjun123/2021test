import pymysql

db = pymysql.connect(
    host='stuq.ceshiren.com',
    user='hogwarts_python',
    password='hogwarts_python',
    db='hogwarts_python',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def test_conn():
    with db.cursor() as cursor:
        sql = 'show tables;'
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())

def test_select():
    with db.cursor() as c:
        sql = "select * from user where username=%s"
        c.execute(sql, ["dengjun123"])
        print(c.fetchall())