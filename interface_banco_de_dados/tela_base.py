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

class Tela(QWidget):
    voltar = pyqtSignal()

    def __init__(self, nome_tela, parent=None):
        super().__init__()

        #DEFINICOES_JANELA
        layout_tela = QVBoxLayout()
        label_tela = QLabel(f"{nome_tela}")
        label_tela.setStyleSheet(estilo_label_menu)
        fonte_label_tela = QFont("Segoe UI", 20)
        fonte_label_tela.setBold(True)
        label_tela.setFont(fonte_label_tela)
        label_tela.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        self.layout_conteudo = QVBoxLayout()


        #DEFINICOES_BOTOES
        self.botao_voltar = QPushButton("<- Voltar ao Menu")
        fonte_botoes = QFont("Segoe UI", 12)
        fonte_botoes.setBold(True)
        self.botao_voltar.setFont(fonte_botoes)
        self.botao_voltar.setStyleSheet(estilo_botao)
        self.botao_voltar.setMaximumWidth(200)

        #DEFINICOES_LAYOUT
        layout_tela.addWidget(label_tela)
        layout_tela.addStretch(1)
        layout_tela.addLayout(self.layout_conteudo)
        layout_tela.addStretch(1)
        layout_tela.addWidget(self.botao_voltar, alignment=Qt.AlignmentFlag.AlignCenter)
    

        self.setLayout(layout_tela)
        self.botao_voltar.clicked.connect(self.voltar.emit)