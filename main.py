# ///////////////////////////////////////////////////////////////
# from . resources_rc import *
# BY: Nerykery


import sys
import os
import platform
import re
import random

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


        self.ui.testradiobutton.toggled.connect(self.toggle_tanks)
        

        
        
        # Переменные для хранения значений и направлений
        
          # True - увеличение, False - уменьшение
        self.tanks = {
            "reservuar1": {"progress": self.ui.progressBar_rezervuar1, "label": self.ui.label_dt, "timer": QTimer(self)},
            "reservuar2": {"progress": self.ui.progressBar_rezervuar2, "label": self.ui.label_a80, "timer": QTimer(self)},
            "reservuar3": {"progress": self.ui.progressBar_rezervuar3, "label": self.ui.label_ai92, "timer": QTimer(self)},
            "reservuar4": {"progress": self.ui.progressBar_rezervuar4, "label": self.ui.label_ai95, "timer": QTimer(self)},
            "reservuar5": {"progress": self.ui.progressBar_rezervuar5, "label": self.ui.label_ai98, "timer": QTimer(self)},
        }
        self.ui.progressBar_rezervuar1.valueChanged.connect(lambda: self.update_label("reservuar1"))
        self.ui.progressBar_rezervuar2.valueChanged.connect(lambda: self.update_label("reservuar2"))
        self.ui.progressBar_rezervuar3.valueChanged.connect(lambda: self.update_label("reservuar3"))
        self.ui.progressBar_rezervuar4.valueChanged.connect(lambda: self.update_label("reservuar4"))
        self.ui.progressBar_rezervuar5.valueChanged.connect(lambda: self.update_label("reservuar5"))


        self.tank_values = {key: 0 for key in self.tanks}
        self.tank_directions = {key: True for key in self.tanks} 
        self.tanks["reservuar1"]["table_label"] = self.ui.table_label_dt  # Предположим, что это QLabel
        self.tanks["reservuar2"]["table_label"] = self.ui.table_label_a80
        self.tanks["reservuar3"]["table_label"] = self.ui.table_label_ai92
        self.tanks["reservuar4"]["table_label"] = self.ui.table_label_ai95
        self.tanks["reservuar5"]["table_label"] = self.ui.table_label_ai98

    

    def extract_level_and_volume(self, text):
        """Извлекает уровень (мм) и объем (л) из HTML-разметки label."""
        doc = QTextDocument()
        doc.setHtml(text)
        plain_text = doc.toPlainText()
        lines = plain_text.split("\n")

        # Ищем строки с уровнем и объемом
        level_mm = 0
        volume_liters = 0

        for line in lines:
            if "мм" in line:
                level_mm = int(re.sub(r"[^0-9]", "", line))  # Извлекаем число
            elif "л" in line:
                volume_liters = int(re.sub(r"[^0-9]", "", line))  # Извлекаем число

        return level_mm, volume_liters
    
    








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

            
    def toggle_tanks(self):
        """Запускает или останавливает анимацию всех резервуаров"""
        if self.ui.testradiobutton.isChecked():
            for tank_name, tank in self.tanks.items():
                self.tank_values[tank_name] = 0
                self.tank_directions[tank_name] = True  # Начинаем с увеличения

                tank["progress"].setValue(0)

                tank["timer"].timeout.connect(lambda t=tank_name: self.cycle_progress(t))
                tank["timer"].start(50)  # Интервал обновления
        else:
            for tank in self.tanks.values():
                tank["timer"].stop()

    def cycle_progress(self, tank_name):
        """Обновляет progressBar и label для каждого резервуара"""
        tank = self.tanks[tank_name]

        if self.ui.testradiobutton.isChecked():
            if self.tank_directions[tank_name]:
                self.tank_values[tank_name] += 1
                if self.tank_values[tank_name] >= 100:
                    self.tank_directions[tank_name] = False
            else:
                self.tank_values[tank_name] -= 1
                if self.tank_values[tank_name] <= 0:
                    self.tank_directions[tank_name] = True

            tank["progress"].setValue(self.tank_values[tank_name])
            self.update_label(tank_name)
        else:
            tank["timer"].stop()

    def update_table_label(self, tank_name):
        """Обновляет table_label_dt на основе данных из label_dt."""
        if tank_name not in self.tanks:
            return  # Просто выходим, если tank_name не найден

        tank = self.tanks[tank_name]
        current_text = tank["label"].text()

        # Извлекаем данные из label_dt
        level_mm, volume_liters = self.extract_level_and_volume(current_text)

        # Формируем новый текст для table_label_dt
        new_text = f"""
            <html><head/><body>
                <p align="right">{level_mm}</p>
                <p align="right">{volume_liters}</p>
                <p align="right">{20000-volume_liters}</p>  <!-- Пример дополнительной строки -->
                <p align="right">4</p>  <!-- Пример дополнительной строки -->
            </body></html>
        """

        # Обновляем table_label_dt
        tank["table_label"].setText(new_text)

    def update_label(self, tank_name):
        """Обновляет label на основе значения progressBar."""
        if tank_name not in self.tanks:
            return  # Просто выходим, если tank_name не найден

        tank = self.tanks[tank_name]
        progress_value = tank["progress"].value()

        # Извлекаем текущие данные из label
        current_text = tank["label"].text()
        level_mm, volume_liters = self.extract_level_and_volume(current_text)

        # Обновляем уровень и объем на основе progress_value
        level_mm = int((progress_value * 2100) / 100)  # Пример расчета уровня
        volume_liters = int((progress_value * 20000) / 100)  # Пример расчета объема

        fuel_type = self.extract_fuel_type(current_text)
        text_color = self.extract_text_color(current_text)  # Извлекаем цвет текста

        # Обновляем текст label
        tank["label"].setText(f"""
            <html><head/><body>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{fuel_type}</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">------</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{level_mm} мм</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{volume_liters} л</span></p>
            </body></html>
        """)

        # Обновляем table_label_dt
        self.update_table_label(tank_name)

    def extract_fuel_type(self, text):
        """Извлекает тип топлива из HTML-разметки label"""
        doc = QTextDocument()
        doc.setHtml(text)
        plain_text = doc.toPlainText()
        lines = plain_text.split("\n")

        return lines[0].strip() if lines else "Неизвестно"

    def extract_text_color(self, text):
        """Извлекает цвет текста из HTML-разметки label"""
        # Используем регулярное выражение для поиска цвета
        match = re.search(r'color:\s*(#[0-9a-fA-F]{6})', text)
        if match:
            return match.group(1)  # Возвращаем найденный цвет
        return "#ffffff"  # Возвращаем белый цвет по умолчанию, если цвет не найден
    

        
    
    
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
