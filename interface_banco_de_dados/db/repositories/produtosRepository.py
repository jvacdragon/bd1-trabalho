from db.connection import get_connection

class ProdutosRepository:

    def create(self, produto_id: int, nome_produto: str, marca: str, tipo: str, preco: int, qtd_estoque: int):
        query = "INSERT INTO produtos (produto_id, nome_produto, marca, tipo, preco, qtd_estoque) VALUES (%s, %s, %s, %s, %s, %s) RETURNING produto_id;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (produto_id, nome_produto, marca, tipo, preco*100, qtd_estoque))
                novo_id = cur.fetchone()[0]
                conn.commit()
                return novo_id

    def read_all(self):
        query = "SELECT produto_id, nome_produto, marca, tipo, preco/100, qtd_estoque  FROM produtos;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                return rows

    def read_by_id(self, produto_id: int):
        query = "SELECT produto_id, nome_produto, marca, tipo, preco/100, qtd_estoque FROM produtos WHERE produto_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (produto_id,))
                return cur.fetchone()

    def update(self, produto_id: int, nome_produto: str, marca: str, tipo: str, preco: float, qtd_estoque: int):
        query = "UPDATE produtos SET nome_produto = %s, marca = %s, tipo = %s, preco = %s, qtd_estoque = %s WHERE produto_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (nome_produto, marca, tipo, preco*100, qtd_estoque, produto_id))
                conn.commit()
                return cur.rowcount

    def delete(self, produto_id: int):
        query = "DELETE FROM produtos WHERE produto_id = %s;"
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (produto_id,))
                conn.commit()
                return cur.rowcount
