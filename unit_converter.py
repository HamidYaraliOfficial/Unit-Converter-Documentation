import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QComboBox, QTextEdit, QLabel, QStyleFactory, QTabWidget,
    QGridLayout, QScrollArea, QMenuBar, QMenu, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPalette, QColor, QFont
import json
import datetime
from pathlib import Path

# Developed by Hamid Yarali
# GitHub: https://github.com/HamidYaraliOfficial
# Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==
# Telegram: @Hamid_Yarali

class UnitConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unit Converter")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.ico'))  # Assuming an icon file exists
        
        # Language and theme settings
        self.current_lang = 'en'
        self.current_theme = 'Windows'
        self.conversion_history = []
        self.load_history()
        
        # Language dictionaries
        self.texts = {
            'en': {
                'title': 'Unit Converter',
                'category_label': 'Conversion Category:',
                'from_unit_label': 'From Unit:',
                'to_unit_label': 'To Unit:',
                'value_label': 'Value:',
                'convert_btn': 'Convert',
                'history_tab': 'Conversion History',
                'settings_tab': 'Settings',
                'language_label': 'Language:',
                'theme_label': 'Theme:',
                'clear_history': 'Clear History',
                'status_idle': 'Ready to convert...',
                'status_converted': 'Result: {result}',
                'status_error': 'Error: {error}',
                'history_input': 'Input',
                'history_result': 'Result',
                'history_date': 'Date',
                'history_category': 'Category',
                'save_history': 'Save History to File',
                'apply': 'Apply',
                'file_menu': 'File',
                'exit_action': 'Exit',
                'about': 'About',
                'about_text': 'Unit Converter\nVersion 1.0\nDeveloped by Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': 'Copy Result',
                'invalid_input': 'Please enter a valid number!',
                'categories': {
                    'temperature': 'Temperature',
                    'length': 'Length',
                    'weight': 'Weight',
                    'area': 'Area',
                    'volume': 'Volume'
                },
                'units': {
                    'temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
                    'length': ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
                    'weight': ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce'],
                    'area': ['Square Meter', 'Square Kilometer', 'Square Centimeter', 'Square Mile', 'Square Yard'],
                    'volume': ['Liter', 'Milliliter', 'Cubic Meter', 'Gallon', 'Quart']
                }
            },
            'fa': {
                'title': 'تبدیل‌کننده واحد',
                'category_label': 'دسته‌بندی تبدیل:',
                'from_unit_label': 'واحد مبدا:',
                'to_unit_label': 'واحد مقصد:',
                'value_label': 'مقدار:',
                'convert_btn': 'تبدیل',
                'history_tab': 'تاریخچه تبدیل',
                'settings_tab': 'تنظیمات',
                'language_label': 'زبان:',
                'theme_label': 'تم:',
                'clear_history': 'پاک کردن تاریخچه',
                'status_idle': 'آماده برای تبدیل...',
                'status_converted': 'نتیجه: {result}',
                'status_error': 'خطا: {error}',
                'history_input': 'ورودی',
                'history_result': 'نتیجه',
                'history_date': 'تاریخ',
                'history_category': 'دسته‌بندی',
                'save_history': 'ذخیره تاریخچه در فایل',
                'apply': 'اعمال',
                'file_menu': 'فایل',
                'exit_action': 'خروج',
                'about': 'درباره',
                'about_text': 'تبدیل‌کننده واحد\nنسخه 1.0\nتوسعه‌یافته توسط حمید یارعلی\nگیت‌هاب: https://github.com/HamidYaraliOfficial\nاینستاگرام: https://www.instagram.com/hamidyaraliofficial\nتلگرام: @Hamid_Yarali',
                'copy_btn': 'کپی نتیجه',
                'invalid_input': 'لطفاً یک عدد معتبر وارد کنید!',
                'categories': {
                    'temperature': 'دما',
                    'length': 'طول',
                    'weight': 'وزن',
                    'area': 'مساحت',
                    'volume': 'حجم'
                },
                'units': {
                    'temperature': ['سانتی‌گراد', 'فارنهایت', 'کلوین'],
                    'length': ['متر', 'کیلومتر', 'سانتی‌متر', 'میلی‌متر', 'مایل', 'یارد', 'فوت', 'اینچ'],
                    'weight': ['کیلوگرم', 'گرم', 'میلی‌گرم', 'پوند', 'اونس'],
                    'area': ['متر مربع', 'کیلومتر مربع', 'سانتی‌متر مربع', 'مایل مربع', 'یارد مربع'],
                    'volume': ['لیتر', 'میلی‌لیتر', 'متر مکعب', 'گالن', 'کوارتر']
                }
            },
            'zh': {
                'title': '单位转换器',
                'category_label': '转换类别：',
                'from_unit_label': '起始单位：',
                'to_unit_label': '目标单位：',
                'value_label': '数值：',
                'convert_btn': '转换',
                'history_tab': '转换历史',
                'settings_tab': '设置',
                'language_label': '语言：',
                'theme_label': '主题：',
                'clear_history': '清除历史记录',
                'status_idle': '准备转换...',
                'status_converted': '结果：{result}',
                'status_error': '错误：{error}',
                'history_input': '输入',
                'history_result': '结果',
                'history_date': '日期',
                'history_category': '类别',
                'save_history': '将历史记录保存到文件',
                'apply': '应用',
                'file_menu': '文件',
                'exit_action': '退出',
                'about': '关于',
                'about_text': '单位转换器\n版本 1.0\n由 Hamid Yarali 开发\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': '复制结果',
                'invalid_input': '请输入有效的数字！',
                'categories': {
                    'temperature': '温度',
                    'length': '长度',
                    'weight': '重量',
                    'area': '面积',
                    'volume': '体积'
                },
                'units': {
                    'temperature': ['摄氏度', '华氏度', '开尔文'],
                    'length': ['米', '公里', '厘米', '毫米', '英里', '码', '英尺', '英寸'],
                    'weight': ['千克', '克', '毫克', '磅', '盎司'],
                    'area': ['平方米', '平方公里', '平方厘米', '平方英里', '平方码'],
                    'volume': ['升', '毫升', '立方米', '加仑', '夸脱']
                }
            },
            'ru': {
                'title': 'Конвертер единиц',
                'category_label': 'Категория преобразования:',
                'from_unit_label': 'Из единицы:',
                'to_unit_label': 'В единицу:',
                'value_label': 'Значение:',
                'convert_btn': 'Конвертировать',
                'history_tab': 'История преобразований',
                'settings_tab': 'Настройки',
                'language_label': 'Язык:',
                'theme_label': 'Тема:',
                'clear_history': 'Очистить историю',
                'status_idle': 'Готово к преобразованию...',
                'status_converted': 'Результат: {result}',
                'status_error': 'Ошибка: {error}',
                'history_input': 'Ввод',
                'history_result': 'Результат',
                'history_date': 'Дата',
                'history_category': 'Категория',
                'save_history': 'Сохранить историю в файл',
                'apply': 'Применить',
                'file_menu': 'Файл',
                'exit_action': 'Выход',
                'about': 'О программе',
                'about_text': 'Конвертер единиц\nВерсия 1.0\nРазработано Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': 'Копировать результат',
                'invalid_input': 'Пожалуйста, введите действительное число!',
                'categories': {
                    'temperature': 'Температура',
                    'length': 'Длина',
                    'weight': 'Вес',
                    'area': 'Площадь',
                    'volume': 'Объем'
                },
                'units': {
                    'temperature': ['Цельсий', 'Фаренгейт', 'Кельвин'],
                    'length': ['Метр', 'Километр', 'Сантиметр', 'Миллиметр', 'Миля', 'Ярд', 'Фут', 'Дюйм'],
                    'weight': ['Килограмм', 'Грамм', 'Миллиграмм', 'Фунт', 'Унция'],
                    'area': ['Квадратный метр', 'Квадратный километр', 'Квадратный сантиметр', 'Квадратная миля', 'Квадратный ярд'],
                    'volume': ['Литр', 'Миллилитр', 'Кубический метр', 'Галлон', 'Кварта']
                }
            }
        }

        # Theme dictionaries
        self.themes = {
            'Windows': {
                'background': QColor(245, 245, 245),
                'text': QColor(0, 0, 0),
                'button': QColor(230, 230, 230),
                'button_text': QColor(0, 0, 0),
                'button_hover': QColor(200, 200, 200),
                'accent': QColor(0, 120, 212),
                'border': QColor(180, 180, 180),
                'header': QColor(220, 220, 220)
            },
            'Dark': {
                'background': QColor(32, 32, 32),
                'text': QColor(230, 230, 230),
                'button': QColor(50, 50, 50),
                'button_text': QColor(230, 230, 230),
                'button_hover': QColor(70, 70, 70),
                'accent': QColor(0, 120, 212),
                'border': QColor(80, 80, 80),
                'header': QColor(40, 40, 40)
            },
            'Red': {
                'background': QColor(255, 235, 235),
                'text': QColor(80, 0, 0),
                'button': QColor(255, 200, 200),
                'button_text': QColor(80, 0, 0),
                'button_hover': QColor(255, 180, 180),
                'accent': QColor(200, 0, 0),
                'border': QColor(220, 150, 150),
                'header': QColor(255, 220, 220)
            },
            'Blue': {
                'background': QColor(235, 245, 255),
                'text': QColor(0, 0, 80),
                'button': QColor(200, 220, 255),
                'button_text': QColor(0, 0, 80),
                'button_hover': QColor(180, 200, 255),
                'accent': QColor(0, 0, 200),
                'border': QColor(150, 180, 220),
                'header': QColor(220, 235, 255)
            }
        }

        # Initialize UI
        self.init_ui()
        self.apply_theme(self.current_theme)
        self.update_texts()

    def init_ui(self):
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Menu bar
        self.menu_bar = QMenuBar()
        self.file_menu = QMenu(self.texts['en']['file_menu'])
        self.exit_action = self.file_menu.addAction(self.texts['en']['exit_action'])
        self.exit_action.triggered.connect(self.close)
        self.about_action = self.file_menu.addAction(self.texts['en']['about'])
        self.about_action.triggered.connect(self.show_about)
        self.menu_bar.addMenu(self.file_menu)
        self.main_layout.addWidget(self.menu_bar)

        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
            QTabBar::tab {
                padding: 10px 20px;
                margin-right: 5px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                background: rgba(0, 0, 0, 0.05);
                color: black;
            }
            QTabBar::tab:selected {
                background: rgba(0, 120, 212, 0.3);
                font-weight: bold;
                color: black;
            }
        """)
        self.main_layout.addWidget(self.tabs)

        # Converter tab
        self.converter_tab = QWidget()
        self.converter_layout = QVBoxLayout(self.converter_tab)
        self.converter_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.converter_layout.setSpacing(10)

        # Conversion category
        self.category_label = QLabel()
        self.category_label.setFont(QFont("Segoe UI", 12))
        self.category_combo = QComboBox()
        self.category_combo.addItems(list(self.texts['en']['categories'].values()))
        self.category_combo.setFixedHeight(40)
        self.category_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.category_combo.currentIndexChanged.connect(self.update_units)

        # From and To units
        self.from_unit_label = QLabel()
        self.from_unit_label.setFont(QFont("Segoe UI", 12))
        self.from_unit_combo = QComboBox()
        self.from_unit_combo.setFixedHeight(40)
        self.from_unit_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        self.to_unit_label = QLabel()
        self.to_unit_label.setFont(QFont("Segoe UI", 12))
        self.to_unit_combo = QComboBox()
        self.to_unit_combo.setFixedHeight(40)
        self.to_unit_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        # Value input
        self.value_label = QLabel()
        self.value_label.setFont(QFont("Segoe UI", 12))
        self.value_input = QLineEdit()
        self.value_input.setFixedHeight(40)
        self.value_input.setStyleSheet("""
            QLineEdit {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Convert button
        self.convert_btn = QPushButton()
        self.convert_btn.setFixedHeight(50)
        self.convert_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.convert_btn.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
            QPushButton:disabled {
                background: rgba(0, 120, 212, 0.5);
                color: rgba(255, 255, 255, 0.7);
            }
        """)
        self.convert_btn.clicked.connect(self.convert)

        # Copy button
        self.copy_btn = QPushButton()
        self.copy_btn.setFixedHeight(40)
        self.copy_btn.setFont(QFont("Segoe UI", 12))
        self.copy_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.copy_btn.clicked.connect(self.copy_to_clipboard)

        # Result output
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)
        self.result_output.setFixedHeight(40)
        self.result_output.setStyleSheet("""
            QLineEdit {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Status text
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setFixedHeight(120)
        self.status_text.setStyleSheet("""
            QTextEdit {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Layout for converter tab
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.category_label)
        input_layout.addWidget(self.category_combo)
        input_layout.addWidget(self.from_unit_label)
        input_layout.addWidget(self.from_unit_combo)
        input_layout.addWidget(self.to_unit_label)
        input_layout.addWidget(self.to_unit_combo)
        input_layout.addWidget(self.value_label)
        input_layout.addWidget(self.value_input)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_output)
        result_layout.addWidget(self.copy_btn)

        self.converter_layout.addLayout(input_layout)
        self.converter_layout.addWidget(self.convert_btn)
        self.converter_layout.addLayout(result_layout)
        self.converter_layout.addWidget(self.status_text)

        # History tab
        self.history_tab = QWidget()
        self.history_layout = QVBoxLayout(self.history_tab)
        self.history_scroll = QScrollArea()
        self.history_scroll.setWidgetResizable(True)
        self.history_content = QWidget()
        self.history_grid = QGridLayout(self.history_content)
        self.history_grid.setSpacing(10)
        self.history_scroll.setWidget(self.history_content)
        self.history_scroll.setStyleSheet("""
            QScrollArea {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
        """)
        self.clear_history_btn = QPushButton()
        self.clear_history_btn.setFixedHeight(40)
        self.clear_history_btn.setFont(QFont("Segoe UI", 12))
        self.clear_history_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(200, 0, 0, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(200, 0, 0, 1.0);
            }
        """)
        self.clear_history_btn.clicked.connect(self.clear_history)
        self.save_history_btn = QPushButton()
        self.save_history_btn.setFixedHeight(40)
        self.save_history_btn.setFont(QFont("Segoe UI", 12))
        self.save_history_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.save_history_btn.clicked.connect(self.save_history_to_file)
        self.history_layout.addWidget(self.history_scroll)
        self.history_layout.addWidget(self.clear_history_btn)
        self.history_layout.addWidget(self.save_history_btn)

        # Settings tab
        self.settings_tab = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_tab)
        self.settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.settings_layout.setSpacing(10)

        self.language_label = QLabel()
        self.language_label.setFont(QFont("Segoe UI", 12))
        self.language_combo = QComboBox()
        self.language_combo.addItems(['English', 'فارسی', '中文', 'Русский'])
        self.language_combo.setFixedHeight(40)
        self.language_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.language_combo.currentIndexChanged.connect(self.change_language)

        self.theme_label = QLabel()
        self.theme_label.setFont(QFont("Segoe UI", 12))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Windows', 'Dark', 'Red', 'Blue'])
        self.theme_combo.setFixedHeight(40)
        self.theme_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        self.apply_btn = QPushButton()
        self.apply_btn.setFixedHeight(40)
        self.apply_btn.setFont(QFont("Segoe UI", 12))
        self.apply_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.apply_btn.clicked.connect(self.apply_settings)

        self.settings_layout.addWidget(self.language_label)
        self.settings_layout.addWidget(self.language_combo)
        self.settings_layout.addWidget(self.theme_label)
        self.settings_layout.addWidget(self.theme_combo)
        self.settings_layout.addWidget(self.apply_btn)
        self.settings_layout.addStretch()

        # Add tabs
        self.tabs.addTab(self.converter_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.history_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.settings_tab, self.texts['en']['settings_tab'])

        # Initialize units
        self.update_units()

        # Load history to UI
        self.update_history_ui()

    def apply_theme(self, theme_name):
        palette = QPalette()
        theme = self.themes.get(theme_name, self.themes['Windows'])
        palette.setColor(QPalette.ColorRole.Window, theme['background'])
        palette.setColor(QPalette.ColorRole.WindowText, theme['text'])
        palette.setColor(QPalette.ColorRole.Button, theme['button'])
        palette.setColor(QPalette.ColorRole.ButtonText, theme['button_text'])
        palette.setColor(QPalette.ColorRole.Highlight, theme['accent'])
        palette.setColor(QPalette.ColorRole.Base, theme['background'])
        palette.setColor(QPalette.ColorRole.AlternateBase, theme['header'])
        palette.setColor(QPalette.ColorRole.Text, theme['text'])
        self.setPalette(palette)
        self.setStyle(QStyleFactory.create('WindowsVista' if theme_name == 'Windows' else 'Fusion'))

    def update_texts(self):
        lang = self.current_lang
        self.setWindowTitle(self.texts[lang]['title'])
        self.category_label.setText(self.texts[lang]['category_label'])
        self.from_unit_label.setText(self.texts[lang]['from_unit_label'])
        self.to_unit_label.setText(self.texts[lang]['to_unit_label'])
        self.value_label.setText(self.texts[lang]['value_label'])
        self.convert_btn.setText(self.texts[lang]['convert_btn'])
        self.copy_btn.setText(self.texts[lang]['copy_btn'])
        self.status_text.setText(self.texts[lang]['status_idle'])
        self.clear_history_btn.setText(self.texts[lang]['clear_history'])
        self.save_history_btn.setText(self.texts[lang]['save_history'])
        self.language_label.setText(self.texts[lang]['language_label'])
        self.theme_label.setText(self.texts[lang]['theme_label'])
        self.apply_btn.setText(self.texts[lang]['apply'])
        self.file_menu.setTitle(self.texts[lang]['file_menu'])
        self.exit_action.setText(self.texts[lang]['exit_action'])
        self.about_action.setText(self.texts[lang]['about'])
        self.tabs.setTabText(0, self.texts[lang]['history_tab'])
        self.tabs.setTabText(1, self.texts[lang]['history_tab'])
        self.tabs.setTabText(2, self.texts[lang]['settings_tab'])

        # Update category combo
        current_category = self.category_combo.currentText()
        self.category_combo.clear()
        self.category_combo.addItems(list(self.texts[lang]['categories'].values()))
        if current_category:
            index = list(self.texts['en']['categories'].values()).index(current_category) if current_category in self.texts['en']['categories'].values() else 0
            self.category_combo.setCurrentIndex(index)
        self.update_units()

        # Set text alignment
        alignment = Qt.AlignmentFlag.AlignRight if lang == 'fa' else Qt.AlignmentFlag.AlignLeft
        self.category_label.setAlignment(alignment)
        self.from_unit_label.setAlignment(alignment)
        self.to_unit_label.setAlignment(alignment)
        self.value_label.setAlignment(alignment)
        self.language_label.setAlignment(alignment)
        self.theme_label.setAlignment(alignment)

    def change_language(self, index):
        langs = ['en', 'fa', 'zh', 'ru']
        self.current_lang = langs[index]
        self.update_texts()
        self.update_history_ui()

    def change_theme(self, index):
        themes = ['Windows', 'Dark', 'Red', 'Blue']
        self.current_theme = themes[index]
        self.apply_theme(self.current_theme)

    def apply_settings(self):
        self.update_texts()
        self.apply_theme(self.current_theme)

    def show_about(self):
        QMessageBox.information(self, self.texts[self.current_lang]['about'], 
                               self.texts[self.current_lang]['about_text'])

    def update_units(self):
        category_index = self.category_combo.currentIndex()
        category = list(self.texts['en']['categories'].keys())[category_index]
        units = self.texts[self.current_lang]['units'][category]
        self.from_unit_combo.clear()
        self.to_unit_combo.clear()
        self.from_unit_combo.addItems(units)
        self.to_unit_combo.addItems(units)
        self.to_unit_combo.setCurrentIndex(1 if len(units) > 1 else 0)

    def convert(self):
        try:
            value = float(self.value_input.text())
        except ValueError:
            self.status_text.setText(self.texts[self.current_lang]['status_error'].format(error=self.texts[self.current_lang]['invalid_input']))
            return

        category_index = self.category_combo.currentIndex()
        category = list(self.texts['en']['categories'].keys())[category_index]
        from_unit = self.from_unit_combo.currentText()
        to_unit = self.to_unit_combo.currentText()

        if from_unit == to_unit:
            result = value
        else:
            result = self.perform_conversion(category, from_unit, to_unit, value)

        result_str = f"{result:.6f}".rstrip('0').rstrip('.')
        self.result_output.setText(f"{result_str} {to_unit}")
        self.status_text.setText(self.texts[self.current_lang]['status_converted'].format(result=f"{result_str} {to_unit}"))

        # Save to history
        self.add_to_history(value, from_unit, to_unit, result_str, category)

    def perform_conversion(self, category, from_unit, to_unit, value):
        # Temperature conversions
        if category == 'temperature':
            if from_unit == self.texts['en']['units']['temperature'][0]:  # Celsius
                if to_unit == self.texts['en']['units']['temperature'][1]:  # Fahrenheit
                    return (value * 9/5) + 32
                elif to_unit == self.texts['en']['units']['temperature'][2]:  # Kelvin
                    return value + 273.15
            elif from_unit == self.texts['en']['units']['temperature'][1]:  # Fahrenheit
                if to_unit == self.texts['en']['units']['temperature'][0]:  # Celsius
                    return (value - 32) * 5/9
                elif to_unit == self.texts['en']['units']['temperature'][2]:  # Kelvin
                    return (value - 32) * 5/9 + 273.15
            elif from_unit == self.texts['en']['units']['temperature'][2]:  # Kelvin
                if to_unit == self.texts['en']['units']['temperature'][0]:  # Celsius
                    return value - 273.15
                elif to_unit == self.texts['en']['units']['temperature'][1]:  # Fahrenheit
                    return (value - 273.15) * 9/5 + 32

        # Length conversions (to meters)
        length_to_meters = {
            'Meter': 1,
            'Kilometer': 1000,
            'Centimeter': 0.01,
            'Millimeter': 0.001,
            'Mile': 1609.34,
            'Yard': 0.9144,
            'Foot': 0.3048,
            'Inch': 0.0254
        }
        if category == 'length':
            meters = value * length_to_meters[from_unit]
            return meters / length_to_meters[to_unit]

        # Weight conversions (to kilograms)
        weight_to_kg = {
            'Kilogram': 1,
            'Gram': 0.001,
            'Milligram': 0.000001,
            'Pound': 0.453592,
            'Ounce': 0.0283495
        }
        if category == 'weight':
            kg = value * weight_to_kg[from_unit]
            return kg / weight_to_kg[to_unit]

        # Area conversions (to square meters)
        area_to_sqm = {
            'Square Meter': 1,
            'Square Kilometer': 1000000,
            'Square Centimeter': 0.0001,
            'Square Mile': 2589988.11,
            'Square Yard': 0.836127
        }
        if category == 'area':
            sqm = value * area_to_sqm[from_unit]
            return sqm / area_to_sqm[to_unit]

        # Volume conversions (to liters)
        volume_to_liter = {
            'Liter': 1,
            'Milliliter': 0.001,
            'Cubic Meter': 1000,
            'Gallon': 3.78541,
            'Quart': 0.946353
        }
        if category == 'volume':
            liter = value * volume_to_liter[from_unit]
            return liter / volume_to_liter[to_unit]

        return value

    def copy_to_clipboard(self):
        result = self.result_output.text()
        if result:
            QApplication.clipboard().setText(result)
            self.status_text.setText(self.texts[self.current_lang]['status_converted'].format(result=result + " (Copied to clipboard)"))

    def add_to_history(self, input_value, from_unit, to_unit, result, category):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversion_history.append({
            'input': f"{input_value} {from_unit}",
            'result': f"{result} {to_unit}",
            'date': timestamp,
            'category': self.texts[self.current_lang]['categories'][category]
        })
        self.save_history()
        self.update_history_ui()

    def save_history(self):
        with open('conversion_history.json', 'w', encoding='utf-8') as f:
            json.dump(self.conversion_history, f, ensure_ascii=False, indent=4)

    def load_history(self):
        try:
            with open('conversion_history.json', 'r', encoding='utf-8') as f:
                self.conversion_history = json.load(f)
        except FileNotFoundError:
            self.conversion_history = []

    def save_history_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, self.texts[self.current_lang]['save_history'], "", "JSON Files (*.json)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.conversion_history, f, ensure_ascii=False, indent=4)
            self.status_text.setText(self.texts[self.current_lang]['status_converted'].format(result="History saved to file"))

    def update_history_ui(self):
        # Clear existing widgets
        for i in reversed(range(self.history_grid.count())):
            self.history_grid.itemAt(i).widget().setParent(None)

        # Add headers
        headers = [
            self.texts[self.current_lang]['history_input'],
            self.texts[self.current_lang]['history_result'],
            self.texts[self.current_lang]['history_date'],
            self.texts[self.current_lang]['history_category']
        ]
        for col, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: black;")
            label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            self.history_grid.addWidget(label, 0, col)

        # Add history items
        for row, item in enumerate(self.conversion_history, 1):
            input_label = QLabel(item['input'])
            result_label = QLabel(item['result'])
            date_label = QLabel(item['date'])
            category_label = QLabel(item['category'])
            
            for label in [input_label, result_label, date_label, category_label]:
                label.setStyleSheet("font-size: 12px; padding: 5px; border-bottom: 1px solid rgba(0, 0, 0, 0.1); color: black;")
                label.setWordWrap(True)
                label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            
            self.history_grid.addWidget(input_label, row, 0)
            self.history_grid.addWidget(result_label, row, 1)
            self.history_grid.addWidget(date_label, row, 2)
            self.history_grid.addWidget(category_label, row, 3)

    def clear_history(self):
        self.conversion_history = []
        self.save_history()
        self.update_history_ui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = UnitConverter()
    window.show()
    sys.exit(app.exec())