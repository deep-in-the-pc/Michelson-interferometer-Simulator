pyinstaller main.py --clean --noconsole -y
rmdir /Q /S .\IDM\main
mkdir .\dist\main\gui
xcopy .\gui .\dist\main\gui /E
move .\dist\main .\IDM
rmdir /Q /S .\build
rmdir /Q /S .\dist
rmdir /Q /S .\__pycache__
rm .\main.spec