#!/usr/bin/env powershell
# Simple GitHub Pages deployment script
Write-Host "=== Simple GitHub Pages Deployment ===" -ForegroundColor Green

# Step 1: Export static site
Write-Host "Step 1: Exporting static site..." -ForegroundColor Yellow
python export_static.py

if (-not (Test-Path "docs")) {
    Write-Host "❌ Failed to export static site" -ForegroundColor Red
    exit 1
}

# Step 2: Check git status
Write-Host "Step 2: Checking git status..." -ForegroundColor Yellow
git status

# Step 3: Add and commit changes
Write-Host "Step 3: Adding and committing changes..." -ForegroundColor Yellow
git add .
git commit -m "Update static site - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

# Step 4: Push to main branch
Write-Host "Step 4: Pushing to main branch..." -ForegroundColor Yellow
git push origin main

Write-Host "🎉 Updated main branch!" -ForegroundColor Green
Write-Host "Now GitHub Actions will automatically deploy to gh-pages branch" -ForegroundColor Cyan
Write-Host "Check the Actions tab in your repository to see the deployment progress" -ForegroundColor Yellow
