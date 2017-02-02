import mysql.connector
from mysql.connector import errorcode


def connect():
    config = {
        'user': 'root',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'dade_test',
        'raise_on_warnings': True,
    }
    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx


def query_data(cnx):
    cursor = cnx.cursor()
    query = ("SELECT *  FROM products")
    cursor.execute(query)
    for result in cursor:
        print result
    cursor.close()


def insert_data(cnx):
    cursor = cnx.cursor()
    add_product = ("INSERT INTO products"
                   "(product_id, product_name, product_description, product_location, product_quantity)"
                   "VALUES (%d, %s, %s, %s, %d)")
    product = (None, 'Masks', 'make faces more beautiful', 'Toronto', 14)
    cursor.execute(add_product, product)
    cursor.close()


if __name__ == '__main__':
    cnx = connect()
    # insert_data(cnx)
    query_data(cnx)
    cnx.commit()
    cnx.close()
