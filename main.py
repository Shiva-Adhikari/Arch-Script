# Built in Module
import os
import click

# Local Module
from src.bashrc import Bashrc
from src.sudoers import Sudoers
from src.pacman_conf import PacmanConf
from src.package_manager import PackageManager
from src.aur_package import AurPackage
from src.blackarch import BlackArch
from src.ufw import Ufw
from src.uninstall import Uninstall
from src.bluetooth import Bluetooth
from src.flathub import Flathub


def header():
    os.system("clear")
    for _ in range(2):
        click.echo("*" * 12)
        if _ == 0:
            click.echo("Arch Script")
    click.echo("\n")


def menu():
    click.echo("1.  Bashrc          → manage aliases, backup and restore .bashrc")
    click.echo("2.  Sudoers         → add current user to sudoers (no password)")
    click.echo("3.  Pacman Conf     → enable parallel downloads, color, candy")
    click.echo("4.  Package Manager → install all pacman packages")
    click.echo("5.  AUR Packages    → install paru and all AUR packages")
    click.echo("6.  BlackArch       → install BlackArch repo")
    click.echo("7.  UFW Firewall    → install and enable ufw")
    click.echo("8.  Uninstall       → remove default GNOME bloat")
    click.echo("9.  Bluetooth       → install and enable bluetooth")
    click.echo("10. Flathub         → install flatpak apps")
    click.echo("0.  Exit\n")


def main():
    header()
    menu()

    user_input = click.prompt("Enter Input", type=click.IntRange(0, 10))
    match user_input:
        case 0:
            exit()
        case 1:
            Bashrc().run()
        case 2:
            Sudoers().run()
        case 3:
            PacmanConf().run()
        case 4:
            PackageManager().run()
        case 5:
            AurPackage().run()
        case 6:
            BlackArch().run()
        case 7:
            Ufw().run()
        case 8:
            Uninstall().run()
        case 9:
            Bluetooth().run()
        case 10:
            Flathub().run()


if __name__ == "__main__":
    main()
