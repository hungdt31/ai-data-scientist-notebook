#!/usr/bin/env powershell
# Manual GitHub Pages deployment script
Write-Host "=== Manual GitHub Pages Deployment ===" -ForegroundColor Green

# Save current branch
$currentBranch = git branch --show-current
Write-Host "Current branch: $currentBranch" -ForegroundColor Cyan

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

# Check if we have changes to commit in current branch
$hasChanges = git status --porcelain
if ($hasChanges) {
    Write-Host "Committing changes in main branch first..." -ForegroundColor Yellow
    git add .
    git commit -m "Update before deploying to gh-pages - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
}

# Create or switch to gh-pages branch
Write-Host "Setting up gh-pages branch..." -ForegroundColor Yellow

# Check if gh-pages branch exists
$ghPagesExists = git branch -a | Select-String "gh-pages"
if ($ghPagesExists) {
    Write-Host "Switching to existing gh-pages branch..." -ForegroundColor Yellow
    git checkout gh-pages
    git pull origin gh-pages 2>$null
    # Clean existing files
    Get-ChildItem -Path . -Exclude ".git" | Remove-Item -Recurse -Force
} else {
    Write-Host "Creating new gh-pages branch..." -ForegroundColor Yellow
    git checkout --orphan gh-pages
    git rm -rf . 2>$null
}

# Copy docs content to root
Write-Host "Copying static files to root..." -ForegroundColor Yellow
Copy-Item -Path "docs\*" -Destination "." -Recurse -Force

# Add and commit
Write-Host "Committing to gh-pages..." -ForegroundColor Yellow
git add .
git commit -m "Deploy static site to gh-pages - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

# Push to gh-pages
Write-Host "Pushing to gh-pages branch..." -ForegroundColor Yellow
git push origin gh-pages --force

# Switch back to original branch
Write-Host "Switching back to $currentBranch branch..." -ForegroundColor Yellow
git checkout $currentBranch

Write-Host "🎉 Manual deployment completed!" -ForegroundColor Green
Write-Host "Your site should be available at: https://username.github.io/repository-name" -ForegroundColor Cyan
Write-Host "Note: Configure GitHub Pages to use 'gh-pages' branch in Settings → Pages" -ForegroundColor Yellow
