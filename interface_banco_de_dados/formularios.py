from estilos import estilo_botao, estilo_dialogo_formulario, estilo_label_menu, estilo_main_window
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
    QFormLayout,
    QDialog,
    QDialogButtonBox,
    QSpacerItem,
    QSizePolicy
)
from PyQt6.QtGui import (
    QIcon,
    QAction,
    QFont
)
from PyQt6.QtCore import (
    Qt,
    QSize,
    pyqtSignal,
    pyqtSlot
)
import sys

class FormularioClienteInsertRead(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #query:"INSERT INTO clientes (cliente_id, nome_cliente,
        #end_residencial, email) VALUES (%s, %s, %s, %s) RETURNING id_cliente;"
        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        self.cliente_id_input = QLineEdit()
        self.cliente_id_input.setPlaceholderText("ID")
        self.cliente_id_input.setFont(fonte_input)
        self.nome_cliente_input = QLineEdit() 
        self.nome_cliente_input.setPlaceholderText("NOME")
        self.nome_cliente_input.setFont(fonte_input)
        self.end_residencial_input = QLineEdit()
        self.end_residencial_input.setPlaceholderText("ENDEREÇO")
        self.end_residencial_input.setFont(fonte_input)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("EMAIL")
        self.email_input.setFont(fonte_input)

        form_layout.addRow("ID:", self.cliente_id_input)
        form_layout.addRow("NOME:", self.nome_cliente_input)
        form_layout.addRow("ENDEREÇO:", self.end_residencial_input)
        form_layout.addRow("EMAIL:", self.email_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "cliente_id": self.cliente_id_input.text(),
            "nome_cliente": self.nome_cliente_input.text(),
            "end_residencial": self.end_residencial_input.text(),
            "email": self.email_input.text()
        }
    
class FormularioClienteUpdateDelete(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        self.cliente_id_input = QLineEdit()
        self.cliente_id_input.setPlaceholderText("ID")
        self.cliente_id_input.setFont(fonte_input)

        form_layout.addRow("ID:", self.cliente_id_input)
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
    def get_data(self):
        return self.cliente_id_input
    
class FormularioVendedoresInsertUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Vendedor (Criar/Atualizar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.matricula_input = QLineEdit()
        self.matricula_input.setPlaceholderText("MATRÍCULA")
        self.matricula_input.setFont(fonte_input)
        
        self.nome_vendedor_input = QLineEdit() 
        self.nome_vendedor_input.setPlaceholderText("NOME")
        self.nome_vendedor_input.setFont(fonte_input)
        
        self.data_admissao_input = QLineEdit()
        self.data_admissao_input.setPlaceholderText("DATA ADMISSÃO (Ex: AAAA-MM-DD)")
        self.data_admissao_input.setFont(fonte_input)
        
        self.salario_base_input = QLineEdit()
        self.salario_base_input.setPlaceholderText("SALÁRIO (Ex: 1500.00)")
        self.salario_base_input.setFont(fonte_input)
        
        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("STATUS (Ex: A)")
        self.status_input.setFont(fonte_input)
        
        self.data_desligamento_input = QLineEdit()
        self.data_desligamento_input.setPlaceholderText("DATA DESLIGAMENTO (Opcional)")
        self.data_desligamento_input.setFont(fonte_input)

        form_layout.addRow("MATRÍCULA:", self.matricula_input)
        form_layout.addRow("NOME:", self.nome_vendedor_input)
        form_layout.addRow("DATA ADMISSÃO:", self.data_admissao_input)
        form_layout.addRow("SALÁRIO BASE:", self.salario_base_input)
        form_layout.addRow("STATUS:", self.status_input)
        form_layout.addRow("DATA DESLIGAMENTO:", self.data_desligamento_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "matricula": self.matricula_input.text(),
            "nome_vendedor": self.nome_vendedor_input.text(),
            "data_admissao": self.data_admissao_input.text(),
            "salario_base": self.salario_base_input.text(),
            "status": self.status_input.text(),
            "data_desligamento": self.data_desligamento_input.text()
        }
    
    def set_data(self, dados):
        """Preenche o formulário com dados existentes (para modo Update)"""
        self.matricula_input.setText(dados.get("matricula", ""))
        self.nome_vendedor_input.setText(dados.get("nome_vendedor", ""))
        self.data_admissao_input.setText(dados.get("data_admissao", ""))
        self.salario_base_input.setText(dados.get("salario_base", ""))
        self.status_input.setText(dados.get("status", ""))
        self.data_desligamento_input.setText(dados.get("data_desligamento", ""))
        
        # Desabilita a chave primária no modo de atualização
        self.matricula_input.setEnabled(False)

class FormularioVendedoresReadDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Vendedor (Buscar/Deletar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.matricula_input = QLineEdit()
        self.matricula_input.setPlaceholderText("MATRÍCULA")
        self.matricula_input.setFont(fonte_input)

        form_layout.addRow("MATRÍCULA:", self.matricula_input)
        
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
        
    def get_data(self):
        return self.matricula_input
    
class FormularioItensInsertUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Item (Criar/Atualizar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.produto_id_input = QLineEdit()
        self.produto_id_input.setPlaceholderText("ID DO PRODUTO")
        self.produto_id_input.setFont(fonte_input)
        
        self.nome_produto_input = QLineEdit() 
        self.nome_produto_input.setPlaceholderText("NOME DO PRODUTO")
        self.nome_produto_input.setFont(fonte_input)
        
        self.marca_input = QLineEdit()
        self.marca_input.setPlaceholderText("MARCA")
        self.marca_input.setFont(fonte_input)
        
        self.tipo_input = QLineEdit()
        self.tipo_input.setPlaceholderText("TIPO (Ex: Smartphone)")
        self.tipo_input.setFont(fonte_input)
        
        self.preco_input = QLineEdit()
        self.preco_input.setPlaceholderText("PREÇO (Ex: 2500.00)")
        self.preco_input.setFont(fonte_input)
        
        self.qtd_estoque_input = QLineEdit()
        self.qtd_estoque_input.setPlaceholderText("QUANTIDADE EM ESTOQUE")
        self.qtd_estoque_input.setFont(fonte_input)

        form_layout.addRow("ID PRODUTO:", self.produto_id_input)
        form_layout.addRow("NOME:", self.nome_produto_input)
        form_layout.addRow("MARCA:", self.marca_input)
        form_layout.addRow("TIPO:", self.tipo_input)
        form_layout.addRow("PREÇO:", self.preco_input)
        form_layout.addRow("QTD ESTOQUE:", self.qtd_estoque_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "produto_id": self.produto_id_input.text(),
            "nome_produto": self.nome_produto_input.text(),
            "marca": self.marca_input.text(),
            "tipo": self.tipo_input.text(),
            "preco": self.preco_input.text(),
            "qtd_estoque": self.qtd_estoque_input.text()
        }
    
    def set_data(self, dados):
        """Preenche o formulário com dados existentes (para modo Update)"""
        self.produto_id_input.setText(dados.get("produto_id", ""))
        self.nome_produto_input.setText(dados.get("nome_produto", ""))
        self.marca_input.setText(dados.get("marca", ""))
        self.tipo_input.setText(dados.get("tipo", ""))
        self.preco_input.setText(dados.get("preco", ""))
        self.qtd_estoque_input.setText(dados.get("qtd_estoque", ""))
        
        # Desabilita a chave primária no modo de atualização
        self.produto_id_input.setEnabled(False)

class FormularioItensReadDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Item (Buscar/Deletar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.produto_id_input = QLineEdit()
        self.produto_id_input.setPlaceholderText("ID DO PRODUTO")
        self.produto_id_input.setFont(fonte_input)

        form_layout.addRow("ID PRODUTO:", self.produto_id_input)
        
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
        
    def get_data(self):
        return self.produto_id_input

class FormularioPedidosInsertUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Pedido (Criar/Atualizar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.pedido_id_input = QLineEdit()
        self.pedido_id_input.setPlaceholderText("ID DO PEDIDO")
        self.pedido_id_input.setFont(fonte_input)
        
        self.data_pedido_input = QLineEdit() 
        self.data_pedido_input.setPlaceholderText("DATA (Ex: AAAA-MM-DD)")
        self.data_pedido_input.setFont(fonte_input)
        
        self.cliente_id_input = QLineEdit()
        self.cliente_id_input.setPlaceholderText("ID DO CLIENTE")
        self.cliente_id_input.setFont(fonte_input)
        
        self.matricula_vendedor_input = QLineEdit()
        self.matricula_vendedor_input.setPlaceholderText("MATRÍCULA DO VENDEDOR")
        self.matricula_vendedor_input.setFont(fonte_input)
        
        self.status_pedido_input = QLineEdit()
        self.status_pedido_input.setPlaceholderText("STATUS (Ex: P, E, C)")
        self.status_pedido_input.setFont(fonte_input)
        
        self.end_entrega_input = QLineEdit()
        self.end_entrega_input.setPlaceholderText("ENDEREÇO DE ENTREGA")
        self.end_entrega_input.setFont(fonte_input)

        form_layout.addRow("ID PEDIDO:", self.pedido_id_input)
        form_layout.addRow("DATA PEDIDO:", self.data_pedido_input)
        form_layout.addRow("ID CLIENTE:", self.cliente_id_input)
        form_layout.addRow("MATRÍCULA VENDEDOR:", self.matricula_vendedor_input)
        form_layout.addRow("STATUS PEDIDO:", self.status_pedido_input)
        form_layout.addRow("ENDEREÇO ENTREGA:", self.end_entrega_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "pedido_id": self.pedido_id_input.text(),
            "data_pedido": self.data_pedido_input.text(),
            "cliente_id": self.cliente_id_input.text(),
            "matricula_vendedor": self.matricula_vendedor_input.text(),
            "status_pedido": self.status_pedido_input.text(),
            "end_entrega": self.end_entrega_input.text()
        }
    
    def set_data(self, dados):
        """Preenche o formulário com dados existentes (para modo Update)"""
        self.pedido_id_input.setText(dados.get("pedido_id", ""))
        self.data_pedido_input.setText(dados.get("data_pedido", ""))
        self.cliente_id_input.setText(dados.get("cliente_id", ""))
        self.matricula_vendedor_input.setText(dados.get("matricula_vendedor", ""))
        self.status_pedido_input.setText(dados.get("status_pedido", ""))
        self.end_entrega_input.setText(dados.get("end_entrega", ""))
        
        # Desabilita a chave primária no modo de atualização
        self.pedido_id_input.setEnabled(False)

class FormularioPedidosReadDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Pedido (Buscar/Deletar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.pedido_id_input = QLineEdit()
        self.pedido_id_input.setPlaceholderText("ID DO PEDIDO")
        self.pedido_id_input.setFont(fonte_input)

        form_layout.addRow("ID PEDIDO:", self.pedido_id_input)
        
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
        
    def get_data(self):
        return self.pedido_id_input

class FormularioItemPedidoInsertUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Item-Pedido (Criar/Atualizar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.id_item_pedido_input = QLineEdit()
        self.id_item_pedido_input.setPlaceholderText("ID ITEM-PEDIDO")
        self.id_item_pedido_input.setFont(fonte_input)
        
        self.id_pedido_input = QLineEdit() 
        self.id_pedido_input.setPlaceholderText("ID PEDIDO")
        self.id_pedido_input.setFont(fonte_input)
        
        self.id_produto_input = QLineEdit()
        self.id_produto_input.setPlaceholderText("ID PRODUTO")
        self.id_produto_input.setFont(fonte_input)
        
        self.qtd_pedido_input = QLineEdit()
        self.qtd_pedido_input.setPlaceholderText("QUANTIDADE")
        self.qtd_pedido_input.setFont(fonte_input)
        
        self.valor_total_input = QLineEdit()
        self.valor_total_input.setPlaceholderText("VALOR TOTAL (Ex: 3000.00)")
        self.valor_total_input.setFont(fonte_input)

        form_layout.addRow("ID ITEM-PEDIDO:", self.id_item_pedido_input)
        form_layout.addRow("ID PEDIDO:", self.id_pedido_input)
        form_layout.addRow("ID PRODUTO:", self.id_produto_input)
        form_layout.addRow("QUANTIDADE:", self.qtd_pedido_input)
        form_layout.addRow("VALOR TOTAL:", self.valor_total_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "id_item_pedido": self.id_item_pedido_input.text(),
            "id_pedido": self.id_pedido_input.text(),
            "id_produto": self.id_produto_input.text(),
            "qtd_pedido": self.qtd_pedido_input.text(),
            "valor_total": self.valor_total_input.text()
        }
    
    def set_data(self, dados):
        """Preenche o formulário com dados existentes (para modo Update)"""
        self.id_item_pedido_input.setText(dados.get("id_item_pedido", ""))
        self.id_pedido_input.setText(dados.get("id_pedido", ""))
        self.id_produto_input.setText(dados.get("id_produto", ""))
        self.qtd_pedido_input.setText(dados.get("qtd_pedido", ""))
        self.valor_total_input.setText(dados.get("valor_total", ""))
        
        # Desabilita a chave primária no modo de atualização
        self.id_item_pedido_input.setEnabled(False)

class FormularioItemPedidoReadDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Item-Pedido (Buscar/Deletar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.id_item_pedido_input = QLineEdit()
        self.id_item_pedido_input.setPlaceholderText("ID ITEM-PEDIDO")
        self.id_item_pedido_input.setFont(fonte_input)

        form_layout.addRow("ID ITEM-PEDIDO:", self.id_item_pedido_input)
        
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
        
    def get_data(self):
        return self.id_item_pedido_input

class FormularioTelefonesInsertUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Telefone (Criar/Atualizar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        #INPUT_CONFIG
        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.id_telefone_input = QLineEdit()
        self.id_telefone_input.setPlaceholderText("ID TELEFONE")
        self.id_telefone_input.setFont(fonte_input)
        
        self.cliente_id_input = QLineEdit() 
        self.cliente_id_input.setPlaceholderText("ID CLIENTE (a quem pertence)")
        self.cliente_id_input.setFont(fonte_input)
        
        self.numero_cliente_input = QLineEdit()
        self.numero_cliente_input.setPlaceholderText("NÚMERO (Ex: 21999998888)")
        self.numero_cliente_input.setFont(fonte_input)

        form_layout.addRow("ID TELEFONE:", self.id_telefone_input)
        form_layout.addRow("ID CLIENTE:", self.cliente_id_input)
        form_layout.addRow("NÚMERO:", self.numero_cliente_input)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)

        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)

    def get_data(self):
        return {
            "id_telefone": self.id_telefone_input.text(),
            "cliente_id": self.cliente_id_input.text(),
            "numero_cliente": self.numero_cliente_input.text()
        }
    
    def set_data(self, dados):
        """Preenche o formulário com dados existentes (para modo Update)"""
        self.id_telefone_input.setText(dados.get("id_telefone", ""))
        self.cliente_id_input.setText(dados.get("cliente_id", ""))
        self.numero_cliente_input.setText(dados.get("numero_cliente", ""))
        
        # Desabilita a chave primária no modo de atualização
        self.id_telefone_input.setEnabled(False)

class FormularioTelefonesReadDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulário de Telefone (Buscar/Deletar)")
        self.setStyleSheet(estilo_dialogo_formulario)
        self.setMinimumWidth(500)

        layout_principal = QVBoxLayout()
        form_layout = QFormLayout()

        fonte_input = QFont("Segoe UI", 12)
        fonte_input.setBold(True)
        
        self.id_telefone_input = QLineEdit()
        self.id_telefone_input.setPlaceholderText("ID TELEFONE")
        self.id_telefone_input.setFont(fonte_input)

        form_layout.addRow("ID TELEFONE:", self.id_telefone_input)
        
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        botoes_dialog = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botoes_dialog.setFont(fonte_botoes)
        botoes_dialog.setStyleSheet(estilo_botao)
        
        botoes_dialog.accepted.connect(self.accept)
        botoes_dialog.rejected.connect(self.reject)
        
        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(botoes_dialog)
        self.setLayout(layout_principal)
        
    def get_data(self):
        return self.id_telefone_input
































































































