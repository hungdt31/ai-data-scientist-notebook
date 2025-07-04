# AI & Data Science Flask Application

## Giới thiệu

Ứng dụng web Flask với navigation đầy đủ cho AI & Data Science, bao gồm:
- Trang chủ với thông tin cá nhân
- Trang về chúng tôi
- Trang dịch vụ
- Trang liên hệ

## Cài đặt và chạy ứng dụng

### Cách 1: Sử dụng PowerShell Script (Khuyến nghị)
```powershell
# Chạy file PowerShell script
.\run_app.ps1
```

### Cách 2: Sử dụng Batch File
```cmd
# Chạy file batch
run_app.bat
```

### Cách 3: Chạy thủ công
```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Format code
black .
isort .

# Kiểm tra linting
flake8 .

# Chạy ứng dụng
python app.py
```

### Cách 4: Sử dụng Makefile
```bash
# Cài đặt dependencies
make install

# Format code
make format

# Kiểm tra linting
make lint

# Chạy ứng dụng
make run

# Hoặc chạy tất cả (format + lint + run)
make dev
```

## Công cụ Code Quality

### Code Formatting
- **Black**: Auto-format Python code
- **isort**: Sắp xếp imports
- **djLint**: Format HTML templates (Jinja2)
- **Prettier**: Format CSS, JavaScript, JSON

### Code Linting
- **flake8**: Kiểm tra code style và lỗi Python
- **djLint**: Kiểm tra HTML templates

### Node.js Tools (Optional)
```bash
# Cài đặt Node.js dependencies
npm install

# Format với Prettier
npm run format
npm run format-html
npm run format-css
```

### Cấu hình
- `pyproject.toml`: Cấu hình Black
- `.isort.cfg`: Cấu hình isort
- `.flake8`: Cấu hình flake8
- `.prettierrc`: Cấu hình Prettier
- `package.json`: Node.js dependencies và scripts
- `.vscode/settings.json`: Cấu hình VS Code auto-format

## Các lệnh format riêng biệt

### Python
```bash
black .                    # Format Python code
isort .                    # Sort imports
flake8 .                   # Check linting
```

### HTML Templates
```bash
djlint templates/ --reformat --profile jinja     # Format HTML
djlint templates/ --check --profile jinja        # Check HTML
```

### CSS
```bash
djlint static/style.css --reformat --profile jinja   # Format CSS
```

## Cấu trúc dự án

```
AI_DS_Resources/
├── app.py              # Flask application chính
├── requirements.txt    # Python dependencies
├── run_app.ps1        # PowerShell script
├── run_app.bat        # Batch script
├── Makefile           # Make commands
├── pyproject.toml     # Black configuration
├── .isort.cfg         # isort configuration
├── .flake8            # flake8 configuration
├── templates/         # HTML templates
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   └── contact.html
└── static/
    └── style.css      # CSS styling
```

## Features

- ✅ Responsive navigation menu
- ✅ Modern UI design
- ✅ Template inheritance
- ✅ Dynamic content rendering
- ✅ Code formatting với Black
- ✅ Import sorting với isort
- ✅ Code linting với flake8
- ✅ Auto-format trong VS Code

## Truy cập ứng dụng

Sau khi chạy, truy cập: http://localhost:5000

## Lời tâm sự

> "Không biết tôi sẽ đi đến đâu, nhưng còn thở là còn gỡ!"
> "Tôi phải kiếm tiền để sống và tiếp tục đam mê."
> "Có những mối tình đã qua, tôi có buồn và hối hận đôi phần."
> "Trên đường đời tấp nập, mong rằng vấp ngã vẫn còn răng. 🌼🌷🌹"

## Tutorial

Không biết học sao nữa, follow theo ROADMAP của [https://roadmap.sh](https://roadmap.sh) vậy, chỗ này làm theo các hướng dẫn của người đi trước (freecodecamp, AIO, etc).

## GitHub Pages Deployment

### Tự động deploy với GitHub Actions

1. **Tạo repository trên GitHub:**
   ```bash
   # Tạo repository mới trên GitHub
   # Ví dụ: https://github.com/username/ai-ds-resources
   ```

2. **Kết nối với GitHub repository:**
   ```bash
   git remote add origin https://github.com/username/ai-ds-resources.git
   git branch -M main
   git push -u origin main
   ```

3. **Cấu hình GitHub Pages:**
   - Vào Settings của repository
   - Chọn Pages từ sidebar
   - Source: GitHub Actions (thay vì Deploy from a branch)
   - Nhấn Save

4. **Tự động deploy:**
   - Mỗi khi push code lên main branch
   - GitHub Actions sẽ tự động build và deploy
   - Site sẽ có tại: `https://username.github.io/repository-name`

### Deploy thủ công với PowerShell

```powershell
# Chạy script deploy
.\deploy.ps1
```

### Export static site

```bash
# Export Flask app thành static HTML
python export_static.py
```

### Cấu trúc deploy

```
docs/                   # Static site cho GitHub Pages
├── index.html         # Trang chủ
├── about.html         # Trang về chúng tôi
├── services.html      # Trang dịch vụ
├── contact.html       # Trang liên hệ
└── static/            # CSS, JS, images
    └── style.css
```

### Files quan trọng cho deploy

- `export_static.py`: Script export Flask thành static HTML
- `deploy.ps1`: PowerShell script cho deploy
- `.github/workflows/deploy.yml`: GitHub Actions workflow
- `docs/`: Output directory cho GitHub Pages

### Troubleshooting

#### GitHub Actions Deployment Issues

1. **Linting Errors:**
   ```bash
   # Sửa lỗi linting trước khi deploy
   black .
   isort .
   flake8 .
   ```

2. **GitHub Pages Settings:**
   - Vào Settings → Pages
   - Source: GitHub Actions (không phải Deploy from a branch)
   - Repository phải là public hoặc có GitHub Pro/Enterprise

3. **Permission Issues:**
   - Vào Settings → Actions → General
   - Workflow permissions: Read and write permissions
   - Allow GitHub Actions to create and approve pull requests: ✅

3. **Common Issues:**
   - Đảm bảo repository là public hoặc có GitHub Pro
   - Kiểm tra file `.github/workflows/deploy.yml` có đúng syntax
   - Thư mục `docs/` phải có trong repository

#### Local Development Issues

1. **PowerShell Execution Policy:**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Static Site Generation:**
   ```bash
   python export_static.py
   ```

### Code Quality Checks

- **Black**: Code formatting
- **isort**: Import sorting  
- **flake8**: Linting và style checks
- **djLint**: HTML template formatting

### Repository Structure for GitHub Pages

```
repository/
├── docs/              # GitHub Pages source
│   ├── index.html     # Generated static files
│   ├── about.html
│   ├── services.html
│   ├── contact.html
│   └── static/
│       └── style.css
├── .github/
│   └── workflows/
│       └── deploy.yml # GitHub Actions
├── templates/         # Flask templates
├── static/           # Flask static files
└── app.py           # Flask application
```
