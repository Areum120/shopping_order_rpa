import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 현재 스크립트의 디렉토리를 기준으로 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(current_dir, "gui", "order_excel_email_classify.ui")

        # UI 파일 로드
        uic.loadUi(ui_file, self)

        # 추가적인 초기화 코드
        self.initUI()

    def initUI(self):
        # UI 요소 초기화 및 이벤트 핸들러 연결
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
