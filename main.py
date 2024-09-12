import sqlite3

def test_db_query():
    try:
        sql_con = sqlite3.connect("my_test.db")
        cursor = sql_con.cursor()

        # with open("create_table.txt") as fh:
        # with open("insert_data.txt") as fh:
        with open("select_data.txt") as fh:
            query = fh.read()

        cursor.execute(query)
        students = cursor.fetchall()
        for student in students:
            print(f"{student = }")

        cursor.close()
        # print("Дані успішно записано.")

    except sqlite3.Error as error:
        print("Виникла помилка:", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершено.")


def insert_data(first_name: str, last_name: str, age: int = None, grade: int = None):
    try:
        sql_con = sqlite3.connect("my_test.db")
        cursor = sql_con.cursor()

        query = "INSERT INTO Students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)"
        data = (first_name, last_name, age, grade)

        cursor.execute(query, data)
        sql_con.commit()
        cursor.close()
        print("Дані успішно записано.")

    except sqlite3.Error as error:
        print("Помилка: ", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Підключення до бази даних закрите.")


insert_data("Дмитро", "Волощенко", 15, 100)
insert_data("Олександр", "Федченко", 16, 100)
insert_data("Абабагаламага", "Абабагаламага"[::-1], grade=1)