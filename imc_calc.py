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
        self.setWindowTitle("Calculadora de IMC") # TÍTLO DA JANELA 
        self.setFixedSize(400, 300)  # TAMANHO DA JANELA FIXA - NÃO REDIMENSIONA

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
            # RECEBE VALORES DOS CAMPOS (aceitar vírgula como separador decimal) ficou show!!
            peso_kg_input = float(self.peso_kg_input.text().replace(",", "."))
            altura_mt_input = float(self.altura_mt_input.text().replace(",", "."))
            result = float
            situation = str

         #-------------------------------- CALCULO DE IMC E CONDIÇÕES --------------------------
            result = peso_kg_input/(altura_mt_input**2)
            if result < 16:
                situation = "Você está com Magreza grave" 
            elif result >= 16 and result < 17:
                situation = "Você está com Magreza moderada"
            elif result >= 17 and result < 18.5:
                situation = "Você está com Mageza leve"
            elif result >= 18.5 and result < 25:
                situation = "Você está Saudável, parabéns!"
            elif result >= 25 and result < 30:
                situation = "Você está com Sobrepeso"
            elif result >= 30 and result < 35:
                situation = "Você está com Obesidade grau 1"
            elif result >= 35 and result < 40:
                situation = "Você está com Obesidade grau 2"
            else:
                situation = "Você está com Obesidade grau 3"
        #---------------------------FIM CALCULO E CONDIÇÕES---------------------------------------   
            self.resultado_label.setText(
                f"Resultado: \n"
                f"{situation}" 
            )
      
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")
#----------------------------------------------------------------------------FIM DA INSTÂNCIA -----------
    # FUNÇÃO LIMPAR CAMPOS
    def limpar_campos(self):
        self.peso_kg_input.clear()
        self.altura_mt_input.clear()
        self.resultado_label.setText("Resultado: ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMC_Calc()
    window.show()
    sys.exit(app.exec_())


