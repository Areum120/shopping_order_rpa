# shopping_order_rpa Guide

### 필요 라이브러리 설치 

pip install -r requirements.txt

### exe 실행파일 Build
- -w : 콜솔창x -F : onefile 

cd 폴더 설치 경로

pyinstaller -w -F run.py

### build 완료 시

dist 폴더에 run.exe 파일 생성 확인

### app 실행

# 24.08.13 update
'pyinstaller'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다. 오류시 아래 참고

### 1. 설치 경로 찾기
python -m site --user-site

예를 들어 아래 경로로 나오면 아래 경로 Scripts 폴더 안에 설치 되어 있음.
C:\Users\USERNAME\AppData\Roaming\Python\PythonXX\site-packages

### 2. 확인한 설치 경로 /Scripts 경로 추가해서 아래 명령어로 설치 

C:\Users\USERNAME\AppData\Roaming\Python\PythonXX\Scripts\pyinstaller -w -F main.py

ui 경로를 찾을 수 없으면 아래 명령어로 설치

C:\Users\USERNAME\AppData\Roaming\Python\PythonXX\Scripts\pyinstaller --onefile --noconsole --add-data "gui/order_excel_email_classify.ui;gui" main.py


만약 import한 다른 py 파일을 못찾을 경우
프로젝트 루트 폴더 아래처럼 만들고 
main.py 실행 파일 따로 만들어서 main.py를 exe파일로 생성

### project_root/
### │
### ├── classi/
### │   ├── __init__.py
### │   ├── excel_clsfn.py
### │   ├── send_email.py
### │   ├── data_store.py
### │
### ── gui/
### │   ├── __init__.py
### │   ├── order_excel_email_classify.ui
### │
### └── main.py



