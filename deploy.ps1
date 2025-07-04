# PowerShell script để deploy lên GitHub Pages
Write-Host "=== Deploy to GitHub Pages ===" -ForegroundColor Green

# Kiểm tra git repository
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    git branch -M main
}

# Format code trước khi deploy
Write-Host "Formatting code..." -ForegroundColor Yellow
black .
isort .

# Export static files
Write-Host "Exporting static site..." -ForegroundColor Yellow
python export_static.py

# Check if docs directory was created
if (-not (Test-Path "docs")) {
    Write-Host "❌ Failed to create static site" -ForegroundColor Red
    exit 1
}

# Add and commit changes
Write-Host "Committing changes..." -ForegroundColor Yellow
git add .
git commit -m "Deploy static site to GitHub Pages"

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
$remoteUrl = git config --get remote.origin.url
if (-not $remoteUrl) {
    Write-Host "⚠️  No remote repository configured." -ForegroundColor Yellow
    Write-Host "Please add your GitHub repository:" -ForegroundColor Yellow
    Write-Host "git remote add origin https://github.com/username/repository.git" -ForegroundColor Cyan
    exit 1
}

git push origin main

Write-Host "🎉 Deployed successfully!" -ForegroundColor Green
Write-Host "Your site will be available at: https://username.github.io/repository" -ForegroundColor Cyan
Write-Host "Note: It may take a few minutes for GitHub Pages to update." -ForegroundColor Yellow
