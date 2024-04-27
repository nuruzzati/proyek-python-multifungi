from libs import welcome_message, exit_program
from games import cuypy
from tools import warung, ytdownloader

def menu():
    try:
        user_option = int(input(f'\nMenu program NuzaPy : \n1. Games Cuypy\n2. Warung mini\n3. Youtube Downloader\n4. Exit program\n\nSilahkan pilih : '))
        
        if user_option == 1:
             cuypy.start()
        elif user_option == 2:
            warung.start()
        elif user_option == 3:
            ytdownloader.main_loop()
        elif user_option == 4:
            exit_program()
        else:
            print(f'{user_option} Tidak ada dalam pilihan, Silakan pilih nomor 1, 2, atau 3.')
    except ValueError:
        print('Input tidak valid. Silakan pilih nomor 1, 2, atau 3.')


     


def main():
    welcome_message()
    menu()

if __name__ == '__main__' :
    main()
