from db.connection import get_connection

class PedidosRepository:

    def create(self, pedido_id: int, data_pedido: int, cliente_id: float, matricula_vendedor: int, status_pedido: str, end_entrega: str):
        query = "INSERT INTO pedidos (pedido_id, data_pedido, cliente_id, matricula_vendedor, status_pedido, end_entrega) VALUES (%s, %s, %s, %s, %s, %s) RETURNING pedido_id;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pedido_id, data_pedido, cliente_id, matricula_vendedor, status_pedido, end_entrega))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT * FROM pedidos;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, pedido_id: int):
        query = "SELECT * FROM pedidos WHERE pedido_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pedido_id,))
                return cur.fetchone()

    def update(self, pedido_id: int, data_pedido: int, cliente_id: float, matricula_vendedor: int, status_pedido: str, end_entrega: str):
        query = "UPDATE pedidos SET data_pedido = %s, cliente_id = %s, matricula_vendedor = %s, status_pedido = %s, end_entrega = %s WHERE pedido_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (data_pedido, cliente_id, matricula_vendedor, status_pedido, end_entrega, pedido_id))
                conn.commit()
                return cur.rowcount

    def delete(self, pedido_id: int):
        query = "DELETE FROM pedidos WHERE pedido_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pedido_id,))
                conn.commit()
                return cur.rowcount
