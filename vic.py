from pyqt5.Qtwidgets import*
app = QApplication([])

window = QWidget()
window.resize(500,500)

lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
srartBtn = QPushButton("Дізнатися переможця")
main_line = QWBoxLayout()
main_line.addWidget(lbl)
window.setLayout(main_line)

def banana():
    a = random.randint(1,10)
    numberlbl.setText(str(a))

    srartBtn.clicked.connect(banana)


window.show()
app.exec()