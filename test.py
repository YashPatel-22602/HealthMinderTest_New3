import sqlite3
import re
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Loginpage(QDialog):
    def _init_(self):
        super(Loginpage, self)._init_()
        loadUi("loginpage.ui", self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.RegisterButton.clicked.connect(self.gotoregisterpage)
        self.pass_Field.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        username = self.Username_Field.text()
        password = self.pass_Field.text()
        if len(username) == 0 or len(password) == 0:
            # self.error.setText("Please input all fields"
            print()
        else:
            conn = sqlite3.connect("Database")
            cur = conn.cursor()
            query = 'SELECT Password FROM Login WHERE Username=\'' + username + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                # self.error.setText("")
            else:
                print("Invalid Details")
                # self.error.setText("Invalid username or password")

        print("Sucessfully logged in")

    def gotoregisterpage(self):
        registerpage = Registerpage()
        widget.addWidget(registerpage)
        widget.setCurrentIndex(widget.currentIndex()+1)



class Registerpage(QDialog):
    def _init_(self):
        super(Registerpage, self)._init_()
        loadUi("registerpage.ui", self)
        self.RegisterButton_rpage.clicked.connect(self.createacc)
        self.BackButton_rpage.clicked.connect(self.goback)

        # self.RegisterButton_rpage.clicked.connect(self.createacc)
        # self.BackButton_rpage.clicked.connect(self.registerfunction)

    def goback(self):
        login = Loginpage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createacc(self):
        name = self.Text_Name_rpage.text()
        Username = self.Text_Username_rpage.text()
        password_rpage = self.Text_passField_rpage.text()
        confirmpassword_rpage = self.Text_Confirmpass_rpage.text()
        flag = 0
        while True:
            if (len(password_rpage) < 8):
                flag = -1
                break
            elif not re.search("[a-z]", password_rpage):
                flag = -1
                break
            elif not re.search("[A-Z]", password_rpage):
                flag = -1
                break
            elif not re.search("[0-9]", password_rpage):
                flag = -1
                break
            elif not re.search("[_@$]", password_rpage):
                flag = -1
                break
            elif re.search("\s", password_rpage):
                flag = -1
                break
            else:
                flag = 0
                confirmpass_rpage = self.Text_ConfirmPass_rpage.text()
                con = sqlite3.connect("Database")
                query = "insert into Registration(Name,Username,Password,Confirm_Password) values ('" + name + "','" + Username+ "','" + password_rpage + "','" + confirmpass_rpage + "')"
                query1 = "insert into Login(Username,Password) values ('" + Username + "','" + password_rpage + "')"
                con.execute(query)
                con.execute(query1)
                con.commit()
                con.close()
                login = Loginpage()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                # print("Valid Password")
                break

        if flag == -1:
            print("Not a Valid Password")
            # self.error.setText("Minimum 8 characters.
            # The alphabets must be between [a-z],
            # At least one alphabet should be of Upper Case,1 number or digit between [0-9],1 character from [ _ or @ or $ ].").

        if self.Text_passField_rpage.text() == self.Text_ConfirmPass_rpage.text():
            password = self.Text_passField_rpage.text()
            print("successfully registered")
            # login=Loginpage()
            # widget.addWidget(login)
            # widget.setCurrentIndex(widget.currentIndex() + 1)




app = QApplication(sys.argv)
mainwindow = Loginpage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
app.exec_()