# pipenv run ampy --port COM8 --baud 115200 get src/boot.py downloads/boot.py
# pipenv run mpfshell -n -c "open ws:192.168.1.36,iopjklnm,"
pipenv run mpfshell -n -c "open com8; get src/boot.py downloads/boot.py"