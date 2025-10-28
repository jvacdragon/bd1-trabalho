from db.connection import get_connection

class VendedoresRepository:

    def create(self, matricula: int, nome_vendedor: str, data_admissao: str, salario_base: float, status: str, data_desligamento: str = None):
        query = "INSERT INTO vendedores (matricula, nome_vendedor, data_admissao, salario_base, status, data_desligamento) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_vendedor;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (matricula, nome_vendedor, data_admissao, salario_base, status, data_desligamento))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT * FROM vendedores;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, matricula: int):
        query = "SELECT * FROM vendedores WHERE matricula = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (matricula,))
                return cur.fetchone()

    def update(self, matricula: int, nome_vendedor: str, data_admissao: str, salario_base: float, status: str, data_desligamento: str = None):
        query = "UPDATE vendedores SET matricula = %s, nome_vendedor = %s, data_admissao = %s, salario_base = %s, status = %s, data_desligamento = %s WHERE matricula = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (matricula, nome_vendedor, data_admissao, salario_base, status, data_desligamento, matricula))
                conn.commit()
                return cur.rowcount

    def delete(self, matricula: int):
        query = "DELETE FROM vendedores WHERE matricula = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (matricula,))
                conn.commit()
                return cur.rowcount
