from PySide6.QtWidgets import QPushButton, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QSizePolicy
from simpleeval import simple_eval


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window initialization
        # - setWindowTitle: user-facing window title
        # - setGeometry: position and size (x, y, width, height)
        self.setWindowTitle("Calculator")
        self.setGeometry(400, 500, 400, 500)
        self.setMaximumSize(400, 500)
        self.setMinimumSize(250, 275)

        # Central widget composition
        central_widget = MainWidget()
        self.setCentralWidget(central_widget)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Main widget layout
        # This widget uses a vertical box layout to host the GridButtonHolder
        self.layout = QVBoxLayout(self)
        main_holder = GridButtonHolder()
        self.layout.addWidget(main_holder)


class GridButtonHolder(QWidget):
    def __init__(self):
        super().__init__()

        # Grid layout setup
        # The calculator UI is arranged in a QGridLayout. Top row contains the
        # input QLineEdit spanning all columns so expressions are visible.
        self.layout = QGridLayout(self)

        # Definition of buttons and input field
        # - `line_edit` displays the current expression / result
        # - Buttons are created for digits, operations, clear, and equals
        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet("""
                QLineEdit{
                            height:70px;
                            font-family:'Arial';
                            font-size:40px;
                            font-weight:bold;
                                     }
        """)
        self.btn_C = CustomButtons("C")
        self.btn_C.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_CE = CustomButtons("CE")
        self.btn_modulo = CustomButtons("%")
        self.btn_divide = CustomButtons("/")
        self.btn_7 = CustomButtons("7")
        self.btn_8 = CustomButtons("8")
        self.btn_9 = CustomButtons("9")
        self.btn_multiply = CustomButtons("*")
        self.btn_4 = CustomButtons("4")
        self.btn_5 = CustomButtons("5")
        self.btn_6 = CustomButtons("6")
        self.btn_add = CustomButtons("+")
        self.btn_1 = CustomButtons("1")
        self.btn_2 = CustomButtons("2")
        self.btn_3 = CustomButtons("3")
        self.btn_minus = CustomButtons("-")
        self.btn_zero = CustomButtons("0")
        self.btn_point = CustomButtons(".")
        self.btn_equals = CustomButtons("=")
        self.btn_equals.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Place widgets into the grid (row, column, [rowSpan, colSpan])
        # The input spans 4 columns on the first row
        self.layout.addWidget(self.line_edit, 0, 0, 1, 4)

        # First button row (clear, clear-entry, modulo, divide)
        self.layout.addWidget(self.btn_C, 1, 0)
        self.layout.addWidget(self.btn_CE, 1, 1)
        self.layout.addWidget(self.btn_modulo, 1, 2)
        self.layout.addWidget(self.btn_divide, 1, 3)

        # Numeric and operator rows
        self.layout.addWidget(self.btn_7, 2, 0)
        self.layout.addWidget(self.btn_8, 2, 1)
        self.layout.addWidget(self.btn_9, 2, 2)
        self.layout.addWidget(self.btn_multiply, 2, 3)

        self.layout.addWidget(self.btn_4, 3, 0)
        self.layout.addWidget(self.btn_5, 3, 1)
        self.layout.addWidget(self.btn_6, 3, 2)
        self.layout.addWidget(self.btn_add, 3, 3)

        self.layout.addWidget(self.btn_1, 4, 0)
        self.layout.addWidget(self.btn_2, 4, 1)
        self.layout.addWidget(self.btn_3, 4, 2)
        self.layout.addWidget(self.btn_minus, 4, 3)

        # Bottom row: zero, decimal point, equals (equals spans two columns)
        self.layout.addWidget(self.btn_zero, 5, 0)
        self.layout.addWidget(self.btn_point, 5, 1)
        self.layout.addWidget(self.btn_equals, 5, 2, 1, 2)

        # Connect button signals to handler methods
        # Clear and editing
        self.btn_C.clicked.connect(self.C_clicked)
        self.btn_CE.clicked.connect(self.CE_clicked)
        self.btn_modulo.clicked.connect(self.modulo_clicked)
        self.btn_divide.clicked.connect(self.divide_clicked)

        # Top numeric/operator row
        self.btn_7.clicked.connect(self.seven_clicked)
        self.btn_8.clicked.connect(self.eight_clicked)
        self.btn_9.clicked.connect(self.nine_clicked)
        self.btn_multiply.clicked.connect(self.multiply_clicked)

        # Middle numeric/operator row
        self.btn_4.clicked.connect(self.four_clicked)
        self.btn_5.clicked.connect(self.five_clicked)
        self.btn_6.clicked.connect(self.six_clicked)
        self.btn_add.clicked.connect(self.add_clicked)

        # Lower numeric/operator row
        self.btn_1.clicked.connect(self.one_clicked)
        self.btn_2.clicked.connect(self.two_clicked)
        self.btn_3.clicked.connect(self.three_clicked)
        self.btn_minus.clicked.connect(self.minus_clicked)

        # Bottom row
        self.btn_zero.clicked.connect(self.zero_clicked)
        self.btn_point.clicked.connect(self.point_clicked)
        self.btn_equals.clicked.connect(self.equals_clicked)

    def C_clicked(self):
        # Clear the entire input
        self.line_edit.clear()

    def CE_clicked(self):
        current_text = self.line_edit.text()
        # Clear the last character (backspace behaviour)
        self.line_edit.setText(current_text[:-1])

    def modulo_clicked(self):
        current_text = self.line_edit.text()
        # Append modulo operator
        self.line_edit.setText(current_text + "%")

    def divide_clicked(self):
        current_text = self.line_edit.text()
        # Append division operator
        self.line_edit.setText(current_text + "/")

    def seven_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '7'
        self.line_edit.setText(current_text + "7")

    def eight_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '8'
        self.line_edit.setText(current_text + "8")

    def nine_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '9'
        self.line_edit.setText(current_text + "9")

    def multiply_clicked(self):
        current_text = self.line_edit.text()
        # Append multiplication operator
        self.line_edit.setText(current_text + "*")

    def four_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '4'
        self.line_edit.setText(current_text + "4")

    def five_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '5'
        self.line_edit.setText(current_text + "5")

    def six_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '6'
        self.line_edit.setText(current_text + "6")

    def add_clicked(self):
        current_text = self.line_edit.text()
        # Append addition operator
        self.line_edit.setText(current_text + "+")

    def one_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '1'
        self.line_edit.setText(current_text + "1")

    def two_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '2'
        self.line_edit.setText(current_text + "2")

    def three_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '3'
        self.line_edit.setText(current_text + "3")

    def minus_clicked(self):
        current_text = self.line_edit.text()
        # Append subtraction operator
        self.line_edit.setText(current_text + "-")

    def zero_clicked(self):
        current_text = self.line_edit.text()
        # Insert digit '0'
        self.line_edit.setText(current_text + "0")

    def point_clicked(self):
        current_text = self.line_edit.text()
        # Insert decimal point
        self.line_edit.setText(current_text + ".")

    def equals_clicked(self):
        current_text = self.line_edit.text()
        result = simple_eval(current_text)
        self.line_edit.setText(str(result))


# Custom class for butttons
class CustomButtons(QPushButton):
    def __init__(self, text):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setText(text)
        self.setStyleSheet("""
                    QPushButton{
                            font-family:'Arial';
                            font-size:30px;
                        }
            """)
