# simulasi ATM
print(14*"_" + 'Welcome To ATM SAYA' + 14*"_")

class Atm:
    def __init__(self):
        self.pin = 112233
        self.no_Rekening = 987654321

    def __init__(self):
        input_pin = int(input("masukkan pin anda = "))
        input_no_Rekening = int(input("masukkan no rekening anda = "))
        self.saldo = 500000
        self.menu()      

    def menu(self):
        print("""
            pilih option yang di inginkan
                1. cek saldo
                2. tarik tunai
                3. setor tunai
                4. keluar
                    """)

        Option = int(input('silahkan pilih option : '))
        if Option == 1:
            self.cek_saldo()
        elif Option == 2:
            self.tarik_tunai()
        elif Option == 3:
            self.setor_tunai()
        elif Option == 4:
            self.keluar()

    def cek_saldo(self):
            print("*" * 40)
            print(f"uang anda berjumlah {self.saldo}")
            print("*" * 40)
            self.menu()

    def tarik_tunai(self):
            print("*" * 40)
            print(f"uang anda sekarang berjumlah {self.saldo} , mau ngambil berapa? ")
            print("*" * 40)
            print ("""
                    1. Rp. 100.000
                    2. Rp. 200.000
                        """)
            tarik_tunai = int(input("Option: "))
            if tarik_tunai == 1:
                hasil1 = self.saldo - 100000
                print(f"uang anda sekarang berjumlah", hasil1)
            elif tarik_tunai == 2:
                hasil2 = self.saldo -200000
                print(f"uang anda sekarang berjumlah", hasil2)
            self.menu()

    def setor_tunai(self):
            input_saldo = int(input('masukkan jumlah yang ingin di setor : '))
            self.saldo = self.saldo + input_saldo
            print("*" * 40)
            print(f"uang anda sekarang berjumlah {self.saldo}")
            print("*" * 40)
            self.menu()

    def keluar(self):
        SystemExit

bank = Atm()
        
