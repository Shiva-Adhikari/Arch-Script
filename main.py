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
    print("5. Aur Install")
    print("6. Black Arch Installer")
    print("7. ufw Firewall")
    print("8. Uninstall Gnome Apps")
    print("9. Bluetooth")
    print("10. Compressed ( Xampp )")
    print("11. Next Dns Setup")
    print("0. exit\n")

def main():
    while True:
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
# skip
                continue
        else:
            print("\nPlease Enter a Number")
# time sleep
        time.sleep(2)

        match user_input:
            case 1:     # Bashrc
                import Bashrc
                # bashrc = Bashrc()
                # bashrc.add_aliases(aliases)
                continue

            case 2:     # Sudoers
                import Sudoers
                # sudoers = Sudoers()
                continue

            case 3:     # Pacman Conf
                import PacmanConf
                # pacmanconf = PacmanConf()
                continue

            case 4:     # Package Manager
                import PackageManager
                # package_manager = PackageManager()
                # package_manager.install_packages(pacman_packages)
                continue

            case 5:     # Aur Install
                pass
                continue

            case 6:     # Black Arch Installer
                pass
                continue

            case 7:     # ufw Firewall
                pass
                continue

            case 8:     # Uninstall Gnome Apps
                import PackageManager
                
                continue

            case 9:     # Bluetooth
                pass
                continue

            case 10:    # Compressed
                pass
                continue

            case 11:    # Next Dns Setup
                pass
                continue


if __name__ == "__main__":
    main()













