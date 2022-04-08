from howdoi.howdoi import howdoi
from os import getcwd, sep
from PySide2.QtWidgets import ( QApplication, QMainWindow, QLabel, QLineEdit,
                                QPushButton, QHBoxLayout, QTextEdit,
                                QVBoxLayout, QWidget)
from sys import argv

# class GegTextEdit(QTextEdit):

#     @property
#     def text(self):
#         return self.Q

class GegPushButton(QPushButton):
    
    def __init__(self, *, label, font, click_func) -> None:
        super().__init__(label)
        self.font = font
        self.clicked_activity = click_func

    @property
    def font(self):
        ...
    
    @font.setter
    def font(self, value):
        self.setFont(value)

    @property
    def clicked_activity(self):
        ...

    @clicked_activity.setter
    def clicked_activity(self, click_func):
        self.clicked.connect(click_func)


class GegMainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Qt5 - How do I GUI")
        self.setFixedSize(600, 720)

        self.label = QLabel()

        font = self.label.font()
        font.setPointSize(14)
        
        # user input line
        self.user_quest = QLineEdit()
        self.user_quest.setFont(font)
        self.user_quest.setMaxLength(250)
        self.user_quest.setPlaceholderText('Please, write here your your question "How do I"')
        self.user_quest.returnPressed.connect(self.Ask)

        # ask button
        self.ask_button = QPushButton("Ask")
        self.ask_button.setFont(font)
        self.ask_button.clicked.connect(self.Ask)

        clear_question_button = GegPushButton(label="Clear Question", font=font, click_func=self.ClearQuestionBox)
        clear_answer_button = GegPushButton(label="Clear Answer", font=font, click_func=self.ClearAnswerBox)
        save_answer_button = GegPushButton(label="Save Answer", font=font, click_func=self.SaveAnswerBox)

        # define the structure of user interface GUI
        # - the box where user can write his question
        # - the Ask button
        input_gui = QVBoxLayout()
        input_gui.addWidget(self.user_quest)
        input_gui.addWidget(self.ask_button)

        button_gui = QHBoxLayout()
        button_gui.addWidget(save_answer_button)
        button_gui.addWidget(clear_answer_button)
        button_gui.addWidget(clear_question_button)

        # define the structure of ANSWER GUI
        self.answer_box = QTextEdit()
        self.answer_box.setFont(font)
        self.answer_box.setStyleSheet('background-color: #D8E4E1')
        self.answer_box.setReadOnly(True)

        self.saved_answer = QLabel()

        # define final GUI structure
        # - User Ask GUI
        # - Answer GUI
        layout = QVBoxLayout()
        layout.addLayout(input_gui)
        layout.addLayout(button_gui)
        layout.addWidget(self.answer_box)
        layout.addWidget(self.saved_answer)
        # layout.addWidget(self.label)

        # create the container with the above GUI defined
        GuiContainer = QWidget()
        GuiContainer.setLayout(layout)
        self.setCentralWidget(GuiContainer)

    def Ask(self):
        if self.user_quest.text() != '':
            self.answer_box.setText(howdoi(self.user_quest.text()))

    def ClearAnswerBox(self):
        self.answer_box.setText('')
    
    def ClearQuestionBox(self):
        self.user_quest.setText('')

    def SaveAnswerBox(self):
        if self.answer_box.toPlainText() != '':
            _t = [ _.capitalize() for _ in self.user_quest.text().split() if len(_) > 2]
            _t.append('.txt')
            file_name = ''.join(_t)
            with open(file_name, 'w') as f:
                f.writelines(self.answer_box.toPlainText())

            msg = 'Answer saved in:\n<a href="' + sep.join([getcwd(), file_name]) + '">open path</a>'
            print(msg)
            self.saved_answer.setText(msg)
            # self.saved_answer.setOpenExternalLinks(True)

if __name__ == '__main__':
    app = QApplication(argv)

    window = GegMainWindow()
    window.show()

    app.exec_()