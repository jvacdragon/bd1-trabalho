from tela_base import Tela
from estilos import estilo_botao, estilo_dialogo_formulario, estilo_label_menu, estilo_main_window, estilo_tabela
from formularios import FormularioVendedoresInsertUpdate, FormularioVendedoresReadDelete
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
    QHeaderView,
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
from db.repositories.vendedoresRepository import VendedoresRepository
import sys


class TelaVendedores(Tela):
    def __init__(self, parent=None):
        super().__init__("PAINEL - Vendedores", parent)

        self.ven = VendedoresRepository()
        self.table = QTableWidget()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.table, 3)
        colunas = ["MATRÍCULA", "VENDEDOR", "DATA", "SALÁRIO", "STATUS", "DESLIGAMENTO"]
        

        #BOTOES_CONFIG
        layout_botoes =  QVBoxLayout()
        conteiner_botoes = QWidget()
        conteiner_botoes.setMaximumWidth(600)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)

        self.botao_create_vendedor = QPushButton("Criar Vendedor")
        self.botao_create_vendedor.setFont(fonte_botoes)
        self.botao_create_vendedor.setStyleSheet(estilo_botao)
        self.botao_create_vendedor.clicked.connect(self.abrir_dialog_create)

        self.botao_read_vendedor = QPushButton("Buscar Vendedor")
        self.botao_read_vendedor.setFont(fonte_botoes)
        self.botao_read_vendedor.setStyleSheet(estilo_botao)
        self.botao_read_vendedor.clicked.connect(self.abrir_dialog_read)

        self.botao_update_vendedor = QPushButton("Atualizar Vendedor")
        self.botao_update_vendedor.setFont(fonte_botoes)
        self.botao_update_vendedor.setStyleSheet(estilo_botao)
        self.botao_update_vendedor.clicked.connect(self.abrir_dialog_update)

        self.botao_delete_vendedor = QPushButton("Deletar Vendedor")
        self.botao_delete_vendedor.setFont(fonte_botoes)
        self.botao_delete_vendedor.setStyleSheet(estilo_botao)
        self.botao_delete_vendedor.clicked.connect(self.abrir_dialog_delete)

        layout_botoes.addWidget(self.botao_create_vendedor)
        layout_botoes.addWidget(self.botao_read_vendedor)
        layout_botoes.addWidget(self.botao_update_vendedor)
        layout_botoes.addWidget(self.botao_delete_vendedor)
        conteiner_botoes.setLayout(layout_botoes)
        
        self.layout_horizontal.addWidget(conteiner_botoes, 1)
        self.layout_conteudo.addLayout(self.layout_horizontal)
        self.atualizar_tabela(self.ven, self.table, colunas)
    
    def atualizar_tabela(self, c : VendedoresRepository, table : QTableWidget, columns):
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
                    mat = QTableWidgetItem(str(obj['matricula']))
                    nome_vendedor = QTableWidgetItem(str(obj['nome_vendedor']))
                    dt_admissao = QTableWidgetItem(str(obj['data_admissao']))
                    salario_base = QTableWidgetItem(str(obj['salario_base']))
                    status = QTableWidgetItem(str(obj['status']))
                    dt_desligamento = QTableWidgetItem(str(obj['data_desligamento']))

                    self.table.setItem(i, 0, mat)
                    self.table.setItem(i, 1, nome_vendedor)
                    self.table.setItem(i, 2, dt_admissao)
                    self.table.setItem(i, 3, salario_base)
                    self.table.setItem(i, 4, status)
                    self.table.setItem(i, 5, dt_desligamento)
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

        dialogo = FormularioVendedoresInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            matricula_vendedor = dados['matricula']
            nome_vendedor = dados['nome_vendedor']
            data_admissao = dados['data_admissao']
            salario_base = dados['salario_base']
            status = dados['status']
            data_desligamento = dados['data_desligamento'] 
            print(f"Salvando: {dados}")
            self.ven.create(matricula_vendedor, nome_vendedor, data_admissao,
                            salario_base, status, data_desligamento)

    @pyqtSlot()
    def abrir_dialog_read(self):

        dialogo = FormularioVendedoresReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_buscado = dialogo.get_data().text()
            print(f"Id buscado: {id_buscado}")
            read = self.ven.read_by_id(id_buscado)
            print(read)

    @pyqtSlot()
    def abrir_dialog_update(self):

        dialogo = FormularioVendedoresInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            matricula_vendedor = dados['matricula']
            nome_vendedor = dados['nome_vendedor']
            data_admissao = dados['data_admissao']
            salario_base = dados['salario_base']
            status = dados['status']
            data_desligamento = dados['data_desligamento'] 
            print(f"Atualizado dados: {dados}")
            self.ven.update(matricula_vendedor, nome_vendedor, data_admissao,
                            salario_base, status, data_desligamento)

    @pyqtSlot()
    def abrir_dialog_delete(self):

        dialogo = FormularioVendedoresReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_deletado = dialogo.get_data().text()
            print(f"Id deletado: {id_deletado}")
            deleted = self.ven.delete(id_deletado)
            print(deleted)