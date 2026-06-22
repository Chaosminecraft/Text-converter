@echo off
nuitka --onefile --msvc=latest --assume-yes-for-download --show-anti-bloat-changes --lto=yes --include-data-dir="C:\Users\Volks\AppData\Local\Programs\Python\Python313\tcl\tcl8.6=tcl\tcl8.6" --include-data-dir="C:\Users\Volks\AppData\Local\Programs\Python\Python313\tcl\tk8.6=tcl\tk8.6" --enable-plugin=tk-inter TextConverter.py
rem nuitka --onefile --msvc=latest TextConverter.py
rem nuitka --onefile --msvc=latest --enable-plugin=pyqt6 --remove-output TextConverter.py
pasue