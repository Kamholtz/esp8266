# pipenv run ampy --port COM8 --baud 115200 get src/main.py downloads/main.py
pipenv run mpfshell -n -c "open com8; get src/main.py downloads/main.py"