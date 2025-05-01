# Built in Module
import os
import click


# display ***** in top
def header():
    os.system("clear")
    for _ in range(2):
        click.echo("*" * 12)
        if _ == 0:
            click.echo("Arch Script")
    click.echo("\n")


def menu():
    click.echo("1. Bashrc")
    click.echo("2. Sudoers")
    click.echo("3. Pacman Conf")
    click.echo("4. Package Manager")
    click.echo("5. Aur Arch Linux")
    click.echo("6. Black Arch Installer")
    click.echo("7. ufw Firewall")
    click.echo("8. Uninstall Gnome Apps")
    click.echo("9. Bluetooth")
    click.echo("10. Compressed ( Xampp )")
    click.echo("11. Next Dns Setup")
    click.echo("12. Flathub Manager")
    click.echo("0. exit\n")


def main():
    header()
    menu()

    user_input = click.prompt("Enter Input", type=click.IntRange(0, 12))
    match user_input:
        case 0:
            exit()

        case 1:
            import Bashrc
            bashrc = Bashrc.Bashrc()
            bashrc.add_aliases()

        case 2:
            import Sudoers
            Sudoers.Sudoers()

        case 3:
            import PacmanConf
            PacmanConf.PacmanConf()

        case 4:
            import PackageManager
            package_manager = PackageManager.PackageManager()
            package_manager.install_packages()
            package_manager.enable_service()

        case 5:
            import AurArchLinux
            aur = AurArchLinux.AurArchLinux()
            aur.gpg_key()
            aur.install_aur_packages()

        case 6:
            import BlackArchInstaller
            black_arch_installer = BlackArchInstaller.BlackArchInstaller()
            black_arch_installer.install_black_arch()

        case 7:
            import Ufw
            Ufw.Ufw()

        case 8:     # Uninstall Gnome Apps
            import Uninstall
            package_manager = Uninstall.Uninstall()
            package_manager.remove_packages()

        case 9:
            import Bluetooth
            Bluetooth.Bluetooth()

        case 10:
            import Compressed
            compressed = Compressed.Compressed()
            compressed.file()

        case 11:
            import NextDns
            nextdns = NextDns.NextDns()
            nextdns.next_dns()

        case 12:
            import FlathubManager
            flathub_manager = FlathubManager.FlathubManager()
            flathub_manager.install_flathub_packages()


if __name__ == "__main__":
    main()
