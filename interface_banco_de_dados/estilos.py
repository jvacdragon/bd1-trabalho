estilo_main_window = """
    background-color: #2E2E2E; /* Fundo cinza escuro */
"""
estilo_label_menu = """
    color: #FFFFFF; 
    background-color: transparent;
"""
estilo_botao = """
    QPushButton {
        background-color: #D32F2F; /* Fundo vermelho */
        color: #FFFFFF;            /* Texto cinza claro */
        border: 1px solid #606060; /* Borda sutil */
        
        padding: 8px;              /* Espaçamento interno (corrige o "label pequena") */
        border-radius: 8px;        /* Cantos arredondados! */
    }
    
    QPushButton:hover {
        background-color: #F44336; /* Efeito ao passar o mouse */
    }
    
    QPushButton:pressed {
        background-color: #B71C1C; /* Efeito ao clicar */
    }
"""
estilo_dialogo_formulario = """
    QDialog {
        background-color: #2E2E2E; /* Fundo escuro */
    }
    
    /* Define a cor dos rótulos ("NOME:", "ID:") */
    QLabel {
        color: #FFFFFF; /* Texto branco */
        font-size: 14px;
    }
    
    /* Define a cor das caixas de texto */
    QLineEdit {
        background-color: #4A4A4A;  /* Fundo da caixa (cinza médio) */
        color: #E0E0E0;             /* Cor do TEXTO (cinza claro) */
        border: 1px solid #606060;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    
    /* (Opcional) Destaca a caixa quando selecionada */
    QLineEdit:focus {
        border-color: #F44336; /* Usa o vermelho do seu tema */
    }
"""

estilo_tabela = """
    QTableWidget {
        background-color: #3A3A3A; /* Um cinza escuro, um pouco mais claro que o fundo */
        color: #E0E0E0;            /* Texto claro */
        border: 1px solid #606060; /* Borda sutil */
        border-radius: 8px;        /* --- BORDAS ARREDONDADAS --- */
        gridline-color: #505050;   /* Cor das linhas da grade */
    }

    /* Estilo do Cabeçalho (ID, Nome, etc.) */
    QHeaderView::section {
        background-color: #B71C1C; /* Vermelho escuro (do clique do botão) */
        color: #FFFFFF;
        padding: 6px;
        border: none;
        font-weight: bold;
    }
    
    /* Cantinho superior esquerdo */
    QTableCornerButton::section {
        background-color: #B71C1C;
    }

    /* Células da tabela */
    QTableWidget::item {
        padding: 5px;
    }
    
    /* Linhas alternadas (efeito zebra) */
    QTableWidget::item:alternate {
        background-color: #424242; /* Um cinza um pouco diferente */
    }

    /* Item selecionado */
    QTableWidget::item:selected {
        background-color: #D32F2F; /* Vermelho principal */
        color: #FFFFFF;
    }
"""