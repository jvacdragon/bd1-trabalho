from tela_base import Tela
from estilos import estilo_botao, estilo_dialogo_formulario, estilo_label_menu, estilo_main_window, estilo_tabela
from formularios import FormularioClienteInsertRead, FormularioClienteUpdateDelete
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
    QHeaderView,
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
from db.repositories.clientesRepository import ClientesRepository
import sys


class TelaClientes(Tela):
    def __init__(self):
        super().__init__("PAINEL - Clientes")
        self.c = ClientesRepository()
        self.table = QTableWidget()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.table, 2)
        colunas = ["ID", "Nome", "Endereço", "Email"]

        #BOTOES_CONFIG
        layout_botoes =  QVBoxLayout()
        conteiner_botoes = QWidget()
        conteiner_botoes.setMaximumWidth(600)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)

        self.botao_create_cliente = QPushButton("Criar Cliente")
        self.botao_create_cliente.setFont(fonte_botoes)
        self.botao_create_cliente.setStyleSheet(estilo_botao)
        self.botao_create_cliente.clicked.connect(self.abrir_dialog_create)

        self.botao_read_cliente = QPushButton("Buscar Cliente")
        self.botao_read_cliente.setFont(fonte_botoes)
        self.botao_read_cliente.setStyleSheet(estilo_botao)
        self.botao_read_cliente.clicked.connect(self.abrir_dialog_read)

        self.botao_update_cliente = QPushButton("Atualizar Cliente")
        self.botao_update_cliente.setFont(fonte_botoes)
        self.botao_update_cliente.setStyleSheet(estilo_botao)
        self.botao_update_cliente.clicked.connect(self.abrir_dialog_update)

        self.botao_delete_cliente = QPushButton("Deletar Cliente")
        self.botao_delete_cliente.setFont(fonte_botoes)
        self.botao_delete_cliente.setStyleSheet(estilo_botao)
        self.botao_delete_cliente.clicked.connect(self.abrir_dialog_delete)

        layout_botoes.addWidget(self.botao_create_cliente)
        layout_botoes.addWidget(self.botao_read_cliente)
        layout_botoes.addWidget(self.botao_update_cliente)
        layout_botoes.addWidget(self.botao_delete_cliente)
        layout_botoes.addStretch(1)
        conteiner_botoes.setLayout(layout_botoes)

        self.layout_horizontal.addWidget(conteiner_botoes, 2)
        self.layout_conteudo.addLayout(self.layout_horizontal)
        self.atualizar_tabela(self.c, self.table, colunas)


    def atualizar_tabela(self, c : ClientesRepository, table : QTableWidget, columns):

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

                    id = QTableWidgetItem(str(obj['cliente_id']))
                    nome = QTableWidgetItem(str(obj['nome_cliente']))
                    end = QTableWidgetItem(str(obj['end_residencial']))
                    email = QTableWidgetItem(str(obj['email']))

                    self.table.setItem(i, 0, id)
                    self.table.setItem(i, 1, nome)
                    self.table.setItem(i, 2, end)
                    self.table.setItem(i, 3, email)

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

        dialogo = FormularioClienteInsertRead()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_cliente = dados['cliente_id']
            nome_cliente = dados['nome_cliente']
            end_cliente = dados['end_residencial']
            email_cliente = dados['email']
            print(f"Salvando novo cliente: {dados}")
            self.c.create(id_cliente, nome_cliente, end_cliente, email_cliente)
            
    @pyqtSlot()
    def abrir_dialog_read(self):

        dialogo = FormularioClienteUpdateDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_buscado = dialogo.get_data().text()
            print(f"Id buscado: {id_buscado}")
            read = self.c.read_by_id(id_buscado)
            print(read)

    @pyqtSlot()
    def abrir_dialog_update(self):

        dialogo = FormularioClienteInsertRead()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_cliente = dados['cliente_id']
            nome_cliente = dados['nome_cliente']
            end_cliente = dados['end_residencial']
            email_cliente = dados['email']
            print(f"Atualizado dados cliente: {dados}")
            self.c.update(id_cliente, nome_cliente, end_cliente, email_cliente)

    @pyqtSlot()
    def abrir_dialog_delete(self):

        dialogo = FormularioClienteUpdateDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_deletado = dialogo.get_data().text()
            print(f"Id deletado: {id_deletado}")
            deleted = self.c.delete(id_deletado)
            print(deleted)


        


