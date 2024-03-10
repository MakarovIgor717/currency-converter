from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel)

def rubles_to_dollars(input_rubles, result_container):
    ru_count = float(input_rubles.text())
    result = str(ru_count/80.0) + "$"
    result_container.setText(result)

def dollars_to_rubles(input_rubles, result_container):
    dol_count = float(input_rubles.text())
    result = str(dol_count*80.0) + "Р"
    result_container.setText(result)


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

label = QLabel("Конвертер валют")
layout.addWidget(label)

result_container = QLabel("Тут будет результат")

input_rubles = QLineEdit()
input_rubles.setPlaceholderText("введите рубли")
input_dollars = QLineEdit()
input_dollars.setPlaceholderText("введите доллары")

btn_rubles = QPushButton("перевести\nрубли в доллары")
btn_rubles.clicked.connect(
    lambda: rubles_to_dollars(input_rubles, result_container)
)

btn_dollars = QPushButton("перевести\nдоллары в рубли")
btn_dollars.clicked.connect(
    lambda: dollars_to_rubles(input_rubles, result_container)
)

h_layout1 = QHBoxLayout()
h_layout1.addWidget(input_rubles)
h_layout1.addWidget(btn_rubles)
h_layout2 = QHBoxLayout()
h_layout2.addWidget(input_dollars)
h_layout2.addWidget(btn_dollars)
layout.addLayout(h_layout1)
layout.addLayout(h_layout2)


layout.addWidget(result_container)


window.setLayout(layout)
window.resize(350, 0)
window.show()
app.exec_() 