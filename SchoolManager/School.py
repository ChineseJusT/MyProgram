import pymysql

class School(object):
    def __init__(self, localhost, user, passwd, database):
        self.__localhost = localhost
        self.__user = user
        self.__passwd = passwd
        self.__database = database

    def add_table_student_info(self):
        sql = '''
        CREATE TABLE student_info(
            id integer auto_increment unique,
            student_no VARCHAR(32) primary key NOT NULL,
            student_name VARCHAR(32) NOT NULL ,
            photo MEDIUMBLOB NOT NULL,
            student_tel_one VARCHAR(13) NOT NULL,
            student_tel_two VARCHAR(13) NOT NULL,
            id_card VARCHAR(32) NOT NULL,
            address_now VARCHAR(64) NOT NULL,
            sex ENUM('0','1') NOT NULL,
            student_type VARCHAR(64) NOT NULL,
            marriage VARCHAR(32) NOT NULL,
            origin_of_student VARCHAR(128) NOT NULL,
            speciality VARCHAR(128),
            political ENUM('0','1','2') NOT NULL,
            natives VARCHAR(32) NOT NULL,
            student_status ENUM('0','1','2','3','4','5','6','7') NOT NULL,
            student_remarks VARCHAR(64) DEFAULT NULL ,
            remarks_one VARCHAR(64) DEFAULT NULL ,
            remarks_two VARCHAR(64) DEFAULT NULL ,
            remarks_three VARCHAR(64) DEFAULT NULL ,
            remarks_four VARCHAR(64) DEFAULT NULL ,
            remarks_five VARCHAR(64) DEFAULT NULL 
                ) ENGINE = InnoDB DEFAULT CHARSET=UTF8'''
        return self.execute_sql(sql)

    def add_table_teacher_info(self):
        sql = '''
        CREATE TABLE teacher_info(
            ID INT NOT NULL AUTO_INCREMENT UNIQUE,
            teacher_no VARCHAR(32) PRIMARY KEY NOT NULL,
            teacher_name VARCHAR(32) NOT NULL ,
            teacher_status ENUM('0', '1', '2', '3', '4', '5') DEFAULT '1' NOT NULL,
            political ENUM('0', '1', '2') DEFAULT '1' NOT NULL,
            natives VARCHAR(32) NOT NULL,
            address_now VARCHAR(32) NOT NULL,
            marriage VARCHAR(32) NOT NULL,
            speciality VARCHAR(64) DEFAULT NULL ,
            teacher_rem_one VARCHAR(128) DEFAULT NULL ,
            teacher_rem_two VARCHAR(128) DEFAULT NULL ,
            teacher_rem_three VARCHAR(128) DEFAULT NULL ,
            teacher_rem_four VARCHAR(128) DEFAULT NULL ,
            teacher_rem_five VARCHAR(128) DEFAULT NULL )
            ENGINE = InnoDB DEFAULT CHARSET=UTF8
        '''
        self.execute_sql(sql)

    def execute_sql(self, sql):
        self.conn = pymysql.connect(
            self.__localhost,
            self.__user,
            self.__passwd,
            self.__database)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            self.conn.rollback()
            result = e
        else:
            self.conn.commit()
            result = cursor.fetchall()
        finally:
            cursor.close()
            self.conn.close()
        return result

    def execute_sql_many(self, sql, lst):
        self.conn = pymysql.connect(
            self.__localhost,
            self.__user,
            self.__passwd,
            self.__database)
        cursor = self.conn.cursor()
        try:
            cursor.executemany(sql, lst)
        except Exception as e:
            self.conn.rollback()
            result = e
        else:
            self.conn.commit()
            result = cursor.fetchall()
        finally:
            cursor.close()
            self.conn.close()
        return result


if __name__ == '__main__':
    db = School('localhost', 'root', 'yx123456', 'School')
    db.add_table_student_info()
    db.add_table_teacher_info()