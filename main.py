# ///////////////////////////////////////////////////////////////
# from . resources_rc import *
# BY: Nerykery


import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "AZS style - Modern GUI"
        description = "AZS style"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        self.ui.progressBar_rezervuar1.valueChanged.connect(self.update_label)
        self.update_label()

        self.ui.dtradiobutton.toggled.connect(self.get_radio_value)






    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

            
    def get_radio_value(self):
        """Запускает циклическое изменение progressBar от 0 до 100 и обратно, пока radioButton включен."""
        if self.ui.dtradiobutton.isChecked():
            self.progress_value = 0
            self.increasing = True  # Флаг направления (увеличение)
            
            self.ui.progressBar_rezervuar1.setValue(self.progress_value)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.cycle_progress)
            self.timer.start(50)  # Интервал в миллисекундах
        else:
            if hasattr(self, "timer"):
                self.timer.stop()  # Остановка анимации, если radioButton выключен

    def cycle_progress(self):
        """Изменяет progressBar от 0 до 100 и обратно по кругу."""
        if self.ui.dtradiobutton.isChecked():
            if self.increasing:
                self.progress_value += 1
                if self.progress_value >= 100:
                    self.increasing = False  # Меняем направление
            else:
                self.progress_value -= 1
                if self.progress_value <= 0:
                    self.increasing = True  # Меняем направление

            self.ui.progressBar_rezervuar1.setValue(self.progress_value)
            self.update_label()  # Обновляем label во время изменения
        else:
            self.timer.stop()  # Если radioButton выключен, останавливаем таймер

    def update_label(self):
        """Обновляет label_4 на основе значения progressBar, сохраняя fuel_type"""
        
        progress_value = self.ui.progressBar_rezervuar1.value()  # Получаем текущее значение

        level_mm = int((progress_value * 2100) / 100)
        volume_liters = int((progress_value * 20000) / 100)

        # Извлекаем текущий fuel_type из текста label_4
        current_text = self.ui.label_4.text()
        fuel_type = self.extract_fuel_type(current_text)

        self.ui.label_4.setText(f"""
            <html><head/><body>
                <p align="center"><span style=" font-weight:700; color:#000000;">{fuel_type}</span></p>
                <p align="center"><span style=" font-weight:700; color:#000000;">------</span></p>
                <p align="center"><span style=" font-weight:700; color:#000000;">{level_mm} мм</span></p>
                <p align="center"><span style=" font-weight:700; color:#000000;">{volume_liters} л</span></p>
            </body></html>
        """)


    def extract_fuel_type(self, text):
        """Извлекает fuel_type из HTML-разметки label_4"""
        doc = QTextDocument()
        doc.setHtml(text)
        plain_text = doc.toPlainText()  # Конвертируем HTML в обычный текст
        lines = plain_text.split("\n")  # Разделяем по строкам

        if len(lines) > 0:
            return lines[0].strip()  # Первая строка — это название топлива
        return "Неизвестно"  # Если не удалось извлечь
    
        
    
    
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
