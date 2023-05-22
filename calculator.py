import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit


class Calculator(QMainWindow):
    def __init__(self): # Метод-конструктор класса Calculator.
        super().__init__() # Конструктор класса QMainWindow для инициализации главного окна калькулятора
        self.setWindowTitle("Calculator")
        self.current_expression = ""  # Текущее выражение, введенное пользователем
        self.previous_expression = ""  # Предыдущее выражение (для отображения истории)

        # Создание виджета QLineEdit для отображения результата
        self.result_display = QLineEdit(self) # Создает виджет QLineEdit для отображения результата вычислений. Виджет инициализируется родительским виджетом self (главное окно калькулятора).
        self.result_display.setReadOnly(True)  # Установка виджета только для чтения
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)  # Выравнивание текста по правому краю
        self.result_display.setFont(QFont("Arial", 24))  # Установка шрифта

        # Создание виджета QLabel для отображения предыдущего вычисления
        self.previous_expression_label = QLabel(self) # Создает виджет QLabel для отображения предыдущего выражения (истории вычислений).
        self.previous_expression_label.setAlignment(Qt.AlignmentFlag.AlignRight)  # Выравнивание текста по правому краю
        self.previous_expression_label.setWordWrap(True)  # Перенос слов
        self.previous_expression_label.setFont(QFont("Arial", 18))  # Установка шрифта

        # Создание кнопок
        buttons_layout = QGridLayout()
        button_labels = [
            "7", "8", "9", "/",  # Цифры и операторы
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "<-"
        ]

        row = 0
        col = 0
        for label in button_labels:
            button = QPushButton(label)
            button.clicked.connect(self.button_click)
            button.setFont(QFont("Arial", 18))
            buttons_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Создание основного виджета и компоновка элементов
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.previous_expression_label)
        central_layout.addWidget(self.result_display)
        central_layout.addLayout(buttons_layout)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def button_click(self):
        button = self.sender()
        label = button.text()

        if label == "=":  # Если нажата кнопка "="
            expression = self.result_display.text()  # Получаем текущее выражение
            try:
                result = eval(expression)  # Вычисляем результат
                self.previous_expression = self.current_expression + " = " + str(result)  # Формируем строку предыдущего вычисления
                self.previous_expression_label.setText(self.previous_expression)  # Устанавливаем текст предыдущего вычисления
                self.result_display.setText(str(result))  # Устанавливаем текст результата
                self.current_expression = ""  # Очищаем текущее выражение
            except Exception as e:
                self.result_display.setText("Error")  # В случае ошибки выводим "Error"
                print(f"Error: {str(e)}")  # Выводим сообщение об ошибке в консоль
        elif label == "C":  # Если нажата кнопка "C" (очистка)
            self.result_display.clear()  # Очищаем результат
            self.current_expression = ""  # Очищаем текущее выражение
            self.previous_expression = ""  # Очищаем предыдущее вычисление
            self.previous_expression_label.clear()  # Очищаем текст предыдущего вычисления
        elif label == "<-":  # Если нажата кнопка "<-" (удаление последнего символа)
            self.current_expression = self.current_expression[:-1]  # Удаляем последний символ из текущего выражения
            self.result_display.setText(self.current_expression)  # Обновляем текст результата
        else:  # Если нажата кнопка с цифрой или оператором
            self.current_expression += label  # Добавляем метку кнопки в текущее выражение
            self.result_display.setText(self.current_expression)  # Обновляем текст результата


if __name__ == "__main__":
    app = QApplication(sys.argv)
    palette = QPalette()
    # Оформление внешнего вида
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
