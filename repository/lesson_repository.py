import sqlite3

def save(title, teacher, class_number, unit):
    connection = sqlite3.connect('./repository/university.db')
    cursor = connection.cursor()
    cursor.execute("insert into lessons (title,teacher,class_number,unit) values  (?,?,?,?)",
                   [title,teacher,class_number,unit])
    connection.commit()
    cursor.close()
    connection.close()


def edit(code,title, teacher, class_number, unit):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("update lessons set title=? ,teacher=? ,class_number=? ,unit=? where code=?",
                   [title, teacher, class_number, unit,code])
    connection.commit()
    cursor.close()
    connection.close()


def remove(code):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("delete from lessons where code = ?",
                   [code])
    connection.commit()
    cursor.close()
    connection.close()


def find_all():
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons")
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list


def find_by_code(code):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where code = ?",[code])
    product = cursor.fetchone()
    cursor.close()
    connection.close()
    return product


def find_by_title(title):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where title like ?",[title+"%"])
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list


def find_by_teacher(teacher):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where teacher like ?",[teacher+"%"])
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list


def find_by_class_number(class_number):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where class_number like ?",[class_number+"%"])
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list


def find_by_unit_range(start_unit, end_unit):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where unit between ? and ?",[start_unit,end_unit])
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list

def find_by_title_and_teacher(title,teacher):
    connection = sqlite3.connect('repository/university.db')
    cursor = connection.cursor()
    cursor.execute("select * from lessons where title like ? and teacher like ?", [title+"%", teacher + "%"])
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return product_list