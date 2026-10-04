import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def find_all():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("select id,name,price from product")
    rows = cursor.fetchall()
    products = []

    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        }

        products.append(product)
    cursor.close()
    connect.close()
    return rows


def find_by_id(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, price FROM product WHERE id = %s",
        (product_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "price": float(row[2])
    }


def save(product):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO product (name, price)
            VALUES (%s, %s)
            RETURNING id, name, price
            """,
            (product["name"], product["price"])
        )

        row = cursor.fetchone()

        connection.commit()

        

        return {
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        }
    except Exception as error:
        if connection:
            connection.rollback()

        print("Database error:", error)
        return None

    finally:
        if connection:
            connection.close()
    

def update(product_id, product):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE product
        SET name = %s,
            price = %s
        WHERE id = %s
        RETURNING id, name, price
        """,
        (
            product["name"],
            product["price"],
            product_id
        )
    )

    row = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "price": float(row[2])
    }

def patch(product_id,updated_data):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, price FROM product WHERE id = %s",
        (product_id,)
    )
    row = cursor.fetchone()
    if row is None :
        cursor.close()
        connection.close()  
        return None
    name = updated_data.get("name",row[1])
    price = updated_data.get("price",row[2])
    cursor.execute(
        """
        UPDATE product
        SET name = %s,
            price = %s
        WHERE id = %s
        RETURNING id, name, price
        """,
        (name, price, product_id)
    )

    updated_row = cursor.fetchone()
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "id": updated_row[0],
        "name": updated_row[1],
        "price": float(updated_row[2])
    }

def delete(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM product
        WHERE id = %s
        RETURNING id, name, price
        """,
        (product_id,)
    )

    row = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "price": float(row[2])
    }