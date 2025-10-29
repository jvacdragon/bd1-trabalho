from tela_base import Tela
from estilos import estilo_botao, estilo_dialogo_formulario, estilo_label_menu, estilo_main_window, estilo_tabela
from formularios import FormularioPedidosInsertUpdate, FormularioPedidosReadDelete
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
from db.repositories.pedidosRepository import PedidosRepository
import sys


class TelaVendas(Tela):
    def __init__(self, parent=None):
        super().__init__("PAINEL - Vendas", parent)
        self.v = PedidosRepository()
        self.table = QTableWidget()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.table, 3)
        colunas = ["ID", "DATA", "CLIENTE", "MATRÍCULA", "STATUS", "ENDEREÇO"]


        #BOTOES_CONFIG
        layout_botoes =  QVBoxLayout()
        conteiner_botoes = QWidget()
        conteiner_botoes.setMaximumWidth(600)

        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)

        self.botao_registrar_venda = QPushButton("Registrar Nova Venda")
        self.botao_registrar_venda.setFont(fonte_botoes)
        self.botao_registrar_venda.setStyleSheet(estilo_botao)
        self.botao_registrar_venda.clicked.connect(self.abrir_dialog_create)

        self.botao_consultar_venda = QPushButton("Consultar Venda")
        self.botao_consultar_venda.setFont(fonte_botoes)
        self.botao_consultar_venda.setStyleSheet(estilo_botao)
        self.botao_consultar_venda.clicked.connect(self.abrir_dialog_read)

        self.botao_alterar_venda = QPushButton("Alterar Venda")
        self.botao_alterar_venda.setFont(fonte_botoes)
        self.botao_alterar_venda.setStyleSheet(estilo_botao)
        self.botao_alterar_venda.clicked.connect(self.abrir_dialog_update)

        self.botao_cancelar_venda = QPushButton("Cancelar Venda")
        self.botao_cancelar_venda.setFont(fonte_botoes)
        self.botao_cancelar_venda.setStyleSheet(estilo_botao)
        self.botao_cancelar_venda.clicked.connect(self.abrir_dialog_delete)

        layout_botoes.addWidget(self.botao_registrar_venda)
        layout_botoes.addWidget(self.botao_consultar_venda)
        layout_botoes.addWidget(self.botao_alterar_venda)
        layout_botoes.addWidget(self.botao_cancelar_venda)
        conteiner_botoes.setLayout(layout_botoes)
        
        self.layout_horizontal.addWidget(conteiner_botoes, 1)
        self.layout_conteudo.addLayout(self.layout_horizontal)
        self.atualizar_tabela(self.v, self.table, colunas)
    
    def atualizar_tabela(self, c : PedidosRepository, table : QTableWidget, columns):
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
                    id = QTableWidgetItem(str(obj['pedido_id']))
                    data = QTableWidgetItem(str(obj['data_pedido']))
                    id_cliente = QTableWidgetItem(str(obj['cliente_id']))
                    matricula_vendedor = QTableWidgetItem(str(obj['matricula_vendedor']))
                    status = QTableWidgetItem(str(obj['status_pedido']))
                    end = QTableWidgetItem(str(obj['end_entrega']))
                    self.table.setItem(i, 0, id)
                    self.table.setItem(i, 1, data)
                    self.table.setItem(i, 2, id_cliente)
                    self.table.setItem(i, 3, matricula_vendedor)
                    self.table.setItem(i, 4, status)
                    self.table.setItem(i, 5, end)
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

        dialogo = FormularioPedidosInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_pedido = dados['pedido_id']
            data_pedido = dados['data_pedido']
            cliente_id = dados['cliente_id']
            matricula_vendedor = dados['matricula_vendedor']
            status_pedido = dados['status_pedido']
            endereco_pedido = dados['end_entrega']
            print(f"Salvando: {dados}")
            self.v.create(id_pedido, data_pedido, cliente_id,
                          matricula_vendedor, status_pedido, endereco_pedido)

    @pyqtSlot()
    def abrir_dialog_read(self):

        dialogo = FormularioPedidosReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_buscado = dialogo.get_data().text()
            print(f"Id buscado: {id_buscado}")
            read = self.v.read_by_id(id_buscado)
            print(read)

    @pyqtSlot()
    def abrir_dialog_update(self):

        dialogo = FormularioPedidosInsertUpdate()
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            dados = dialogo.get_data()
            id_pedido = dados['pedido_id']
            data_pedido = dados['data_pedido']
            cliente_id = dados['cliente_id']
            matricula_vendedor = dados['matricula_vendedor']
            status_pedido = dados['status_pedido']
            endereco_pedido = dados['end_entrega']
            print(f"Atualizado dados: {dados}")
            self.v.update(id_pedido, data_pedido, cliente_id, matricula_vendedor,
                          status_pedido, endereco_pedido)

    @pyqtSlot()
    def abrir_dialog_delete(self):

        dialogo = FormularioPedidosReadDelete()

        if dialogo.exec() == QDialog.DialogCode.Accepted:
            id_deletado = dialogo.get_data().text()
            print(f"Id deletado: {id_deletado}")
            deleted = self.v.delete(id_deletado)
            print(deleted)