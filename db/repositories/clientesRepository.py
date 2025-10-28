from db.connection import get_connection

class ClientesRepository:

    def create(self, cliente_id: int, nome_cliente: str, end_residencial: str, email: str):
        query = "INSERT INTO clientes (cliente_id, nome_cliente, end_residencial, email) VALUES (%s, %s, %s, %s) RETURNING id_cliente;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cliente_id, nome_cliente, end_residencial, email))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT * FROM clientes;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, cliente_id: int):
        query = "SELECT * FROM clientes WHERE cliente_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cliente_id,))
                return cur.fetchone()

    def update(self, cliente_id: int, nome_cliente: str, end_residencial: str, email: str):
        query = "UPDATE clientes SET nome_cliente = %s, end_residencial = %s, email = %s WHERE cliente_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (nome_cliente, end_residencial, email, cliente_id))
                conn.commit()
                return cur.rowcount

    def delete(self, cliente_id: int):
        query = "DELETE FROM clientes WHERE cliente_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cliente_id,))
                conn.commit()
                return cur.rowcount
