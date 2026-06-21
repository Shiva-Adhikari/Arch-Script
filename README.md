# Arch Script

A post-install automation tool for Arch Linux. Run it after a fresh install to set up your system quickly.

---

## Requirements

- Arch Linux
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (package manager)

---

## Installation

```bash
git clone https://github.com/Shiva-Adhikari/Arch-Script.git
cd Arch-Script
uv run src/main.py
```

---

## Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Bashrc | Manage aliases, backup and restore `.bashrc` |
| 2 | Sudoers | Add current user to sudoers (no password prompt) |
| 3 | Pacman Conf | Enable parallel downloads, color, and candy |
| 4 | Package Manager | Install all pacman packages |
| 5 | AUR Packages | Install paru, then all AUR packages |
| 6 | BlackArch | Install BlackArch repo |
| 7 | UFW Firewall | Install and enable UFW |
| 8 | Uninstall | Remove default GNOME bloat |
| 9 | Bluetooth | Install and enable bluetooth |
| 10 | Flathub | Install flatpak apps |
| 0 | Exit | Exit the script |

---

## Configuration

All packages and settings live in `config/packages.json`. Edit this file to add or remove packages without touching any Python code.

```json
{
    "pacman": ["git", "curl", "htop"],
    "aur": ["vscodium-bin", "librewolf-bin"],
    "flathub": {
        "Telegram": "org.telegram.desktop"
    },
    "aliases": {
        "update": "sudo pacman -Sy"
    }
}
```

### Sections

| Key | Type | Description |
|-----|------|-------------|
| `pacman` | list | Packages to install via pacman |
| `pacman_services` | list | Services to enable after pacman install |
| `aur` | list | Packages to install via paru |
| `aur_dependencies` | list | Dependencies needed before AUR install |
| `aur_services` | list | Services to enable after AUR install |
| `flathub` | dict | Flatpak apps `{ "Name": "app.id" }` |
| `uninstall` | list | GNOME packages to remove |
| `bluetooth` | list | Bluetooth packages |
| `bluetooth_services` | list | Bluetooth services to enable |
| `ufw` | list | UFW packages |
| `ufw_services` | list | UFW services to enable |
| `aliases` | dict | Shell aliases `{ "alias": "command" }` |

---

## Project Structure

```
Arch-Script/
├── config/
│   └── packages.json   # all packages and settings
├── src/
│   ├── main.py         # entry point and menu
│   ├── base.py         # shared base class
│   ├── bashrc.py       # alias and bashrc management
│   ├── sudoers.py      # sudoers configuration
│   ├── pacman_conf.py  # pacman configuration
│   ├── package_manager.py  # pacman package installer
│   ├── aur_package.py  # paru and AUR package installer
│   ├── blackarch.py    # BlackArch repo installer
│   ├── ufw.py          # firewall setup
│   ├── uninstall.py    # remove GNOME bloat
│   ├── bluetooth.py    # bluetooth setup
│   └── flathub.py      # flatpak app installer
└── pyproject.toml
```

---

## License

MIT
