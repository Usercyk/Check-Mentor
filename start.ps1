# 快速启动脚本 - PowerShell 版本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "学术开盒 - 环境检查与启动" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查虚拟环境
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "✓ 找到虚拟环境" -ForegroundColor Green
    Write-Host "激活虚拟环境..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠ 未找到虚拟环境" -ForegroundColor Yellow
    $createVenv = Read-Host "是否创建虚拟环境? (y/n)"
    
    if ($createVenv -eq "y") {
        Write-Host "创建虚拟环境..." -ForegroundColor Yellow
        python -m venv venv
        & .\venv\Scripts\Activate.ps1
        
        Write-Host "安装依赖..." -ForegroundColor Yellow
        pip install -r requirements.txt
    }
}

# 检查 .env 文件
if (!(Test-Path ".env")) {
    Write-Host "⚠ 未找到 .env 文件" -ForegroundColor Yellow
    Write-Host "从 .env.example 复制..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ 已创建 .env 文件，请编辑并填入 API Key" -ForegroundColor Green
    Write-Host ""
    $editNow = Read-Host "是否现在编辑 .env 文件? (y/n)"
    if ($editNow -eq "y") {
        notepad .env
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "选择启动方式:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Web 界面 (推荐)" -ForegroundColor Green
Write-Host "2. 命令行模式" -ForegroundColor Yellow
Write-Host "3. 退出" -ForegroundColor Red
Write-Host ""

$choice = Read-Host "请选择 (1/2/3)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "启动 Streamlit Web 应用..." -ForegroundColor Green
        streamlit run app.py
    }
    "2" {
        Write-Host ""
        $profName = Read-Host "请输入导师的英文姓名"
        python main.py $profName
    }
    "3" {
        Write-Host "再见!" -ForegroundColor Cyan
        exit
    }
    default {
        Write-Host "无效选择，退出" -ForegroundColor Red
    }
}
