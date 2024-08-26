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
            case 1:
                import Bashrc
                # bashrc = Bashrc()
                # bashrc.add_aliases(aliases)
                continue

            case 2:
                import Sudoers
                # sudoers = Sudoers()
                continue

            case 3:
                import PacmanConf
                # pacmanconf = PacmanConf()
                continue

            case 4:
                import PackageManager
                # package_manager = PackageManager()
                # package_manager.install_packages(pacman_packages)
                continue

            case 5:
                pass
                continue

            case 6:
                pass
                continue

            case 7:
                pass
                continue

            case 8:
                import PackageManager
                # pacman_packages = ["gnome-maps", "gnome-music", "gnome-tour", "gnome-weather"]
                # package_manager = PackageManager.PackageManager()
                # package_manager.remove_packages(pacman_packages)
                continue

            case 9:
                pass
                continue

            case 10:
                pass
                continue

            case 11:
                pass
                continue


if __name__ == "__main__":
    main()













