from tela_clientes import TelaClientes
from tela_itens import TelaItens
from tela_vendas import TelaVendas
from tela_vendedores import TelaVendedores
from tela_base import Tela
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #DEFINICOES_JANELA  #ACHO QUE 600X400 DEIXA MENOS FEIO
        self.resize(800, 600)
        self.setWindowTitle("LREST")
        self.setStyleSheet(estilo_main_window)

        w_menu = QWidget()
        label_menu = QLabel("BEM-VINDO AO LREST!")
        layout_menu = QVBoxLayout() 
        conteiner_botoes = QWidget()
        layout_botoes = QVBoxLayout()
        conteiner_botoes.setMaximumWidth(500)
        layout_botoes.setSpacing(15)

        self.stack = QStackedWidget()


        #LABEL_MENU_CONFIG
        fonte = label_menu.font()
        fonte.setFamily("Segoe UI")
        fonte.setBold(True)
        fonte.setPointSize(28)
        label_menu.setFont(fonte)
        label_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_menu.setStyleSheet(estilo_label_menu)

        #BOTOES_CONFIG
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)

        botao_painel_cliente = QPushButton("Painel de Clientes")
        botao_painel_cliente.setFont(fonte_botoes)
        botao_painel_cliente.setStyleSheet(estilo_botao)
        botao_painel_cliente.clicked.connect(self.ir_para_clientes)

        botao_painel_vendedor= QPushButton("Painel de Vendedores")
        botao_painel_vendedor.setFont(fonte_botoes)
        botao_painel_vendedor.setStyleSheet(estilo_botao)
        botao_painel_vendedor.clicked.connect(self.ir_para_vendedores)

        botao_painel_itens= QPushButton("Painel de Itens")
        botao_painel_itens.setFont(fonte_botoes)
        botao_painel_itens.setStyleSheet(estilo_botao)
        botao_painel_itens.clicked.connect(self.ir_para_itens)

        botao_painel_vendas= QPushButton("Painel de Vendas")
        botao_painel_vendas.setFont(fonte_botoes)
        botao_painel_vendas.setStyleSheet(estilo_botao)
        botao_painel_vendas.clicked.connect(self.ir_para_vendas)

        #LAYOUT_CONFIG
        layout_botoes.addWidget(label_menu)
        layout_botoes.addWidget(botao_painel_cliente)
        layout_botoes.addWidget(botao_painel_vendedor)
        layout_botoes.addWidget(botao_painel_itens)
        layout_botoes.addWidget(botao_painel_vendas)
        conteiner_botoes.setLayout(layout_botoes)
        layout_menu.addStretch(1)
        layout_menu.addWidget(conteiner_botoes, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_menu.addStretch(1)

        #MAINWINDOW_CONFIG
        w_menu.setLayout(layout_menu)

        #NOVAS_TELAS
        self.tela_clientes = TelaClientes()
        self.tela_vendedores = TelaVendedores()
        self.tela_itens = TelaItens()
        self.tela_vendas = TelaVendas()

        self.stack.addWidget(w_menu)
        self.stack.addWidget(self.tela_clientes)
        self.stack.addWidget(self.tela_vendedores)
        self.stack.addWidget(self.tela_itens)
        self.stack.addWidget(self.tela_vendas)

        self.tela_clientes.voltar.connect(self.ir_para_menu)
        self.tela_vendedores.voltar.connect(self.ir_para_menu)
        self.tela_itens.voltar.connect(self.ir_para_menu)
        self.tela_vendas.voltar.connect(self.ir_para_menu)

        self.setCentralWidget(self.stack)

    

        #MOSTRAR TELA    
        self.show()

    @pyqtSlot()
    def ir_para_menu(self):
        self.stack.setCurrentIndex(0)

    @pyqtSlot()
    def ir_para_clientes(self):
        self.stack.setCurrentIndex(1)
        
    @pyqtSlot()
    def ir_para_vendedores(self):
        self.stack.setCurrentIndex(2)

    @pyqtSlot()
    def ir_para_itens(self):
        self.stack.setCurrentIndex(3)

    @pyqtSlot()
    def ir_para_vendas(self):
        self.stack.setCurrentIndex(4)

app = QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())



