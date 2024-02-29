import sys
import AppLib

if __name__ == "__main__":
    process = AppLib.QtWidgets.QApplication(sys.argv)
    execution = AppLib.HWDPROC()
    sys.exit(process.exec())