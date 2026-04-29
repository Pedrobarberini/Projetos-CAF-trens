@echo off
echo ============================================
echo  Gerando PAV.exe com PyInstaller...
echo ============================================

cd /d "%~dp0"

pyinstaller --onefile ^
  --name PAV ^
  --add-data "data/raw/pedidos.csv;data/raw" ^
  --add-data "data/raw/produtos.csv;data/raw" ^
  --add-data "data/raw/clientes.csv;data/raw" ^
  --paths src ^
  src/main.py

echo.
echo ============================================
echo  Pronto! O .exe esta em: dist\PAV.exe
echo ============================================
pause
