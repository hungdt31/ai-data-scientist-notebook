#!/usr/bin/env powershell
# Manual GitHub Pages deployment script
Write-Host "=== Manual GitHub Pages Deployment ===" -ForegroundColor Green

# Format code
Write-Host "Formatting code..." -ForegroundColor Yellow
black .
isort .

# Export static site
Write-Host "Exporting static site..." -ForegroundColor Yellow
python export_static.py

# Check if docs directory exists
if (-not (Test-Path "docs")) {
    Write-Host "❌ Static site export failed" -ForegroundColor Red
    exit 1
}

# Create or switch to gh-pages branch
Write-Host "Setting up gh-pages branch..." -ForegroundColor Yellow
git checkout --orphan gh-pages 2>$null
if ($LASTEXITCODE -ne 0) {
    git checkout gh-pages 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create/switch to gh-pages branch" -ForegroundColor Red
        exit 1
    }
}

# Remove all files except docs
Write-Host "Cleaning gh-pages branch..." -ForegroundColor Yellow
Get-ChildItem -Path . -Exclude "docs", ".git" | Remove-Item -Recurse -Force

# Move docs content to root
Write-Host "Moving static files to root..." -ForegroundColor Yellow
Get-ChildItem -Path "docs" | Move-Item -Destination "."
Remove-Item "docs" -Recurse -Force

# Add and commit
Write-Host "Committing to gh-pages..." -ForegroundColor Yellow
git add .
git commit -m "Deploy static site to gh-pages - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

# Push to gh-pages
Write-Host "Pushing to gh-pages branch..." -ForegroundColor Yellow
git push origin gh-pages --force

# Switch back to main
Write-Host "Switching back to main branch..." -ForegroundColor Yellow
git checkout main

Write-Host "🎉 Manual deployment completed!" -ForegroundColor Green
Write-Host "Your site should be available at: https://username.github.io/repository-name" -ForegroundColor Cyan
Write-Host "Note: Configure GitHub Pages to use 'gh-pages' branch in Settings → Pages" -ForegroundColor Yellow
