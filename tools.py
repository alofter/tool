import os
import time

def show_banner():
    os.system('clear')
    print("\033[92m")
    print("""
    ██████╗ ██╗███████╗ █████╗ 
    ██╔══██╗██║╚══███╔╝██╔══██╗
    ██████╔╝██║  ███╔╝ ███████║
    ██╔══██╗██║ ███╔╝  ██╔══██║
    ██║  ██║██║███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print("     yakında.")
    print("\033[0m")

def main_menu():
    print("\n1. Port Tara")
    print("2. Sistem Bilgisi")
    print("3. Çıkış")
    
    secim = input("\nSeçim: ")
    return secim
