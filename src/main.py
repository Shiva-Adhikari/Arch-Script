# Built in Module
import os
import click

# Local Module
from bashrc import Bashrc
from sudoers import Sudoers
from pacman_conf import PacmanConf
from package_manager import PackageManager
from aur_package import AurPackage
from blackarch import BlackArch
from ufw import Ufw
from uninstall import Uninstall
from bluetooth import Bluetooth
from flathub import Flathub


def header():
    os.system("clear")
    for _ in range(2):
        click.echo("*" * 12)
        if _ == 0:
            click.echo("Arch Script")
    click.echo("\n")


def menu():
    click.echo("1.  Bashrc")
    click.echo("2.  Sudoers")
    click.echo("3.  Pacman Conf")
    click.echo("4.  Package Manager")
    click.echo("5.  AUR Packages")
    click.echo("6.  BlackArch Installer")
    click.echo("7.  UFW Firewall")
    click.echo("8.  Uninstall Gnome Apps")
    click.echo("9.  Bluetooth")
    click.echo("10. Flathub Manager")
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
