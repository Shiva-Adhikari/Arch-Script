import os
import time

def print_header():
# clear
    os.system("clear")
# print *****
    for _ in range(2):
        print("*" * 12 ,end="")
        if _ == 0:
            print("Arch Script", end="")
    print("\n")

def print_menu():
    # print("\n")
    print("1. Bashrc")
    print("2. Sudoers")
    print("3. Pacman Conf")
    print("4. Package Manager")
    print("5. Aur Arch Linux")
    print("6. Black Arch Installer")
    print("7. ufw Firewall")
    print("8. Uninstall Gnome Apps")
    print("9. Bluetooth")
    print("10. Compressed ( Xampp )")
    print("11. Next Dns Setup")
    print("12. Flathub Manager")
    print("0. exit\n")

def main():
# pause
    i = 0
    while True:
        if i == 1:
            input("Press Any Key...")

# call function
        print_header()
        print_menu()
# user input
        user_input = input("Enter Input... ")
        if user_input.isdecimal():
# convert to decimal
            user_input = int(user_input)
# 0 = exit
            if user_input == 0:
                exit()
# greater than 12
            if user_input > 12:
                print("Input Between 1 to 12")
                time.sleep(2)
# skip
                continue
        else:
            print("\nPlease Enter a Number")
# time sleep
        time.sleep(2)

        match user_input:
            case 1:     # Bashrc
                import Bashrc
                bashrc = Bashrc.Bashrc()
                bashrc.add_aliases()
                i = 1
                continue

            case 2:     # Sudoers
                import Sudoers
                sudoers = Sudoers.Sudoers()
                i = 1
                continue

            case 3:     # Pacman Conf
                import PacmanConf
                pacmanconf = PacmanConf.PacmanConf()
                i = 1
                continue

            case 4:     # Package Manager
                import PackageManager
                package_manager = PackageManager.PackageManager()
                package_manager.install_packages()
                package_manager.enable_service()
                i = 1
                continue

            case 5:     # Aur Arch Linux
                import AurArchLinux
                aur = AurArchLinux.AurArchLinux()
                aur.gpg_key()
                aur.install_aur_packages()
                i = 1
                continue

            case 6:     # Black Arch Installer
                import BlackArchInstaller
                black_arch_installer = BlackArchInstaller.BlackArchInstaller()
                black_arch_installer.install_black_arch()
                i = 1
                continue

            case 7:     # ufw Firewall
                import Ufw
                ufw = Ufw.Ufw()
                i = 1
                continue

            case 8:     # Uninstall Gnome Apps
                import Uninstall
                package_manager = Uninstall.Uninstall()
                package_manager.remove_packages()
                i = 1
                continue

            case 9:     # Bluetooth
                import Bluetooth
                bluetooth = Bluetooth.Bluetooth()
                i = 1
                continue

            case 10:    # Compressed
                import Compressed
                compressed = Compressed.Compressed()
                compressed.file()
                i = 1
                continue

            case 11:    # Next Dns Setup
                import NextDns
                nextdns = NextDns.NextDns()
                nextdns.next_dns()
                i = 1
                continue

            case 12:    # Flathub Manager
                import FlathubManager
                flathub_manager = FlathubManager.FlathubManager()
                flathub_manager.install_flathub_packages()
                i = 1


if __name__ == "__main__":
    main()













