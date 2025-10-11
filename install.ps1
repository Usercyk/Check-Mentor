# 安装依赖脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "学术开盒 - 依赖安装" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 创建虚拟环境
if (!(Test-Path ".\venv")) {
    Write-Host "创建虚拟环境..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ 虚拟环境创建完成" -ForegroundColor Green
} else {
    Write-Host "✓ 虚拟环境已存在" -ForegroundColor Green
}

# 激活虚拟环境
Write-Host "激活虚拟环境..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# 升级 pip
Write-Host "升级 pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# 安装依赖
Write-Host "安装项目依赖..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✓ 安装完成!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "下一步:" -ForegroundColor Yellow
Write-Host "1. 复制 .env.example 为 .env" -ForegroundColor White
Write-Host "2. 在 .env 中填入你的 OPENAI_API_KEY" -ForegroundColor White
Write-Host "3. 运行: .\start.ps1" -ForegroundColor White
Write-Host ""

# 检查并创建 .env
if (!(Test-Path ".env")) {
    $createEnv = Read-Host "是否现在创建 .env 文件? (y/n)"
    if ($createEnv -eq "y") {
        Copy-Item .env.example .env
        Write-Host "✓ 已创建 .env 文件" -ForegroundColor Green
        
        $editNow = Read-Host "是否现在编辑 .env 文件? (y/n)"
        if ($editNow -eq "y") {
            notepad .env
        }
    }
}
