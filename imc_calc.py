import sys
from PyQt5.QtWidgets import ( # importação das classes da biblioteca
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QFont # aqui importa a fonte

class IMC_Calc(QWidget): # Classe IMC_Calc instanciada.-------------- INICIO DA CLASSE --------------
    def __init__(self):                                                                                                                     
        super().__init__()                                                         
        self.init_ui()                                                             
                                                                                   
    def init_ui(self):
        self.setWindowTitle("Calculadora de IMC") # Título da janela 
        self.setFixedSize(400, 300)  # Fixa o tamanho da janela

        # Layout principal
        layout = QVBoxLayout()

        # Formulário para os campos de inputs.............................
        form_layout = QFormLayout()

        self.peso_kg_input = QLineEdit() # campo de inserção do peso
        self.altura_mt_input = QLineEdit() # campo de inseerção da altura

         # Legenda dos campos inputs......................................
        form_layout.addRow("Peso (Kg):", self.peso_kg_input) 
        form_layout.addRow("Altura (m):", self.altura_mt_input)

        layout.addLayout(form_layout) 

        # Resultado
        self.resultado_label = QLabel("Resultado: ")
        font = QFont()
        font.setPointSize(13)  # Define o tamanho da fonte
        self.resultado_label.setFont(font)
        layout.addWidget(self.resultado_label)

        # Criando dois botões: Calcular e Limpar
        button_layout = QHBoxLayout()
        self.calcular_button = QPushButton("Calcular")
        self.calcular_button.setFont(font)
        self.limpar_button = QPushButton("Limpar")
        self.limpar_button.setFont(font)

        button_layout.addWidget(self.calcular_button)
        button_layout.addWidget(self.limpar_button)
        layout.addLayout(button_layout)

         # Conectar os botões
        self.calcular_button.clicked.connect(self.calcular) # Chama a função Calcular
        self.limpar_button.clicked.connect(self.limpar_campos) # chama a função limpar

        # Configuração do layout
        self.setLayout(layout)

    def calcular(self):
        try:
            # Obter valores dos campos (aceitar vírgula como separador decimal) ficou show!!
            peso_kg_input = float(self.peso_kg_input.text().replace(",", "."))
            altura_mt_input = float(self.altura_mt_input.text().replace(",", "."))

         #-------------------------------- calculo de imc--------------------------
        



         #-------------------------------------------------------------------------
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")
#----------------------------------------------------------------------------FIM DA INSTÂNCIA -----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMC_Calc()
    window.show()
    sys.exit(app.exec_())


