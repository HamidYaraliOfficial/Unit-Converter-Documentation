# Unit Converter Documentation

## Persian (فارسی)

### معرفی پروژه
این پروژه یک اپلیکیشن تبدیل‌کننده واحد است که با استفاده از پایتون و کتابخانه PyQt6 برای رابط گرافیکی توسعه یافته است. این برنامه امکان تبدیل واحدهای مختلف از جمله دما، طول، وزن، مساحت و حجم را فراهم می‌کند. رابط کاربری حرفه‌ای با الهام از ویندوز 11 طراحی شده و از چهار تم (ویندوز، تاریک، قرمز و آبی) و چهار زبان (فارسی، انگلیسی، چینی و روسی) پشتیبانی می‌کند. این اپلیکیشن قابلیت‌هایی مانند نمایش تاریخچه تبدیل‌ها، ذخیره‌سازی تاریخچه و رابط کاربری چندزبانه با چیدمان راست‌چین و چپ‌چین را ارائه می‌دهد.

### ویژگی‌ها
- **تبدیل واحدهای متنوع**: پشتیبانی از تبدیل دما (سانتی‌گراد، فارنهایت، کلوین)، طول (متر، کیلومتر، مایل و غیره)، وزن (کیلوگرم، پوند و غیره)، مساحت (متر مربع، مایل مربع و غیره) و حجم (لیتر، گالن و غیره).
- **رابط کاربری چندزبانه**: پشتیبانی از زبان‌های فارسی، انگلیسی، چینی و روسی با چیدمان مناسب (راست‌چین برای فارسی).
- **تم‌های متنوع**: شامل تم‌های ویندوز 11، تاریک، قرمز و آبی با طراحی مدرن و جذاب.
- **تاریخچه تبدیل‌ها**: ذخیره و نمایش تاریخچه تبدیل‌ها با جزئیات (ورودی، نتیجه، تاریخ و دسته‌بندی).
- **ذخیره‌سازی تاریخچه**: امکان ذخیره تاریخچه تبدیل‌ها در فایل JSON.
- **کپی نتیجه**: امکان کپی کردن نتیجه تبدیل به کلیپ‌بورد.
- **طراحی حرفه‌ای**: رابط کاربری مشابه ویندوز 11 با انیمیشن‌ها و افکت‌های بصری زیبا.
- **ورودی معتبر**: اعتبارسنجی ورودی برای اطمینان از وارد کردن مقادیر عددی معتبر.

### پیش‌نیازها
- پایتون 3.8 یا بالاتر
- کتابخانه‌های مورد نیاز:
  - PyQt6 (`pip install PyQt6`)
- سیستم‌عامل: ویندوز یا لینوکس
- فایل آیکون (اختیاری): `icon.ico` برای نمایش در نوار عنوان

### نصب و راه‌اندازی
1. فایل `unit_converter.py` را در یک پوشه ذخیره کنید.
2. کتابخانه مورد نیاز را نصب کنید:
   ```bash
   pip install PyQt6
   ```
3. فایل را اجرا کنید:
   ```bash
   python unit_converter.py
   ```
4. در رابط کاربری، دسته‌بندی تبدیل، واحد مبدا، واحد مقصد و مقدار را انتخاب کرده و دکمه تبدیل را فشار دهید.

### ساختار فایل‌ها
- `unit_converter.py`: فایل اصلی حاوی کد پایتون و رابط گرافیکی.
- `conversion_history.json`: فایل ذخیره‌سازی تاریخچه تبدیل‌ها (به‌صورت خودکار ایجاد می‌شود).
- `icon.ico` (اختیاری): فایل آیکون برنامه برای نمایش در نوار عنوان.

### توسعه‌دهنده
توسعه‌یافته توسط حمید یارعلی  
- گیت‌هاب: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- اینستاگرام: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- تلگرام: [@Hamid_Yarali](https://t.me/Hamid_Yarali)

---

## English

### Project Overview
This project is a unit converter application developed using Python and the PyQt6 library for its graphical user interface. It enables users to convert various units, including temperature, length, weight, area, and volume. The application features a professional Windows 11-inspired interface, supports four themes (Windows, Dark, Red, and Blue), and four languages (Persian, English, Chinese, and Russian). It includes functionalities such as conversion history, history export to JSON, and a multilingual interface with proper right-to-left and left-to-right layouts.

### Features
- **Diverse Unit Conversions**: Supports conversions for temperature (Celsius, Fahrenheit, Kelvin), length (meter, kilometer, mile, etc.), weight (kilogram, pound, etc.), area (square meter, square mile, etc.), and volume (liter, gallon, etc.).
- **Multilingual Interface**: Supports Persian, English, Chinese, and Russian with appropriate layout directions (right-to-left for Persian).
- **Multiple Themes**: Includes Windows 11, Dark, Red, and Blue themes with a modern and attractive design.
- **Conversion History**: Stores and displays conversion history with details (input, result, date, and category).
- **History Export**: Allows saving conversion history to a JSON file.
- **Copy Result**: Enables copying the conversion result to the clipboard.
- **Professional Design**: Windows 11-inspired interface with smooth animations and visual effects.
- **Input Validation**: Ensures valid numerical input for accurate conversions.

### Requirements
- Python 3.8 or higher
- Required libraries:
  - PyQt6 (`pip install PyQt6`)
- Operating System: Windows or Linux
- Icon file (optional): `icon.ico` for the title bar

### Installation and Setup
1. Save the `unit_converter.py` file in a directory.
2. Install the required library:
   ```bash
   pip install PyQt6
   ```
3. Run the file:
   ```bash
   python unit_converter.py
   ```
4. In the interface, select the conversion category, source unit, target unit, and value, then click the convert button.

### File Structure
- `unit_converter.py`: Main file containing the Python code and GUI.
- `conversion_history.json`: File for storing conversion history (automatically created).
- `icon.ico` (optional): Application icon file for the title bar.

### Developer
Developed by Hamid Yarali  
- GitHub: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- Telegram: [@Hamid_Yarali](https://t.me/Hamid_Yarali)

---

## Chinese (中文)

### 项目简介
该项目是一个单位转换器应用程序，使用 Python 和 PyQt6 库开发，具备图形用户界面。它支持多种单位的转换，包括温度、长度、重量、面积和体积。该应用程序采用灵感来源于 Windows 11 的专业界面，支持四种主题（Windows、暗色、红色和蓝色）和四种语言（波斯语、英语、中文和俄语）。其功能包括转换历史记录、历史记录导出到 JSON 文件以及多语言界面，适配右到左和左到右的布局。

### 功能
- **多样化的单位转换**：支持温度（摄氏度、华氏度、开尔文）、长度（米、公里、英里等）、重量（千克、磅等）、面积（平方米、平方英里等）和体积（升、加仑等）的转换。
- **多语言界面**：支持波斯语、英语、中文和俄语，适配相应的布局方向（波斯语为右到左）。
- **多种主题**：包括 Windows 11、暗色、红色和蓝色主题，设计现代且吸引人。
- **转换历史**：存储并显示转换历史，包含详细信息（输入、结果、日期和类别）。
- **历史记录导出**：支持将转换历史保存到 JSON 文件。
- **复制结果**：允许将转换结果复制到剪贴板。
- **专业设计**：灵感来源于 Windows 11 的界面，带有流畅的动画和视觉效果。
- **输入验证**：确保输入有效的数字以进行准确的转换。

### 要求
- Python 3.8 或更高版本
- 所需库：
  - PyQt6 (`pip install PyQt6`)
- 操作系统：Windows 或 Linux
- 图标文件（可选）：`icon.ico` 用于标题栏

### 安装和设置
1. 将 `unit_converter.py` 文件保存在一个目录中。
2. 安装所需库：
   ```bash
   pip install PyQt6
   ```
3. 运行文件：
   ```bash
   python unit_converter.py
   ```
4. 在界面中选择转换类别、起始单位、目标单位和数值，然后点击转换按钮。

### 文件结构
- `unit_converter.py`：包含 Python 代码和图形用户界面的主文件。
- `conversion_history.json`：用于存储转换历史的文件（自动创建）。
- `icon.ico`（可选）：应用程序标题栏的图标文件。

### 开发者
由 Hamid Yarali 开发  
- GitHub: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- Telegram: [@Hamid_Yarali](https://t.me/Hamid_Yarali)