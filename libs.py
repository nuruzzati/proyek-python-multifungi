import socket
from time import sleep
PC_NAME = socket.gethostname()


def welcome_message() :
    style = '•' * (len(PC_NAME) + 6)
    print(style)
    print(f'•• {PC_NAME} ••')
    print(style)

def exit_program():
    print('program akan dihentikan\n', end='')
    sleep(1)
    print('\b\b\b3', end='', flush=True)
    sleep(1)
    print('\b\b2', end='', flush=True)
    sleep(1)
    print('\b1', end='', flush=True)
    print('\nprogram berhasil dihentikan')
    exit()

if __name__ == '__main__' :    
    welcome_message()
    exit_program()
