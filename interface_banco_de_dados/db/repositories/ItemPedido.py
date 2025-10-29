from db.connection import get_connection

class ItemPedidoRepository:

    def create(self, id_item_pedido: int, id_pedido: int, id_produto: int, qtd_pedido: int, valor_total: int):
        query = "INSERT INTO item_pedido (id_item_pedido, id_pedido, id_produto, qtd_pedido, valor_total) VALUES (%s, %s, %s, %s, %s) RETURNING id_item_pedido;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_item_pedido, id_pedido, id_produto, qtd_pedido, valor_total*100))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT id_item_pedido, id_pedido, id_produto, qtd_pedido, valor_total/100 FROM item_pedido;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, id_item_pedido: int):
        query = "SELECT id_item_pedido, id_pedido, id_produto, qtd_pedido, valor_total/100 FROM item_pedido WHERE id_item_pedido = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_item_pedido,))
                return cur.fetchone()

    def update(self, id_item_pedido: int, id_pedido: int, id_produto: int, qtd_pedido: int, valor_total: int):
        query = "UPDATE item_pedido SET id_pedido = %s, id_produto = %s, qtd_pedido = %s, valor_total = %s WHERE id_item_pedido = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_pedido, id_produto, qtd_pedido, valor_total*100, id_item_pedido))
                conn.commit()
                return cur.rowcount

    def delete(self, id_item_pedido: int):
        query = "DELETE FROM item_pedido WHERE id_item_pedido = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_item_pedido,))
                conn.commit()
                return cur.rowcount
