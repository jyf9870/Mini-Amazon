"""
This file is used to populate the database that is created by Django.
"""


import db_utils

conn, cursor = db_utils.connect_db()

# clear all tables
query = f"""
    TRUNCATE  
    mini_amazon_stock, 
    mini_amazon_order, 
    mini_amazon_product
    CASCADE;
    DELETE FROM mini_amazon_warehouse;
"""
db_utils.execute_and_commit(query, conn, cursor)

# create some products
query = f"""
    INSERT INTO mini_amazon_product(pid, description, catalog, pic, price)
    VALUES
    (1, 'Vice', 2, 'images/glove_1.png', 100),
    (2, 'Marble Fade', 2, 'images/glove_2.png', 200),
    (3, 'Pow', 2, 'images/glove_3.png', 300),
    (4, 'Snow Leopard', 2, 'images/glove_4.png', 400),
    (5, 'Talon Knife', 1, 'images/knife_1.png', 500),
    (6, 'Flip Knife', 1, 'images/knife_2.png', 600),
    (7, 'Gold Arabesque', 3, 'images/gun_1.png', 700),
    (8, 'Ocean Drive', 3, 'images/gun_2.png', 800);
"""
db_utils.execute_and_commit(query, conn, cursor)

# create some warehouses
query = f"""
    INSERT INTO mini_amazon_warehouse(whid, x, y)
    VALUES
    (0, 0, 0),
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3);
"""
db_utils.execute_and_commit(query, conn, cursor)

# create some stock
# query = f"""
#     SELECT mini_amazon_warehouse.whid AS warehouse_id
#     FROM mini_amazon_warehouse
# """
# cursor.execute(query)
# rows = cursor.fetchall()
# for warehouse_id in rows:
#     query = f"""
#         INSERT INTO mini_amazon_stock(pid, count, worldid, whid)
#         VALUES
#         (1, 1, 1, {warehouse_id[0]}),
#         (2, 1, 1, {warehouse_id[0]}),
#         (3, 1, 1, {warehouse_id[0]}),
#         (4, 1, 1, {warehouse_id[0]}),
#         (5, 1, 1, {warehouse_id[0]}),
#         (6, 1, 1, {warehouse_id[0]}),
#         (7, 1, 1, {warehouse_id[0]}),
#         (8, 1, 1, {warehouse_id[0]});
#     """
#     db_utils.execute_and_commit(query, conn, cursor)

query = f"""
        INSERT INTO mini_amazon_stock(pid, count, worldid, whid)
        VALUES
        (1, 1, 1, 0),
        (2, 1, 1, 0),
        (3, 1, 1, 0),
        (4, 1, 1, 0),
        (5, 1, 1, 0),
        (6, 1, 1, 0),
        (7, 1, 1, 0),
        (8, 1, 1, 0);
    """
db_utils.execute_and_commit(query, conn, cursor)


cursor.close()
