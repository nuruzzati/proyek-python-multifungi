import random
import main

def start():
    while True:
        cuypay_position = random.randint(1,4)
                        
        bentuk_goa = '|_|'
        goa_kosong = [bentuk_goa] * 4

        goa = goa_kosong.copy()
        goa[cuypay_position - 1] = '[0_0]'

        print('\n' + ' '.join(goa_kosong))    
            
        pilihan_user = int(input(f'\nPerhatikan goa tersebut, ada di mana cuypay berada ? [1/2/3/4] : '))

        while pilihan_user not in [1, 2, 3, 4]:
            pilihan_user = int(input('\nPilihan tidak tersedia, pilih antara [1/2/3/4] : '))
    
        if pilihan_user == cuypay_position:
            print('\n' + ' '.join(goa))
            print(f'\nSelamat kamu menang 🏆')
        else:
            print('\n' +' '.join(goa))
            print(f'\nNice try, Kamu kalah ❎')
    

        play_again = input("\nApakah ingin melanjutkan game nya? [y/n] : ")
        if play_again == 'n':
            main.menu()
            
if __name__ == '__name__' :
    start()

