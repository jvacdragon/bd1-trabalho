from db.connection import get_connection

class TelefoneRepository:

    def create(self, id_telefone: int, cliente_id: int, numero_cliente: str):
        query = "INSERT INTO telefones (id_telefone, cliente_id, numero_cliente) VALUES (%s, %s, %s) RETURNING id_telefone;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_telefone, cliente_id, numero_cliente))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT * FROM telefones;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, id_telefone: int):
        query = "SELECT * FROM telefones WHERE id_telefone = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_telefone))
                return cur.fetchone()

    def update(self, id_telefone: int, cliente_id: int, numero_cliente: str):
        query = "UPDATE telefones SET cliente_id = %s, numero_cliente = %s WHERE id_telefone = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cliente_id, numero_cliente, id_telefone))
                conn.commit()
                return cur.rowcount

    def delete(self, id_telefone: int):
        query = "DELETE FROM telefones WHERE id_telefone = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id_telefone,))
                conn.commit()
                return cur.rowcount
