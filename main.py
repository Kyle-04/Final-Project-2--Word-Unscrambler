from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from english_words import english_words_lower_alpha_set

wordlist = english_words_lower_alpha_set


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        This is all the code from PyQt designer, which designs and opens
        the GUI.

        :param MainWindow: Main Window is just the name of the GUI window.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 0, 121, 16))
        self.title.setObjectName("title")
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.input_label.setObjectName("input_label")
        self.input_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.input_entry.setGeometry(QtCore.QRect(20, 70, 113, 21))
        self.input_entry.setObjectName("input_entry")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.output_label.setObjectName("output_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.scramble_button())

        # This means that the scramble_button function will be run whenever the start button is pressed.

        self.start_button.setGeometry(QtCore.QRect(20, 100, 100, 32))
        self.start_button.setObjectName("start_button")
        self.output_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_display.setGeometry(QtCore.QRect(20, 170, 151, 91))
        self.output_display.setObjectName("output_display")
        self.close_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: exit())

        # This means that the exit() function will be run whenever the close button is pressed.

        self.close_button.setGeometry(QtCore.QRect(190, 230, 100, 32))
        self.close_button.setObjectName("close_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        This function changes the text shown on the buttons, as well as the text found
        in the label headers and titles.
        :param MainWindow: This is just the GUI design from PyQt Designer.
        :return: nothing
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Unscrambler"))
        self.input_label.setText(_translate("MainWindow", "Enter Scrambled Letters:"))
        self.output_label.setText(_translate("MainWindow", "All Possible Words:"))
        self.start_button.setText(_translate("MainWindow", "Unscramble!"))
        self.output_display.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "hr { height: 1px; border-width: 0; }\n"
                                               "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.close_button.setText(_translate("MainWindow", "Close"))

    def scramble_button(self):
        """
        This is the most important function, as it deals with the logic that takes place once
        the start button is clicked. It takes the arrangement of scrambled letters and alphabetizes
        them. Then it compares that with every word (alphabetized) in the english dictionary
        to see which ones match. If a word matches, it then appends the word to a list of
        possible matches, and outputs that list to the output label on the GUI.
        :return: The list of possible words.
        """
        raw_letters = self.input_entry.text().lower().strip()
        letters = list(raw_letters)
        letters.sort()
        output_list = []
        for row in wordlist:
            row_list = list(row)
            row_list.sort()
            if row_list == letters:
                output_list.append(row)
        output = ','.join(output_list)
        self.output_display.setText(output)
        if len(output_list) == 0:
            self.output_display.setText('No matching words!')


def main():
    """
    This is the main function. When the program is run, this function
    will run and open up the GUI, so you can unscramble your words!
    """
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
