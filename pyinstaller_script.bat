pyinstaller main.py --clean --noconsole -y
rmdir /Q /S .\SIdM\main
mkdir .\dist\main\gui
xcopy .\gui .\dist\main\gui /E
move .\dist\main .\SIdM
rmdir /Q /S .\build
rmdir /Q /S .\dist
rmdir /Q /S .\__pycache__
rm .\main.spec