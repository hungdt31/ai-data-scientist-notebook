# Makefile cho Flask App
.PHONY: install format format-python format-html lint lint-python lint-html run clean help

# Cài đặt dependencies
install:
	pip install -r requirements.txt

# Format tất cả code
format: format-python format-html format-css

# Format Python code
format-python:
	black .
	isort .

# Format HTML templates
format-html:
	djlint templates/ --reformat --profile jinja --indent 2 --max-line-length 80

# Format CSS files
format-css:
	python format_css.py static/style.css

# Kiểm tra linting tất cả
lint: lint-python lint-html

# Kiểm tra Python linting
lint-python:
	flake8 .

# Kiểm tra HTML linting
lint-html:
	djlint templates/ --check --profile jinja --max-line-length 80

# Chạy ứng dụng
run:
	python app.py

# Dọn dẹp
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Chạy đầy đủ (format + lint + run)
dev: format lint run

# Hiển thị help
help:
	@echo "Available commands:"
	@echo "  install - Install dependencies"
	@echo "  format  - Format code with black and isort"
	@echo "  lint    - Check code with flake8"
	@echo "  run     - Run Flask application"
	@echo "  dev     - Format, lint, and run"
	@echo "  clean   - Clean up cache files"
	@echo "  help    - Show this help message"
