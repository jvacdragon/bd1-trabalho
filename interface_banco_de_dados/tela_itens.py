from tela_base import Tela
from estilos import estilo_botao, estilo_dialogo_formulario, estilo_label_menu, estilo_main_window, estilo_tabela
from formularios import FormularioItensInsertUpdate, FormularioItensReadDelete
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
    QHeaderView,
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
from db.repositories.produtosRepository import ProdutosRepository
import sys


class TelaItens(Tela):
    def __init__(self, parent=None):
        super().__init__("PAINEL - Itens", parent)
        self.p = ProdutosRepository()
        self.table = QTableWidget()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.table, 3)
        colunas = ["ID", "NOME", "MARCA", "TIPO", "PREÇO", "QUANTIDADE"]
        

        #BOTOES_CONFIG
        layout_botoes =  QVBoxLayout()
        conteiner_botoes = QWidget()
        conteiner_botoes.setMaximumWidth(600)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)

        self.botao_create_item = QPushButton("Criar Item")
        self.botao_create_item.setFont(fonte_botoes)
        self.botao_create_item.setStyleSheet(estilo_botao)
        self.botao_create_item.clicked.connect(self.abrir_dialog_create)

        self.botao_read_item = QPushButton("Buscar Item")
        self.botao_read_item.setFont(fonte_botoes)
        self.botao_read_item.setStyleSheet(estilo_botao)
        self.botao_read_item.clicked.connect(self.abrir_dialog_read)

        self.botao_update_item = QPushButton("Atualizar Item")
        self.botao_update_item.setFont(fonte_botoes)
        self.botao_update_item.setStyleSheet(estilo_botao)
        self.botao_update_item.clicked.connect(self.abrir_dialog_update)

        self.botao_delete_item = QPushButton("Deletar Item")
        self.botao_delete_item.setFont(fonte_botoes)
        self.botao_delete_item.setStyleSheet(estilo_botao)
        self.botao_delete_item.clicked.connect(self.abrir_dialog_delete)

        layout_botoes.addWidget(self.botao_create_item)
        layout_botoes.addWidget(self.botao_read_item)
        layout_botoes.addWidget(self.botao_update_item)
        layout_botoes.addWidget(self.botao_delete_item)
        conteiner_botoes.setLayout(layout_botoes)
        
        self.layout_horizontal.addWidget(conteiner_botoes, 1)
        self.layout_conteudo.addLayout(self.layout_horizontal)
        self.atualizar_tabela(self.p, self.table, colunas)
    
    def atualizar_tabela(self, c : ProdutosRepository, table : QTableWidget, columns):
        fonte_table = QFont("Segoe UI", 12)
        fonte_table.setBold(True)
        table.setFont(fonte_table)
        table.setStyleSheet(estilo_tabela)
        colunas = columns
        self.table.setColumnCount(len(colunas))
        self.table.setHorizontalHeaderLabels(colunas)
        self.table.setRowCount(0)
        try:
            all = c.read_all()
            if all:
                for i, obj in enumerate(all):
                    self.table.insertRow(i)

                    id = QTableWidgetItem(str(obj['produto_id']))
                    nome = QTableWidgetItem(str(obj['nome_produto']))
                    marca = QTableWidgetItem(str(obj['marca']))
                    tipo = QTableWidgetItem(str(obj['tipo']))
                    preco = QTableWidgetItem(str(obj['preco']))
                    qtd = QTableWidgetItem(str(obj['qtd_estoque']))

                    self.table.setItem(i, 0, id)
                    self.table.setItem(i, 1, nome)
                    self.table.setItem(i, 2, marca)
                    self.table.setItem(i, 3, tipo)
                    self.table.setItem(i, 4, preco)
                    self.table.setItem(i, 5, qtd)
                    self.table.resizeColumnsToContents()
            

                    if len(self.colunas_tabela) >= 4:
                        self.table.horizontalHeader().setStretchLastSection(True)
                    else:
                        self.table.horizontalHeader().setStretchLastSection(False)
                        self.table.horizontalHeader().setSectionResizeMode(
                            QHeaderView.ResizeMode.ResizeToContents
                        )
        except Exception as e:
            print(f"ERRO ao atualizar tabela: {e}")
            QMessageBox.critical(self, "Erro de Banco de Dados", 
                                 f"Não foi possível carregar os clientes: {e}")

    @pyqtSlot()
    def abrir_dialog_create(self):

        dialogo = FormularioItensInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_produto = dados['produto_id']
            nome_produto = dados['nome_produto']
            marca_produto = dados['marca']
            tipo_produto = dados['tipo']
            preco_produto = dados['preco']
            qtd_estoque_produto = dados['qtd_estoque']
            print(f"Salvando: {dados}")
            self.p.create(id_produto, nome_produto, marca_produto, tipo_produto,
                          preco_produto, qtd_estoque_produto)

    @pyqtSlot()
    def abrir_dialog_read(self):

        dialogo = FormularioItensReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_buscado = dialogo.get_data().text()
            print(f"Id buscado: {id_buscado}")
            read = self.p.read_by_id(id_buscado)
            print(read)

    @pyqtSlot()
    def abrir_dialog_update(self):

        dialogo = FormularioItensInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_produto = dados['produto_id']
            nome_produto = dados['nome_produto']
            marca_produto = dados['marca']
            tipo_produto = dados['tipo']
            preco_produto = dados['preco']
            qtd_estoque_produto = dados['qtd_estoque']
            print(f"Atualizado dados: {dados}")
            self.p.update(id_produto, nome_produto, marca_produto, tipo_produto,
                          preco_produto, qtd_estoque_produto)

    @pyqtSlot()
    def abrir_dialog_delete(self):

        dialogo = FormularioItensReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_deletado = dialogo.get_data().text()
            print(f"Id deletado: {id_deletado}")
            deleted = self.p.delete(id_deletado)
            print(deleted)
