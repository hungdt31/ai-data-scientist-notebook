# PowerShell script để chạy Flask app
Write-Host "=== AI & Data Science Flask App ===" -ForegroundColor Green

# Kiểm tra Python
try {
    $pythonVersion = python --version
    Write-Host "Python version: $pythonVersion" -ForegroundColor Yellow
} catch {
    Write-Host "Python not found! Please install Python first." -ForegroundColor Red
    exit 1
}

# Tạo virtual environment nếu chưa tồn tại
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Kích hoạt virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Cài đặt dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Format code
Write-Host "Formatting Python code with Black..." -ForegroundColor Yellow
black .

Write-Host "Sorting imports with isort..." -ForegroundColor Yellow
isort .

Write-Host "Formatting HTML templates with djLint..." -ForegroundColor Yellow
djlint templates/ --reformat --profile jinja --indent 2 --max-line-length 80

Write-Host "Formatting CSS with custom formatter..." -ForegroundColor Yellow
python format_css.py static/style.css

Write-Host "Checking Python code with flake8..." -ForegroundColor Yellow
flake8 .

Write-Host "Checking HTML templates with djLint..." -ForegroundColor Yellow
djlint templates/ --check --profile jinja --max-line-length 80

# Chạy Flask app
Write-Host "Starting Flask application..." -ForegroundColor Green
Write-Host "App will be available at: http://localhost:5000" -ForegroundColor Cyan
python app.py
