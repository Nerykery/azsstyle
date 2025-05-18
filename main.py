



from datetime import datetime, timedelta
import bcrypt
import sqlite3
import sys
import os
import platform
import re
import random



from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" 



widgets = None


def init_database():
    db_exists = os.path.exists('debug.db')
    
    conn = sqlite3.connect('debug.db')
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()
    
    if not db_exists or not table_exists:
        try:
            
            cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            """)
            
            
            cursor.execute("""
                CREATE TABLE tanks (
                    tank_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fuel_type TEXT NOT NULL CHECK(fuel_type IN ('ДТ', 'АИ-92', 'АИ-95', 'А-80', 'АИ-98')),
                    volume REAL NOT NULL,
                    current_level REAL NOT NULL,
                    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            
            cursor.execute("""
                CREATE TABLE fuel_transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tank_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    operation_type TEXT NOT NULL CHECK(operation_type IN ('прием', 'продажа', 'корректировка')),
                    volume REAL NOT NULL,
                    price_per_liter REAL,
                    total_amount REAL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (tank_id) REFERENCES tanks(tank_id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            
            
            cursor.execute("""
                CREATE TABLE cash_register (
                    operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    operation_type TEXT NOT NULL CHECK(operation_type IN ('доход', 'расход')),
                    amount REAL NOT NULL,
                    description TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            
            
            cursor.execute("""
                CREATE TABLE fuel_prices (
                    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fuel_type TEXT NOT NULL CHECK(fuel_type IN ('ДТ', 'АИ-92', 'АИ-95', 'А-80', 'АИ-98')),
                    price REAL NOT NULL,
                    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    valid_to TIMESTAMP NULL
                )
            """)
            
            
            admin_password = "root123".encode('utf-8')
            
            
            admin_hash = bcrypt.hashpw(admin_password, bcrypt.gensalt())
            
            
            cursor.execute("INSERT INTO users (login, password_hash, role) VALUES (?, ?, ?)", 
                         ('root', admin_hash.decode('utf-8'), 'admin'))
            
            
            cursor.executemany(
                "INSERT INTO tanks (fuel_type, volume, current_level) VALUES (?, ?, ?)",
                [
                    ('ДТ', 20000, 15000),
                    ('АИ-92', 20000, 12000),
                    ('АИ-95', 20000, 18000),
                    ('А-80', 10000, 5000),
                    ('АИ-98', 10000, 8000)
                ]
            )
            
            
            cursor.executemany(
                "INSERT INTO fuel_prices (fuel_type, price) VALUES (?, ?)",
                [
                    ('ДТ', 45.50),
                    ('АИ-92', 48.30),
                    ('АИ-95', 51.20),
                    ('А-80', 42.10),
                    ('АИ-98', 55.70)
                ]
            )
            
            conn.commit()
            QMessageBox.information(None, "База данных", "База данных успешно инициализирована")
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при создании базы данных: {str(e)}")
        finally:
            conn.close()
    else:
        conn.close()

def verify_password(login: str, password: str) -> bool:
    """Проверяет соответствие логина и пароля, возвращает True если верно"""
    try:
        conn = sqlite3.connect('debug.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE login = ?", (login,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            stored_hash = result[0].encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
        return False
    except Exception as e:
        print(f"Ошибка при проверке пароля: {e}")
        return False
    


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(300, 200)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(10)

        
        self.label_title = QLabel("Введите логин и пароль")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_title)

        
        self.line_edit_login = QLineEdit()
        self.line_edit_login.setPlaceholderText("Логин")
        layout.addWidget(self.line_edit_login)

        
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setPlaceholderText("Пароль")
        self.line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.line_edit_password)

        
        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.check_credentials)
        layout.addWidget(self.button_login)

    def check_credentials(self):
        login = self.line_edit_login.text()
        password = self.line_edit_password.text()
        
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM users WHERE login = ?", (login,))
            result = cursor.fetchone()
            
            if result and verify_password(login, password):
                role = result[0]
                self.main_window = MainWindow(role=role, login=login)  
                self.main_window.show()
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {str(e)}")
        finally:
            if conn:
                conn.close()
        
class MainWindow(QMainWindow):
    def __init__(self, role='admin', login=''):
        super().__init__()  

        
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)     

        self.setup_user_creation()
        
        
        self.role = role
        self.current_user_login = login
        



        self.tank_mapping = {
            "reservuar1": "ДТ",
            "reservuar2": "А-80",
            "reservuar3": "АИ-92",
            "reservuar4": "АИ-95",
            "reservuar5": "АИ-98"
        }
        self.load_tanks_data()
        
        self.connect_buttons()
        self.display = self.findChild(QTextEdit, "kassa_oknovvoda")


        
        

        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        
        
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        
        
        title = "AZS style - Modern GUI"
        description = "AZS style"
        
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        
        
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        
        
        UIFunctions.uiDefinitions(self)

        
        

        
        

        
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.sozdatuser.clicked.connect(self.buttonClick)
        widgets.delluser.clicked.connect(self.buttonClick)
        widgets.kassa.clicked.connect(self.buttonClick)
        widgets.kassa_enter_button.clicked.connect(self.buttonClick)
        widgets.kassa_clear_button.clicked.connect(self.buttonClick)
        widgets.kassa_dot_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra0_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra00_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra1_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra2_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra3_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra4_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra5_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra6_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra7_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra8_button.clicked.connect(self.buttonClick)
        widgets.kassa_cifra9_button.clicked.connect(self.buttonClick)
        widgets.logs.clicked.connect(self.buttonClick)
        widgets.dt_switch.clicked.connect(self.buttonClick)
        widgets.ai92_switch.clicked.connect(self.buttonClick)
        widgets.ai95_switch.clicked.connect(self.buttonClick)
        widgets.ai98_switch.clicked.connect(self.buttonClick)
        widgets.a80_switch.clicked.connect(self.buttonClick)

        widgets.logs.show() if self.role == 'admin' else widgets.logs.hide()
        widgets.btn_widgets.show() if self.role == 'admin' else widgets.btn_widgets.hide()


        
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)

        
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        
        
        self.show()

        
        
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        
        if useCustomTheme:
            
            UIFunctions.theme(self, themeFile, True)

            
            AppFunctions.setThemeHack(self)

        
        
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


        self.ui.testradiobutton.toggled.connect(self.toggle_tanks)
        

        
        

        self.tanks = {
            "reservuar1": {"progress": self.ui.progressBar_rezervuar1, "label": self.ui.label_dt, "timer": QTimer(self)},
            "reservuar2": {"progress": self.ui.progressBar_rezervuar2, "label": self.ui.label_a80, "timer": QTimer(self)},
            "reservuar3": {"progress": self.ui.progressBar_rezervuar3, "label": self.ui.label_ai92, "timer": QTimer(self)},
            "reservuar4": {"progress": self.ui.progressBar_rezervuar4, "label": self.ui.label_ai95, "timer": QTimer(self)},
            "reservuar5": {"progress": self.ui.progressBar_rezervuar5, "label": self.ui.label_ai98, "timer": QTimer(self)},
        }
        self.setup_connections()
        self.load_tanks_data()

        self.ui.progressBar_rezervuar1.valueChanged.connect(lambda: self.update_label("reservuar1"))
        self.ui.progressBar_rezervuar2.valueChanged.connect(lambda: self.update_label("reservuar2"))
        self.ui.progressBar_rezervuar3.valueChanged.connect(lambda: self.update_label("reservuar3"))
        self.ui.progressBar_rezervuar4.valueChanged.connect(lambda: self.update_label("reservuar4"))
        self.ui.progressBar_rezervuar5.valueChanged.connect(lambda: self.update_label("reservuar5"))

        
        self.ui.radioButton_dt.toggled.connect(self.calculate_price)
        self.ui.radioButton_a80.toggled.connect(self.calculate_price)
        self.ui.radioButton_ai92.toggled.connect(self.calculate_price)
        self.ui.radioButton_ai95.toggled.connect(self.calculate_price)
        self.ui.radioButton_98.toggled.connect(self.calculate_price)
        
        self.ui.litri_dt.textChanged.connect(self.calculate_price)
        self.ui.litri_a80.textChanged.connect(self.calculate_price)
        self.ui.litri_ai92.textChanged.connect(self.calculate_price)
        self.ui.litri_ai95.textChanged.connect(self.calculate_price)
        self.ui.litri_ai98.textChanged.connect(self.calculate_price)


        self.tank_values = {key: 0 for key in self.tanks}
        self.tank_directions = {key: True for key in self.tanks} 
        self.tanks["reservuar1"]["table_label"] = self.ui.table_label_dt  
        self.tanks["reservuar2"]["table_label"] = self.ui.table_label_a80
        self.tanks["reservuar3"]["table_label"] = self.ui.table_label_ai92
        self.tanks["reservuar4"]["table_label"] = self.ui.table_label_ai95
        self.tanks["reservuar5"]["table_label"] = self.ui.table_label_ai98
        
        self.setup_logs_table()
        

    

    
    
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.ui.kassa_oknovvoda.setValidator(validator)
        self.ui.litri_a80.setValidator(validator)
        self.ui.litri_ai92.setValidator(validator)
        self.ui.litri_ai98.setValidator(validator)
        self.ui.litri_dt.setValidator(validator)
        self.ui.litri_ai95.setValidator(validator)




    

    def extract_level_and_volume(self, text):
        """Извлекает уровень (мм) и объем (л) из HTML-разметки label."""
        doc = QTextDocument()
        doc.setHtml(text)
        plain_text = doc.toPlainText()
        lines = plain_text.split("\n")


        level_mm = 0
        volume_liters = 0

        for line in lines:
            if "мм" in line:
                level_mm = int(re.sub(r"[^0-9]", "", line))  
            elif "л" in line:
                volume_liters = int(re.sub(r"[^0-9]", "", line))  

        return level_mm, volume_liters
    
    








    
    
    
    def buttonClick(self):
        
        btn = self.sender()
        btnName = btn.objectName()

        
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "sozdatuser":
            self.create_new_user()

        
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.load_users_to_table()
            self.setup_users_table()

        
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) 
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName == "btn_save":
            print("Save BTN clicked!")
        
        if btnName == "btn_logout":
            self.logout()

        if btnName == "delluser":
            self.delete_selected_user()
        

        if btnName == "kassa":
            widgets.stackedWidget.setCurrentWidget(widgets.kase_page) 
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName == "kassa_cifra00_button":
            self.ui.kassa_oknovvoda.insert("00")
        if btnName == "kassa_cifra0_button":
            self.ui.kassa_oknovvoda.insert("0")
        if btnName == "kassa_dot_button":
            self.ui.kassa_oknovvoda.insert(".")
        if btnName == "kassa_enter_button":
            self.enter_pressed()
        if btnName == "kassa_clear_button":
            self.clear_display()
        if btnName == "kassa_cifra1_button":
            self.ui.kassa_oknovvoda.insert("1")
        if btnName == "kassa_cifra2_button":
            self.ui.kassa_oknovvoda.insert("2")
        if btnName == "kassa_cifra3_button":
            self.ui.kassa_oknovvoda.insert("3")
        if btnName == "kassa_cifra4_button":
            self.ui.kassa_oknovvoda.insert("4")
        if btnName == "kassa_cifra5_button":
            self.ui.kassa_oknovvoda.insert("5")
        if btnName == "kassa_cifra6_button":
            self.ui.kassa_oknovvoda.insert("6")
        if btnName == "kassa_cifra7_button":
            self.ui.kassa_oknovvoda.insert("7")
        if btnName == "kassa_cifra8_button":
            self.ui.kassa_oknovvoda.insert("8")
        if btnName == "kassa_cifra9_button":
            self.ui.kassa_oknovvoda.insert("9")
        if btnName == "logs":
            widgets.stackedWidget.setCurrentWidget(widgets.logs_page) 
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName in ["dt_switch", "ai92_switch", "ai95_switch", "ai98_switch", "a80_switch"]:
            self.toggle_locker_color(btnName)



        

        print(f'Button "{btnName}" pressed!')



    
    
    def resizeEvent(self, event):
        
        UIFunctions.resize_grips(self)

    
    
    def mousePressEvent(self, event):
        
        self.dragPos = event.globalPos()

        
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

            
    def toggle_tanks(self):
        """Запускает или останавливает анимацию всех резервуаров"""
        if self.ui.testradiobutton.isChecked():
            for tank_name, tank in self.tanks.items():
                self.tank_values[tank_name] = 0
                self.tank_directions[tank_name] = True  

                tank["progress"].setValue(0)

                tank["timer"].timeout.connect(lambda t=tank_name: self.cycle_progress(t))
                tank["timer"].start(50)  
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
            return  

        tank = self.tanks[tank_name]
        current_text = tank["label"].text()

        
        level_mm, volume_liters = self.extract_level_and_volume(current_text)

        
        new_text = f"""
            <html><head/><body>
                <p align="right">{level_mm}</p>
                <p align="right">{volume_liters}</p>
                <p align="right">{20000-volume_liters}</p>  <!-- Пример дополнительной строки -->
                <p align="right"></p> 
  <!-- Пример дополнительной строки -->
            </body></html>
        """

        
        tank["table_label"].setText(new_text)

    def update_label(self, tank_name):
        """Обновляет label на основе значения progressBar."""
        if tank_name not in self.tanks:
            return  

        tank = self.tanks[tank_name]
        progress_value = tank["progress"].value()

        
        current_text = tank["label"].text()
        level_mm, volume_liters = self.extract_level_and_volume(current_text)

        
        level_mm = int((progress_value * 2100) / 100)  
        volume_liters = int((progress_value * 20000) / 100)  

        fuel_type = self.extract_fuel_type(current_text)
        text_color = self.extract_text_color(current_text)  

        
        tank["label"].setText(f"""
            <html><head/><body>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{fuel_type}</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">------</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{level_mm} мм</span></p>
                <p align="center"><span style=" font-weight:700; color:{text_color};">{volume_liters} л</span></p>
            </body></html>
        """)

        
        self.update_table_label(tank_name)

    def extract_fuel_type(self, text):
        """Извлекает тип топлива из HTML-разметки label"""
        doc = QTextDocument()
        doc.setHtml(text)
        plain_text = doc.toPlainText()
        lines = plain_text.split("\n")

        return lines[0].strip() if lines else "Неизвестно"

    def extract_text_color(self, text):


        match = re.search(r'color:\s*(#[0-9a-fA-F]{6})', text)
        if match:
            return match.group(1) 
        return "#ffffff"  
    
    def logout(self):
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Выход")
        msg_box.setText("Вы уверены, что хотите выйти?")
        
        
        yes_button = msg_box.addButton("Да", QMessageBox.YesRole)
        no_button = msg_box.addButton("Нет", QMessageBox.NoRole)
        
        
        msg_box.setIcon(QMessageBox.Question)
        
        
        msg_box.exec()
        
        
        if msg_box.clickedButton() == yes_button:
            self.auth_window = AuthWindow()
            self.auth_window.show()
            self.close()
        

        
    def setup_user_creation(self):
        """Настройка функционала создания пользователя"""
        if hasattr(widgets, 'sozdatuser'):
            widgets.sozdatuser.clicked.connect(self.create_new_user)
        
        
        if hasattr(self, 'groupvibor'):
            self.ui.groupvibor.clear()
            self.ui.groupvibor.addItems(["Пользователь", "Администратор"])

    def create_new_user(self):
        """Создание нового пользователя"""
        try:
            
            login = self.ui.login.text().strip() if hasattr(self.ui, 'login') else ""
            password = self.ui.password.text().strip() if hasattr(self.ui, 'password') else ""
            
            
            if hasattr(self.ui, 'groupvibor'):
                role = "admin" if self.ui.groupvibor.currentText() == "Администратор" else "user"
            else:
                role = "user"
            
            
            if not login or not password:
                QMessageBox.warning(self, "Ошибка", "Логин и пароль не могут быть пустыми")
                return
                
            if len(password) < 4:
                QMessageBox.warning(self, "Ошибка", "Пароль должен содержать минимум 4 символа")
                return
            
            
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            
            
            cursor.execute("SELECT login FROM users WHERE login = ?", (login,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином уже существует")
                return
            
            
            cursor.execute(
                "INSERT INTO users (login, password_hash, role) VALUES (?, ?, ?)",
                (login, password_hash.decode('utf-8'), role))
            
            conn.commit()
            QMessageBox.information(self, "Успех", "Пользователь успешно создан")
            self.load_users_to_table()
            
            
            if hasattr(self.ui, 'login'):
                self.ui.login.clear()
            if hasattr(self.ui, 'password'):
                self.ui.password.clear()
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Ошибка БД", f"Ошибка при создании пользователя: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Неизвестная ошибка: {str(e)}")
        finally:
            if 'conn' in locals():
                conn.close()
                

    def setup_users_table(self):
        """Настройка таблицы пользователей и слайдера"""
        if hasattr(self.ui, 'table_users'):
            
            self.ui.table_users.setColumnCount(2)  
            self.ui.table_users.setHorizontalHeaderLabels(["Логин", "Группа"])
            self.ui.table_users.horizontalHeader().setVisible(True)  

            
            self.ui.table_users.setColumnWidth(0, 300)  
            self.ui.table_users.setColumnWidth(1, 150)  

            
            self.ui.table_users.horizontalHeader().setStretchLastSection(False)  
            self.ui.table_users.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  
            self.ui.table_users.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)  
                        
            
            self.ui.table_users.setStyleSheet("""
                QTableWidget {
                    color: 
                    background-color: 
                    gridline-color: 
                }
                QHeaderView::section {
                    background-color: 
                    color: 
                    padding: 5px;
                }
            """)
            
            
            if hasattr(self.ui, 'slider_table'):
                self.ui.slider_table.valueChanged.connect(self.update_table_position)
                self.ui.table_users.verticalScrollBar().valueChanged.connect(
                    self.update_slider_from_table
                )
        


    def load_users_to_table(self):
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            cursor.execute("SELECT login, role FROM users WHERE login != 'root' ORDER BY login")
            users = cursor.fetchall()
            
            self.ui.table_users.setRowCount(len(users))
            
            for row, (login, role) in enumerate(users):
                
                item_login = QTableWidgetItem(login)
                item_login.setFlags(item_login.flags() ^ Qt.ItemIsEditable)
                self.ui.table_users.setItem(row, 0, item_login)
                
                
                role_text = "Администратор" if role == "admin" else "Пользователь"
                item_role = QTableWidgetItem(role_text)
                item_role.setFlags(item_role.flags() ^ Qt.ItemIsEditable)
                
                
                if role == "admin":
                    item_role.setForeground(QColor("#ff5555")) 
                else:
                    item_role.setForeground(QColor("#55aaff"))
                    
                self.ui.table_users.setItem(row, 1, item_role)
                
            

            
        except sqlite3.Error as e:
            print(f"Ошибка загрузки пользователей: {e}")
        finally:
            if conn:
                conn.close()

    def delete_selected_user(self):
        """Удаление выбранного пользователя"""
        selected_row = self.ui.table_users.currentRow()
        if selected_row >= 0:
            login = self.ui.table_users.item(selected_row, 0).text()
            
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setText(f"Вы уверены, что хотите удалить пользователя {login}?")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.button(QMessageBox.Yes).setText("Да")
            msg_box.button(QMessageBox.No).setText("Нет")
            reply = msg_box.exec_()
            
       


            
            if reply == QMessageBox.Yes:
                try:
                    conn = sqlite3.connect('debug.db')
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM users WHERE login = ?", (login,))
                    conn.commit()
                    self.load_users_to_table()
                except sqlite3.Error as e:
                    QMessageBox.critical(self, "Ошибка", f"Не удалось удалить пользователя: {e}")
                finally:
                    if conn:
                        conn.close()
    def kassa_window(self):
        print("pizda1")

    def setup_connections(self):
        """Настраивает соединения сигналов и слотов"""
        self.ui.progressBar_rezervuar1.valueChanged.connect(lambda: self.update_label("reservuar1"))
        self.ui.progressBar_rezervuar2.valueChanged.connect(lambda: self.update_label("reservuar2"))
        self.ui.progressBar_rezervuar3.valueChanged.connect(lambda: self.update_label("reservuar3"))
        self.ui.progressBar_rezervuar4.valueChanged.connect(lambda: self.update_label("reservuar4"))
        self.ui.progressBar_rezervuar5.valueChanged.connect(lambda: self.update_label("reservuar5"))
        
        
        self.tanks["reservuar1"]["table_label"] = self.ui.table_label_dt  
        self.tanks["reservuar2"]["table_label"] = self.ui.table_label_a80
        self.tanks["reservuar3"]["table_label"] = self.ui.table_label_ai92
        self.tanks["reservuar4"]["table_label"] = self.ui.table_label_ai95
        self.tanks["reservuar5"]["table_label"] = self.ui.table_label_ai98
    
    def load_tanks_data(self):
        """Загружает данные о резервуарах из базы данных"""
        conn = None
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            
            for tank_name, fuel_type in self.tank_mapping.items():
                cursor.execute(
                    "SELECT current_level, volume FROM tanks WHERE fuel_type = ?",
                    (fuel_type,)
                )
                result = cursor.fetchone()
                
                if result:
                    current_level, volume = result
                    progress = int((current_level / volume) * 100)
                    self.tanks[tank_name]["progress"].setValue(progress)
                    self.update_label(tank_name)
                    
        except Exception as e:
            print(f"Ошибка при загрузке данных резервуаров: {e}")
        finally:
            if conn:
                conn.close()

    def connect_buttons(self):
        for i in range(10):
            button = self.findChild(QPushButton, f"kassa_cifra{i}_button")
            if button:
                button.clicked.connect(lambda _, num=str(i): self.append_number(num))

        button_00 = self.findChild(QPushButton, "kassa_cifra00_button")
        if button_00:
            button_00.clicked.connect(lambda: self.append_number("00"))

        button_dot = self.findChild(QPushButton, "kassa_dot_button")
        if button_dot:
            button_dot.clicked.connect(lambda: self.append_number("."))

        button_clear = self.findChild(QPushButton, "kassa_clear_button")
        if button_clear:
            button_clear.clicked.connect(self.clear_display)

        button_enter = self.findChild(QPushButton, "kassa_enter_button")
        if button_enter:
            button_enter.clicked.connect(self.enter_pressed)

    def append_number(self, number):
        current_text = self.display.setText()
        self.display.setText(current_text + number)

    def clear_display(self):
        self.ui.kassa_oknovvoda.clear()



    
    
    def get_fuel_price(self, fuel_type):
        """Получает цену топлива из базы данных"""
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            cursor.execute(
                "SELECT price FROM fuel_prices WHERE fuel_type = ? ORDER BY valid_from DESC LIMIT 1",
                (fuel_type,)
            )
            result = cursor.fetchone()
            price = result[0] if result else 0
            print(f"Fetched price for {fuel_type}: {price}")  
            return price
        except Exception as e:
            print(f"Ошибка при получении цены топлива: {e}")
            return 0
        finally:
            if conn:
                conn.close()









    def generate_test_data(self):
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            
            
            cursor.execute("DELETE FROM fuel_transactions")
            cursor.execute("DELETE FROM cash_register")
            
            
            cursor.execute("SELECT id FROM users")
            user_ids = [row[0] for row in cursor.fetchall()]
            
            cursor.execute("SELECT tank_id, fuel_type FROM tanks")
            tanks = cursor.fetchall()
            
            
            for i in range(30):
                date = datetime.now() - timedelta(days=30 - i)
                
                
                for tank_id, fuel_type in tanks:
                    
                    for _ in range(random.randint(1, 5)):
                        volume = round(random.uniform(5, 50), 2)
                        price = self.get_fuel_price(fuel_type)
                        total = round(volume * price, 2)
                        
                        cursor.execute(
                            "INSERT INTO fuel_transactions (tank_id, user_id, operation_type, volume, price_per_liter, total_amount, timestamp) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (tank_id, random.choice(user_ids), 'продажа', volume, price, total, 
                            date.replace(hour=random.randint(8, 20), minute=random.randint(0, 59))))
                        
                        
                        cursor.execute(
                            "INSERT INTO cash_register (user_id, operation_type, amount, description, timestamp) "
                            "VALUES (?, ?, ?, ?, ?)",
                            (random.choice(user_ids), 'доход', total, 
                            f"Продажа {fuel_type} - {volume} л", 
                            date.replace(hour=random.randint(8, 20), minute=random.randint(0, 59))))
                    
                    
                    if i % random.randint(3, 5) == 0:
                        volume = round(random.uniform(1000, 5000), 2)
                        price = round(self.get_fuel_price(fuel_type) * 0.8, 2)  
                        total = round(volume * price, 2)
                        
                        cursor.execute(
                            "INSERT INTO fuel_transactions (tank_id, user_id, operation_type, volume, price_per_liter, total_amount, timestamp) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (tank_id, random.choice(user_ids), 'прием', volume, price, total, 
                            date.replace(hour=random.randint(8, 20), minute=random.randint(0, 59))))
                        
                        
                        cursor.execute(
                            "INSERT INTO cash_register (user_id, operation_type, amount, description, timestamp) "
                            "VALUES (?, ?, ?, ?, ?)",
                            (random.choice(user_ids), 'расход', total, 
                            f"Закупка {fuel_type} - {volume} л", 
                            date.replace(hour=random.randint(8, 20), minute=random.randint(0, 59))))
            
            conn.commit()
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при генерации тестовых данных: {str(e)}")
        finally:
            if conn:
                conn.close()

    def setup_logs_table(self):
        """Настраивает таблицу логов"""
        if hasattr(self.ui, 'table_logs'):
            
            self.ui.table_logs.setColumnCount(5)
            self.ui.table_logs.setHorizontalHeaderLabels(["Дата", "Тип операции", "Описание", "Сумма", "Пользователь"])
            
            
            self.ui.table_logs.setStyleSheet("""
                QTableWidget {
                    background-color: 
                    color: 
                    gridline-color: 
                    border: 1px solid 
                }
                QHeaderView::section {
                    background-color: 
                    color: 
                    padding: 5px;
                    border: none;
                }
                QTableWidget::item {
                    padding: 5px;
                }
            """)
            
            
            self.ui.table_logs.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
            self.ui.table_logs.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            self.ui.table_logs.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
            self.ui.table_logs.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
            self.ui.table_logs.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
            
            
            self.load_logs_data()

    def load_logs_data(self):
        """Загружает данные в таблицу логов"""
        try:
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            
            
            cursor.execute("""
                SELECT cr.timestamp, cr.operation_type, cr.description, cr.amount, u.login 
                FROM cash_register cr
                JOIN users u ON cr.user_id = u.id
                ORDER BY cr.timestamp DESC
                LIMIT 100
            """)
            logs = cursor.fetchall()
            
            self.ui.table_logs.setRowCount(len(logs))
            
            for row, (timestamp, op_type, description, amount, user) in enumerate(logs):
                
                date_item = QTableWidgetItem(timestamp)
                self.ui.table_logs.setItem(row, 0, date_item)
                
                
                type_item = QTableWidgetItem("Доход" if op_type == "доход" else "Расход")
                self.ui.table_logs.setItem(row, 1, type_item)
                
                
                desc_item = QTableWidgetItem(description)
                self.ui.table_logs.setItem(row, 2, desc_item)
                
                

                amount_item = QTableWidgetItem(f"{amount:.2f} ₽")
                if op_type == "доход":
                    amount_item.setForeground(QColor("#7CFC00"))
                else:
                    amount_item.setForeground(QColor("#FF4500"))
                self.ui.table_logs.setItem(row, 3, amount_item)
                
                
                user_item = QTableWidgetItem(user)
                self.ui.table_logs.setItem(row, 4, user_item)
                
        except Exception as e:
            print(f"Ошибка загрузки логов: {e}")
        finally:
            if conn:
                conn.close()

    def toggle_locker_color(self, btnName):
        
        button_to_locker = {
            "dt_switch": "dt_locker",
            "ai92_switch": "ai92_locker",
            "ai95_switch": "ai95_locker",
            "ai98_switch": "ai98_locker",
            "a80_switch": "a80_locker",
        }
        
        locker_name = button_to_locker.get(btnName)
        if not locker_name:
            return
        
        locker = self.findChild(QFrame, locker_name)
        if not locker:
            return
        
        
        style = locker.styleSheet()
        
        
        if "background-color: green" in style:
            new_style = style.replace("green", "red")
        else:
            new_style = style.replace("red", "green")
        
        locker.setStyleSheet(new_style)


    def calculate_price(self):
        """Рассчитывает цену на основе выбранного топлива и введенных литров"""
        fuel_types = {
            "radioButton_dt": "ДТ",
            "radioButton_a80": "А-80",
            "radioButton_ai92": "АИ-92",
            "radioButton_ai95": "АИ-95",
            "radioButton_98": "АИ-98"
        }
        
        
        selected_fuel = None
        for radio_name, fuel_type in fuel_types.items():
            radio = self.findChild(QRadioButton, radio_name)
            if radio and radio.isChecked():
                selected_fuel = fuel_type
                break
        
        if not selected_fuel:
            return
        
        
        liters_input = None
        if selected_fuel == "ДТ":
            liters_input = self.findChild(QLineEdit, "litri_dt")
        elif selected_fuel == "А-80":
            liters_input = self.findChild(QLineEdit, "litri_a80")
        elif selected_fuel == "АИ-92":
            liters_input = self.findChild(QLineEdit, "litri_ai92")
        elif selected_fuel == "АИ-95":
            liters_input = self.findChild(QLineEdit, "litri_ai95")
        elif selected_fuel == "АИ-98":
            liters_input = self.findChild(QLineEdit, "litri_ai98")
        
        if not liters_input:
            return
        
        try:
            liters = float(liters_input.text())
            price_per_liter = self.get_fuel_price(selected_fuel)
            total = liters * price_per_liter
            
            
            self.ui.kassa_oknovvoda.setText(f"{total:.2f} ₽")
        except ValueError:
            
            self.ui.kassa_oknovvoda.setText("")

    def enter_pressed(self):
        """Обработка нажатия кнопки Enter - запись операции в БД"""
        try:
            
            amount_text = self.ui.kassa_oknovvoda.text().replace(' ₽', '').strip()
            if not amount_text:
                QMessageBox.warning(self, "Ошибка", "Введите сумму")
                return
                
            try:
                total_amount = float(amount_text)
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Некорректная сумма")
                return
            
            
            fuel_types = {
                "radioButton_dt": "ДТ",
                "radioButton_a80": "А-80",
                "radioButton_ai92": "АИ-92",
                "radioButton_ai95": "АИ-95",
                "radioButton_98": "АИ-98"
            }
            
            selected_fuel = None
            for radio_name, fuel_type in fuel_types.items():
                radio = self.findChild(QRadioButton, radio_name)
                if radio and radio.isChecked():
                    selected_fuel = fuel_type
                    break
            
            if not selected_fuel:
                QMessageBox.warning(self, "Ошибка", "Выберите тип топлива")
                return
            
            
            liters_input = None
            if selected_fuel == "ДТ":
                liters_input = self.findChild(QLineEdit, "litri_dt")
            elif selected_fuel == "А-80":
                liters_input = self.findChild(QLineEdit, "litri_a80")
            elif selected_fuel == "АИ-92":
                liters_input = self.findChild(QLineEdit, "litri_ai92")
            elif selected_fuel == "АИ-95":
                liters_input = self.findChild(QLineEdit, "litri_ai95")
            elif selected_fuel == "АИ-98":
                liters_input = self.findChild(QLineEdit, "litri_ai98")
            
            if not liters_input:
                QMessageBox.warning(self, "Ошибка", "Не найдено поле ввода литров")
                return
            
            try:
                volume = float(liters_input.text())
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Некорректное количество литров")
                return
            
            conn = sqlite3.connect('debug.db')
            cursor = conn.cursor()
            
            
            cursor.execute("SELECT current_level FROM tanks WHERE fuel_type = ?", (selected_fuel,))
            current_level = cursor.fetchone()[0]
            
            if volume > current_level:
                QMessageBox.warning(self, "Ошибка", "Недостаточно топлива в резервуаре")
                conn.close()
                return
            
            
            cursor.execute("SELECT tank_id FROM tanks WHERE fuel_type = ?", (selected_fuel,))
            tank_result = cursor.fetchone()
            if not tank_result:
                QMessageBox.warning(self, "Ошибка", "Не найден резервуар для выбранного топлива")
                conn.close()
                return
            tank_id = tank_result[0]
            
            
            cursor.execute("SELECT id FROM users WHERE login = ?", (self.current_user_login,))
            user_result = cursor.fetchone()
            if not user_result:
                QMessageBox.warning(self, "Ошибка", "Не найден пользователь")
                conn.close()
                return
            user_id = user_result[0]
            
            
            price_per_liter = self.get_fuel_price(selected_fuel)
            
            
            cursor.execute(
                "INSERT INTO fuel_transactions (tank_id, user_id, operation_type, volume, price_per_liter, total_amount, timestamp) "
                "VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
                (tank_id, user_id, 'продажа', volume, price_per_liter, total_amount)
            )
            
            
            cursor.execute(
                "INSERT INTO cash_register (user_id, operation_type, amount, description, timestamp) "
                "VALUES (?, ?, ?, ?, datetime('now'))",
                (user_id, 'доход', total_amount, f"Продажа {selected_fuel} - {volume} л")
            )
            
            
            cursor.execute(
                "UPDATE tanks SET current_level = current_level - ?, last_update = datetime('now') WHERE tank_id = ?",
                (volume, tank_id)
            )
            
            conn.commit()
            conn.close()
            
            
            self.load_tanks_data()  
            self.load_logs_data()   
            
            
            self.clear_display()
            liters_input.clear()
            for radio_name in fuel_types:
                radio = self.findChild(QRadioButton, radio_name)
                if radio:
                    radio.setChecked(False)
            
            QMessageBox.information(self, "Успех", "Операция успешно записана")
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при записи операции: {str(e)}")
            if 'conn' in locals():
                conn.close()



        
    
    
    




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    init_database()
    app.setWindowIcon(QIcon("icon.ico"))
    
    auth_window = AuthWindow()
    auth_window.show()
    
    sys.exit(app.exec())