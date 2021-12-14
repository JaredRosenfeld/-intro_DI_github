import mysql.connector
import psycopg2
connection = mysql.connector.connect(
    host="localhost",
    user="jared",
    passwd="1234",
    database = 'RestaurantMenuManager'
)


class MenuItem:
    def __init__(self):
        pass

    def save(self, name1, price1):
        query = f"INSERT INTO MenuItem (name,price) values ('{name1}',{price1});"
        cursor.execute(query)
        connection.commit()
        print("item added succesfully ")

    def delete(self, name):
        query = f"delete from MenuItem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item deleted succesfully ")

    def update(self, name, price):
        query = f"update MenuItem set price={price} where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item updated succesfully ")

    def all(self):
        print("full data is: ")
        query = f"select*from MenuItem"
        cursor.execute(query)
        result= cursor.fetchall()
        for i in result:
            print(i)

    def get_by_name(self, name):
        query = f"select*from menuitem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        result = self.run_query(query)
        for i in result:
            print(i)
