from PyQt5.QtWidgets import *
from WordData import WordData
from buttons import buttons, title, updateData, setReviewData


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

class Label(QLabel):

    def __init__(self, text):
        super().__init__()
        self.setText(text)


class CrowlingGui(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.choiceLayout = QGridLayout()
        self.buttonLayout = QGridLayout()
        self.labelLayout = QGridLayout()

        # 콤보 박스
        self.choiceLabel = QLabel()
        self.choiceLabel.setText('영화 분류')
        self.choiceMovie = QComboBox()
        self.choiceMovie.addItems(["master", "국가 부도의 날", "가장 보통의 연애", "검은 사제들"])
        self.choiceLayout.addWidget(self.choiceLabel, 0, 0)
        self.choiceLayout.addWidget(self.choiceMovie, 0, 1, 0, 6)

        #buttons Layout
        r = 0; c = 0
        for btnText in buttons:
            button = Button(btnText, self.buttonClicked)
            self.buttonLayout.addWidget(button, r, c)
            c += 1
            if c >= 2:
                c = 0; r += 1

        #labels Layout
        r = 0
        for lbText in title:
            label = Label(lbText)
            self.labelLayout.addWidget(label, r, 0)
            r += 1

        #texts Layout
        self.tx1 = QLineEdit(); self.tx2 = QLineEdit(); self.tx3 = QLineEdit(); self.tx4 = QTextEdit(); self.tx5 = QTextEdit()
        self.txs = [self.tx1, self.tx2, self.tx3, self.tx4, self.tx5]
        for i in range(len(self.txs)):
            self.txs[i].setReadOnly(True)
            self.labelLayout.addWidget(self.txs[i], i, 1)

        self.mainLayout = QGridLayout()
        self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.mainLayout.addLayout(self.choiceLayout, 0, 0)
        self.mainLayout.addLayout(self.labelLayout,1,0)
        self.mainLayout.addLayout(self.buttonLayout, 1, 1)

        self.setLayout(self.mainLayout)

    def buttonClicked(self):

        button = self.sender()
        key = button.text()

        if key == 'Search':
            self.setData()
        elif key == 'Update':
            self.text = self.choiceMovie.currentText()
            updateData(self.text)
        else:

            for i in self.txs:
                i.clear()

    def setData(self):
        text = self.choiceMovie.currentText()
        self.tx1.setText(text)

        infoData = WordData.getWord(WordData, text+'.info')
        self.tx2.setText(infoData[0])
        self.tx3.setText(infoData[1])

        reviewTexts, reviews = setReviewData(text)
        self.tx4.setText(reviewTexts)
        self.tx5.setText(reviews)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    crowling = CrowlingGui()
    crowling.show()
    sys.exit(app.exec_())