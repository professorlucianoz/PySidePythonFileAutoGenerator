import time
import os
import glob

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget, QFileDialog)

from PySide6.QtCore import QRunnable, Slot, QThreadPool

from ui_main import Ui_MainWindow



class Worker(QRunnable):
    def __init__(self, *args):
        super(Worker, self).__init__()
        self.args = args
        
        self.modifiedOn = os.path.getmtime(self.args[0])
    
    @Slot()
    def run(self):
        try:
            while (True):
                time.sleep(0.5)
                modified = os.path.getmtime(self.args[0])
                if modified != self.modifiedOn:
                    print("Modified")
                    self.modifiedOn = modified
                    self.recreate_python_file()
        except Exception as e:
            print(e)
            
    def recreate_python_file(self):
        ui_files = glob.glob("*.ui")
        
        for file in ui_files:
            os.system("pyside6-uic {} -o {}".format(file,  file.replace(".ui", ".py")))



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        self.ui_open_button.clicked.connect(self.open_ui_folder)
        self.python_open_button.clicked.connect(self.open_python_folder)
        
        self.start_button.clicked.connect(self.start)
    
    def start(self):
        if self.ui_edit.text() and self.python_edit.text():
            self.start_button.setEnabled(False)
            print("Start monitoring file changes") 
            self.threadpool = QThreadPool()
            worker = Worker(self.ui_edit.text(), self.python_edit.text())
            self.threadpool.start(worker)
        
    def open_ui_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getExistingDirectoryUrl(self, "Select UI Folder", QUrl(), options=options)
        
        self.ui_edit.setText(file.toLocalFile())
        
    def open_python_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getExistingDirectoryUrl(self, "Select Python Folder", QUrl(), options=options)
        
        self.python_edit.setText(file.toLocalFile())


app = QApplication([])

window = MainWindow()
window.show()

app.exec()