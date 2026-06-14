def search_products(keyword):
    query = "SELECT * FROM products WHERE name LIKE '%" + keyword + "%'"
    cursor.execute(query)
