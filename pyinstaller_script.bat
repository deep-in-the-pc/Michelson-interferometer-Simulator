pyinstaller main.py --clean --noconsole -y
rmdir /Q /S .\IDM\main
xcopy .\gui .\dist\main /E
move .\dist\main .\IDM
rmdir /Q /S .\build
rmdir /Q /S .\dist
rmdir /Q /S .\__pycache__
rm .\main.spec