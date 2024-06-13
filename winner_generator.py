#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

#создание элементов интерфейса
app = QApplication([])
m_w = QWidget()
m_w.setWindowTitle('Определите победителя')
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

#привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
m_w.setLayout(line)

#обработка событий

def show_winner():
    n = randint(0, 99)
    winner.setText(str(n))
    text.setText('Победитель:')

button.clicked.connect(show_winner)

#запуск приложения
m_w.show()
app.exec()