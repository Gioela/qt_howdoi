import sys

from howdoi.howdoi import howdoi
from os import getcwd, sep
from PySide2.QtWidgets import ( QApplication, QMainWindow, QLabel, QLineEdit,
                                QPushButton, QHBoxLayout, QTextEdit,
                                QVBoxLayout, QWidget)

class GegMainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Qt5 - How do I GUI")
        self.setFixedSize(600, 720)

        self.label = QLabel()

        font = self.label.font()
        font.setPointSize(14)
        
        # user input line
        self.UserQuest = QLineEdit()
        self.UserQuest.setFont(font)
        self.UserQuest.setMaxLength(250)
        self.UserQuest.setPlaceholderText('Please, write here your your question "How do I"')

        # ask button
        self.ask_button = QPushButton("Ask")
        self.ask_button.setFont(font)
        self.ask_button.clicked.connect(self.Ask)

        ClearQuestionButton = QPushButton("Clear Question")
        ClearQuestionButton.setFont(font)
        ClearQuestionButton.clicked.connect(self.ClearQuestionBox)

        ClearAnswerButton = QPushButton("Clear Answer")
        ClearAnswerButton.setFont(font)
        ClearAnswerButton.clicked.connect(self.ClearAnswerBox)

        SaveAnswerButton = QPushButton("Save Answer")
        SaveAnswerButton.setFont(font)
        SaveAnswerButton.clicked.connect(self.SaveAnswerBox)

        # define the structure of user interface GUI
        # - the box where user can write his question
        # - the Ask button
        InputGUI = QVBoxLayout()
        InputGUI.addWidget(self.UserQuest)
        InputGUI.addWidget(self.ask_button)

        ButtonGUI = QHBoxLayout()
        ButtonGUI.addWidget(SaveAnswerButton)
        ButtonGUI.addWidget(ClearAnswerButton)
        ButtonGUI.addWidget(ClearQuestionButton)

        # define the structure of ANSWER GUI
        self.AnswerBox = QTextEdit()
        self.AnswerBox.setFont(font)
        self.AnswerBox.setStyleSheet('background-color: #D8E4E1')
        self.AnswerBox.setReadOnly(True)

        self.SavedAnswer = QLabel()

        # define final GUI structure
        # - User Ask GUI
        # - Answer GUI
        layout = QVBoxLayout()
        layout.addLayout(InputGUI)
        layout.addLayout(ButtonGUI)
        layout.addWidget(self.AnswerBox)
        layout.addWidget(self.SavedAnswer)
        # layout.addWidget(self.label)

        # create the container with the above GUI defined
        GuiContainer = QWidget()
        GuiContainer.setLayout(layout)
        self.setCentralWidget(GuiContainer)

    def Ask(self):
        if self.UserQuest.text() != '':
            self.AnswerBox.setText(howdoi(self.UserQuest.text()))

    def ClearAnswerBox(self):
        self.AnswerBox.setText('')
    
    def ClearQuestionBox(self):
        self.UserQuest.setText('')

    def SaveAnswerBox(self):
        if self.AnswerBox.toPlainText() != '':
            _t = [ _.capitalize() for _ in self.UserQuest.text().split() if len(_) > 2]
            _t.append('.txt')
            file_name = ''.join(_t)
            with open(file_name, 'w') as f:
                f.writelines(self.AnswerBox.toPlainText())

            self.SavedAnswer.setText(f'Answer saved in:\n{sep.join([getcwd(), file_name])}')
            # self.SavedAnswer.setOpenExternalLinks(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GegMainWindow()
    window.show()

    app.exec_()