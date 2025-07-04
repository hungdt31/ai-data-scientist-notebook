@echo off
echo === AI ^& Data Science Flask App ===

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Please install Python first.
    pause
    exit /b 1
)

echo Python version:
python --version

REM Tạo virtual environment nếu chưa tồn tại
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Kích hoạt virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Cài đặt dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Format code
echo Formatting Python code with Black...
black .

echo Sorting imports with isort...
isort .

echo Formatting HTML templates with djLint...
djlint templates/ --reformat --profile jinja --indent 2 --max-line-length 80

echo Checking Python code with flake8...
flake8 .

echo Checking HTML templates with djLint...
djlint templates/ --check --profile jinja --max-line-length 80

REM Chạy Flask app
echo Starting Flask application...
echo App will be available at: http://localhost:5000
python app.py

pause
