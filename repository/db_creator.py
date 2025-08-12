import sqlite3


def create_database():
    connection = sqlite3.connect('./repository/university.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        create table lessons(
            code integer primary key autoincrement,
            title text not null,
            teacher text not null,
            class_number text not null,
            unit integer not null default 1
        )
        """
    )
    cursor.execute(
        """
        create table students(
            code integer primary key autoincrement,
            name text not null,
            family text not null,
            birth_date text not null,
            phone text not null
        )
        """
    )
    connection.commit()
    connection.close()