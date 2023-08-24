import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIntValidator
import sqlite3

uname = ""

class Loginpage(QDialog):
    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("loginpage.ui", self)
        username = self.Username_Field.text()
        # self.setWindowTitle("Login page")
        loginbg = QPixmap('Loginpage_bg.png')
        self.imglabel.setPixmap(loginbg)
        self.loginButton.clicked.connect(self.loginfunction)
        self.RegisterButton.clicked.connect(self.gotoregisterpage)
        self.pass_Field.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        username = self.Username_Field.text()
        global uname
        uname = username
        password = self.pass_Field.text()
        if len(username) == 0 or len(password) == 0:
            self.errorlabel.setText("Fields are empty")
        else:
            conn = sqlite3.connect("HealthMinder.db")
            cur = conn.cursor()
            query = 'SELECT Password FROM login WHERE Username =\'' + username + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                homepage = Homepage()
                widget.addWidget(homepage)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            else:
                self.errorlabel.setText("Invalid Username or password")

    def gotoregisterpage(self):
        registerpage = Registerpage()
        widget.addWidget(registerpage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Registerpage(QDialog):
    def __init__(self):
        super(Registerpage, self).__init__()
        loadUi("registerpage.ui", self)
        self.RegisterButton_rpage.clicked.connect(self.createacc)
        self.BackButton_rpage.clicked.connect(self.goback)
        self.Text_passField_rpage.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Text_ConfirmPass_rpage.setEchoMode(QtWidgets.QLineEdit.Password)

    def goback(self):
        login = Loginpage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createacc(self):
        name = self.Text_Name_rpage.text()
        Username = self.Text_Username_rpage.text()
        password_rpage = self.Text_passField_rpage.text()
        confirmpass_rpage = self.Text_ConfirmPass_rpage.text()
        SpecialSym = ['$', '@', '#', '%', '^', '&', '*', '(', ')', '~']
        val = True
        if val:
            if not password_rpage == confirmpass_rpage:
                val = False

            if len(password_rpage) < 6:
                val = False

            if len(password_rpage) > 20:
                val = False

            if not any(char.isdigit() for char in password_rpage):
                val = False

            if not any(char.isupper() for char in password_rpage):
                val = False

            if not any(char.islower() for char in password_rpage):
                val = False

            if not any(char in SpecialSym for char in password_rpage):
                val = False
            if val:
                con = sqlite3.connect("HealthMinder.db")
                query = "insert into Register(name,Username_rpage,pass_rpage,confirmpass_rpage) values ('" + name + "','" + Username + "','" + password_rpage + "','" + confirmpass_rpage + "')"
                query1 = "insert into Login(Username,Password) values ('" + Username + "','" + password_rpage + "')"
                con.execute(query)
                con.execute(query1)
                con.commit()
                con.close()
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Registered Successfully!")
                msg.setIcon(QMessageBox.Information)
                msg.buttonClicked.connect(self.goback)
                x = msg.exec_()
            else:
                print("set a proper password")
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Invalid Password!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()


class Excercise(QDialog, QWidget):
    def __init__(self):
        super(Excercise, self).__init__()
        loadUi("NExercise.ui", self)
        self.BackbtnExer.clicked.connect(self.gotohomepage)
        # Exercise buttons
        self.btn_run.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1_run))
        self.btn_cycling.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3_Cycling))
        self.btn_legraise.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_9_legraise))
        self.btn_plank.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_10_plank))
        self.btn_crunches.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_8_crunches))
        self.btn_pullup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7_pullp))
        self.btn_pushup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5_pushup))
        self.btn_skipping.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4_skipping))
        self.btn_surya.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6_surya))
        self.btn_walk.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2_walk))
        self.btn_addexerrun.clicked.connect(self.execaddexerrun)
        self.btn_addexer_walk.clicked.connect(self.execaddexerwalk)
        self.btn_addexer_pushup.clicked.connect(self.execaddexerpushup)
        self.btn_addexer_pullup.clicked.connect(self.execaddexerpullup)
        self.btn_addexer_skip.clicked.connect(self.execaddexerskip)
        self.btn_addexer_cyc.clicked.connect(self.execaddexercyc)
        self.btn_addexer_legraise.clicked.connect(self.execaddexerlegraise)
        self.btn_addexer_crunches.clicked.connect(self.execaddexercrunches)
        self.btn_addexer_plank.clicked.connect(self.execaddexerplank)
        self.btn_addexer_surya.clicked.connect(self.execaddexersurya)
        runimg = QPixmap('RUN3.png')
        self.run_img_lab.setPixmap(runimg)

        walkimg = QPixmap('WALK2.PNG')
        self.label_3.setPixmap(walkimg)

        pspimg = QPixmap('PULLUPS2.PNG')
        self.label_9.setPixmap(pspimg)

        plpimg = QPixmap('PULLUPS2.PNG')
        self.label_13.setPixmap(plpimg)

        skpimg = QPixmap('SKIP2.PNG')
        self.label_7.setPixmap(skpimg)

        cycimg = QPixmap('Cycling.jpg')
        self.label_5.setPixmap(cycimg)

        lgrimg = QPixmap('LEGRAISES1.PNG')
        self.label_17.setPixmap(lgrimg)

        crchimg = QPixmap('CRUNCHES1.PNG')
        self.label_15.setPixmap(crchimg)

        plnkimg = QPixmap('PLANK2.PNG')
        self.label_19.setPixmap(plnkimg)

        suryaimg = QPixmap('SURYA2.PNG')
        self.label_11.setPixmap(suryaimg)


    def execaddexerwalk(self):
        user1 = uname
        walkcounter = self.min_counter_walk.text()
        con = sqlite3.connect("HealthMinder.db")
        query1 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Walking','" + walkcounter + "','-----')"
        con.execute(query1)
        con.commit()
        con.close()
        print("working")

    def execaddexerrun(self):
        user1 = uname
        runcounter = self.min_counter_run.text()
        con = sqlite3.connect("HealthMinder.db")
        query2 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Running','" + runcounter + "','-----')"
        con.execute(query2)
        con.commit()
        con.close()
        print("working")

    def execaddexerpushup(self):
        user1 = uname
        pushupscounter = self.rep_counter_pushup.text()
        con = sqlite3.connect("HealthMinder.db")
        query3 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Pushups','-----','" + pushupscounter + "')"
        con.execute(query3)
        con.commit()
        con.close()
        print("working")

    def execaddexerpullup(self):
        user1 = uname
        pullupscounter = self.rep_counter_pullups.text()
        con = sqlite3.connect("HealthMinder.db")
        query4 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Pullsups','-----','" + pullupscounter + "')"
        con.execute(query4)
        con.commit()
        con.close()
        print("working")

    def execaddexerskip(self):
        user1 = uname
        skippingcounter = self.min_counter_skipping.text()
        con = sqlite3.connect("HealthMinder.db")
        query5 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Skipping','-----','" + skippingcounter + "')"
        con.execute(query5)
        con.commit()
        con.close()
        print("working")

    def execaddexercyc(self):
        user1 = uname
        cyclingcounter = self.min_counter_cycling.text()
        con = sqlite3.connect("HealthMinder.db")
        query6 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Cycling','" + cyclingcounter + "','-----')"
        con.execute(query6)
        con.commit()
        con.close()
        print("working")

    def execaddexerlegraise(self):
        user1 = uname
        legraisecounter = self.rep_counter_legraise.text()
        con = sqlite3.connect("HealthMinder.db")
        query7 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Legraise','-----','" + legraisecounter + "')"
        con.execute(query7)
        con.commit()
        con.close()
        print("working")

    def execaddexercrunches(self):
        user1 = uname
        crunchescounter = self.rep_counter_crunches.text()
        con = sqlite3.connect("HealthMinder.db")
        query8 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Crunches','-----','" + crunchescounter + "')"
        con.execute(query8)
        con.commit()
        con.close()
        print("working")

    def execaddexerplank(self):
        user1 = uname
        plankcounter = self.min_counter_plank.text()
        con = sqlite3.connect("HealthMinder.db")
        query9 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Plank','" + plankcounter + "','-----')"
        con.execute(query9)
        con.commit()
        con.close()
        print("working")

    def execaddexersurya(self):
        user1 = uname
        suryacounter = self.rep_counter_surya.text()
        con = sqlite3.connect("HealthMinder.db")
        query0 = "insert into Exercise(Username,Type,Time,Reps) values ('" + user1 + "','Surya Namaskar','-----','" + suryacounter + "')"
        con.execute(query0)
        con.commit()
        con.close()
        print("working")

    # def loaddata(self):
        # connection = sqlite3.connect("HealthMinder.db")
        # cur = connection.cursor()
        # sqlquery = "SELECT * FROM Run LIMIT 50 "
        #
        # self.tableWidget.setRowCount(50)
        # tablerow = 0
        # for row in cur.execute(sqlquery):
        #     self.tableWidget_user1.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
        #     self.tableWidget_user1.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[0]))
        #
        #     tablerow+=1

    def gotohomepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Diet(QDialog):
    def __init__(self):
        super(Diet, self).__init__()
        loadUi("NDiet.ui", self)
        self.Backbtn_diet.clicked.connect(self.gotohomepage)
        self.btn_weightgainplan.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3_wtgain))
        self.btn_weightlossplan.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2_wtloss))
        self.btn_regularplan.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1_regular))

    def gotohomepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Medicine(QDialog):
    def __init__(self):
        super(Medicine, self).__init__()
        loadUi("NMedicine.ui", self)
        self.btnback_Med.clicked.connect(self.gotohomepage)
        self.btn_add_med.clicked.connect(self.gotoaddmedicine)

    def gotoaddmedicine(self):
        # super().loginfunction()
        # username_login = self.username
        # print(username_login)
        # Username_med = self.txt_Username.text()
        user1 = uname
        medicine_name =self.text_med1.text()
        day=self.txt_day1.text()
        time=self.txt_time1.text()
        con = sqlite3.connect("HealthMinder.db")
        # query = "insert into Medicine(Medicine_Name,Days,Time) values ("' + medicine_name +'",'" + day + "','" + time + ''")"
        query = "insert into Medicine(Username,Medicine_Name,Days,Time) values ('" + user1 + "','" + medicine_name + "','" + day + "','" + time + "')"
        con.execute(query)
        con.commit()
        con.close()
        self.text_med1.setText("")
        self.txt_day1.setText("")
        self.txt_time1.setText("")


    def gotohomepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Homepage(QDialog):
    def __init__(self):
        super(Homepage, self).__init__()
        loadUi("Homepage.ui", self)
        Homepagebg = QPixmap('medbk1.png')
        self.bkgd_label.setPixmap(Homepagebg)

        self.btn_med.clicked.connect(self.gotomedicine)
        self.btn_diet.clicked.connect(self.gotodiet)
        self.btn_abt.clicked.connect(self.gotoabout)
        self.btn_close.clicked.connect(self.logout)
        self.btn_exer.clicked.connect(self.gotoexer)
        self.btn_exerdata.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.user1_page))
        self.btn_meddata.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.user2_page))
        # self.btn_dietdata.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.user3_page))
        self.tableWidget_exer.setColumnWidth(0, 250)
        self.tableWidget_exer.setColumnWidth(1, 250)
        self.tableWidget_exer.setColumnWidth(2, 250)
        self.tableWidget_exer.setColumnWidth(3, 250)
        # self.tableWidget_exer.setColumnWidth(3, 200)
        # self.tableWidget_exer.setColumnWidth(4, 200)
        self.tableWidget_med.setColumnWidth(0, 250)
        self.tableWidget_med.setColumnWidth(1, 250)
        self.tableWidget_med.setColumnWidth(2, 250)
        self.tableWidget_med.setColumnWidth(3, 250)
        # self.tableWidget_med.setColumnWidth(3, 200)
        # self.tableWidget_med.setColumnWidth(4, 200)
        # self.tableWidget_diet.setColumnWidth(0, 340)
        # self.tableWidget_diet.setColumnWidth(1, 340)
        # self.tableWidget_diet.setColumnWidth(2, 340)
        # self.tableWidget_diet.setColumnWidth(3, 200)
        # self.tableWidget_diet.setColumnWidth(4, 200)
        self.loadmeddata()
        self.loadexerdata()
    def loadexerdata(self):
        conn = sqlite3.connect("HealthMinder.db")
        cur = conn.cursor()
        user1 = uname
        # meddataquery = "SELECT * FROM Medicine LIMIT 50 "
        exerdataquery = 'SELECT * FROM Exercise WHERE Username =\'' + user1 + "\'"

        self.tableWidget_exer.setRowCount(50)
        tablerow = 0
        for row in cur.execute(exerdataquery):
            # print(row)
            self.tableWidget_exer.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget_exer.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget_exer.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget_exer.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1

    def loadmeddata(self):
        conn = sqlite3.connect("HealthMinder.db")
        cur = conn.cursor()
        user1 = uname
        # meddataquery = "SELECT * FROM Medicine LIMIT 50 "
        meddataquery = 'SELECT * FROM Medicine WHERE Username =\'' + user1 + "\'"

        self.tableWidget_med.setRowCount(50)
        tablerow = 0
        for row in cur.execute(meddataquery):
            # print(row)
            self.tableWidget_med.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget_med.setItem(tablerow, 1,QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget_med.setItem(tablerow, 2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget_med.setItem(tablerow, 3,QtWidgets.QTableWidgetItem(row[3]))
            tablerow+=1


    def gotohomepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoexer(self):
        exercise = Excercise()
        widget.addWidget(exercise)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomedicine(self):
        medicine = Medicine()
        widget.addWidget(medicine)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotodiet(self):
        diet = Diet()
        widget.addWidget(diet)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoabout(self):
        abtus = Aboutpage()
        widget.addWidget(abtus)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def logout(self):
        login = Loginpage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Aboutpage(QDialog):
    def __init__(self):
        super(Aboutpage, self).__init__()
        loadUi("UAboutUs.ui", self)
        bmi_img = QPixmap('BMI2.png')
        self.imgLabelbmi.setPixmap(bmi_img)
        self.Back_btn_abtpage.clicked.connect(self.gotohomepage)
        self.Calc_btn_abtpage.clicked.connect(self.Calc_BMI)
        self.Clear_btn_abtpage.clicked.connect(self.cleartext)
    def Calc_BMI(self):
        h = float(self.Height.text())
        w = float(self.Weight.text())

        bmi = ((w/(h*h))*10000)
        bmi1 = str("{:.2f}".format(bmi))
        self.BMIresult.setText(bmi1)
        if bmi1 < "18.5":
            self.BMIstatus.setText("Underweight")
        elif "18.5" <= bmi1 <= "24.5":
            self.BMIstatus.setText("Normal weight")
        elif "25.0" <= bmi1 <= "29.9":
            self.BMIstatus.setText("Overweight")
        elif bmi1 >= "30":
            self.BMIstatus.setText("Obese")
        else:
            self.BMIstatus.setText("Error")

    def cleartext(self):
        self.Height.setText("")
        self.Weight.setText("")
        self.BMIresult.setText("")
        self.BMIstatus.setText("")

    def gotohomepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Loginpage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
app.exec_()
