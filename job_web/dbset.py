import sqlite3

def create_table(conn, sql='', choice="0"):
    if sql == '':
        switcher = {
            "1" : '''CREATE TABLE company(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                password    varchar(30)     NOT NULL,
                created_at  date            NOT NULL,
                updated_at  date            NOT NULL,
                email       varchar(30)     NOT NULL,
                is_enable   int             NOT NULL,
                name        text            NOT NULL,
                website     text            DEFAULT NONE,
                address     text            DEFAULT NONE,
                logo        blob            NOT NULL,
                role        varchar(30)     NOT NULL,
                finance_stage   varchar(30) DEFAULT NONE,
                field       varchar(30)     DEFAULT NONE,
                description text            DEFAULT NONE,
                details     text            DEFAULT NONE);''' ,
            "2" : '''CREATE TABLE job(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at  date            NOT NULL,
                updated_at  date            NOT NULL,
                company_id  int             DEFAULT NONE,
                treatment   text            NOT NULL,
                name        text            NOT NULL,
                exp         text            NOT NULL,
                education   text            NOT NULL,
                city        varchar(30)     NOT NULL,
                tags        text            NOT NULL,
                salary_min  int             NOT NULL,
                salary_max  int             NOT NULL,
                is_enable   int             NOT NULL,
                description text            NOT NULL);''',
            "3" : '''CREATE TABLE user(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                password    varchar(30)     NOT NULL,
                created_at  date            NOT NULL,
                updated_at  date            NOT NULL,
                email       text            NOT NULL,
                name        text            NOT NULL,
                resume      text            DEFAULT NONE,
                role        varchar(30)     NOT NULL,
                is_enable   int             NOT NULL);''',
            "4" : '''CREATE TABLE zhaopintb(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        varchar(250)    NOT NULL,
                co_name     varchar(250)    NOT NULL,
                area        varchar(250)    NOT NULL,
                salary      varchar(250)    DEFAULT NULL,
                exp         varchar(250)    NOT NULL,
                edu         varchar(250)    DEFAULT NULL,
                num         varchar(250)    NOT NULL,
                time        varchar(250)    NOT NULL,
                welfare     varchar(250)    DEFAULT NULL,
                info        text            NOT NULL,
                local       varchar(250)    NOT NULL,
                co_url      varchar(250)    NOT NULL,
                co_type     varchar(250)    NOT NULL,
                spider_name varchar(250)    NOT NULL,
                UNIQUE (name, co_name, spider_name) ON CONFLICT REPLACE);''',
        }
        sql = switcher.get(choice,"nothing")
        
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

def select_table(conn, sql=''):
    if sql == '':
        sql = '''SELECT * FROM company;'''
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

def delete_table(conn, sql='', choice="0"):
    if sql == '':
        switcher = {
            "1" : '''DROP TABLE company''',
            "2" : '''DROP TABLE job''',
            "3" : '''DROP TABLE user''',
            "4" : '''DROP TABLE jobs'''
        }
        sql = switcher.get(choice,"nothing")
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

def get_all_table(conn):
    sql = '''SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;'''
    c = conn.cursor()
    cursor = c.execute(sql)
    for row in cursor:
        print(row[0])
    conn.commit()

def insert_into_table(conn,sql='',choice="0"):
    if sql == '':
        switcher = {
            "1" : '''INSERT INTO job()'''
        }
        pass
    c = conn.cursor()
    cursor = c.execute(sql)
    conn.commit()

if __name__ == "__main__":
    db = sqlite3.connect('./job_web/jobs')
    create_table(db, choice="1")
    create_table(db, choice="2")
    create_table(db, choice="3")
    get_all_table(db)
    db.close()
