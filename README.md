# Systemd Services Manager

**Systemd Services Manager** is a simple yet powerful graphical user interface (GUI) application to manage and control systemd services on Linux systems. It allows users to view, start, stop, enable, and disable systemd services easily through an intuitive interface.

This project is designed to make managing systemd services more accessible, especially for users who prefer not to interact with the terminal directly.

---

## Features

- **List All Services**: View all systemd services, whether they are running or not.
- **List Running Services**: See only the active services.
- **List Enabled Services**: View services that are enabled to start on boot.
- **Start/Stop Services**: Start or stop any service directly from the interface.
- **Enable/Disable Services**: Enable or disable services from starting on boot.
- **Modern GUI**: Simple and clean interface built with **GTK3** and **Python**.
- **Cross-Platform**: Works on any system with Python 3 and GTK3.

---

## Requirements

### Runtime Requirements:

- **Python 3**: Version 3.x of Python should be installed.
- **GTK3**: A graphical user interface toolkit for Python. It provides a modern and responsive GUI.
- **Python GObject**: Python bindings for GObject and GTK3.
- **systemd**: The system manager for Linux that controls system services.

### Package Dependencies:

- `python-gobject`
- `gtk3`
- `python`

### Build-time Dependencies:

- `git` (used to fetch the repository)

---

## Installation

### Arch Linux (or Arch-based distributions)

You can install the Systemd Services Manager using the AUR (Arch User Repository).

1. **Using an AUR Helper**:
   If you have an AUR helper like `yay`, you can install it with:

   ```bash
   yay -S systemd-services-manager
   ```

### From Source

1. **Clone the Repository**:
   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/TiagoRibeiro25/systemd-services-manager.git
   cd systemd-services-manager
   ```

2. **Build and Install Using `makepkg`**:
   If you're on an Arch-based distribution (like Arch Linux, Manjaro, etc.), you can create and install the package directly using the `PKGBUILD` script.

   ```bash
   makepkg -si
   ```

This command will:

- Fetch the necessary dependencies.
- Compile the Python code.
- Install the app to the correct locations on your system.

3. **Run the Application**:
   After installation, you can run the application using the command:

   ```bash
   systemd-services-manager
   ```

## Usage

Once the application is installed, you can run it either from your desktop environment's application launcher or by typing `systemd-services-manager` in the terminal.

### Interface Overview:

The main interface consists of:

1. **Tabs**:

   - **All Services**: Shows all available systemd services.
   - **Running Services**: Shows only the services that are currently running.
   - **Enabled Services**: Shows the services that are enabled to start on boot.

2. **Actions**:
   - **Start**: Starts a selected service.
   - **Stop**: Stops a selected service.
   - **Enable**: Enables a selected service to start on boot.
   - **Disable**: Disables a selected service from starting on boot.

You can perform actions on each service by selecting it and clicking the corresponding button.

## Troubleshooting

### Common Issues

1. **Missing GTK3 or GObject dependencies**:

   - Make sure you have installed `python3-gtk` and `python-gobject`. You can install these on Arch-based systems via:

      ```bash
      sudo pacman -S python-gobject gtk3
      ```

2. **Permissions**:

   - Some actions, such as starting, stopping, enabling, or disabling services, may require administrative (root) permissions. The application will prompt you for your password if necessary.

3. **Error with `systemctl`**:
   - Ensure that `systemd` is properly configured on your system and that the `systemctl` command is available.

---

## Development

If you want to contribute to this project, you can fork the repository, make changes, and then submit a pull request. Here's how you can set up the development environment:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TiagoRibeiro25/systemd-services-manager.git
   cd systemd-services-manager
   ```

2. **Install dependencies**:
   You'll need Python and GTK3 to work on this project. You can install the dependencies with:
   ```bash
   sudo pacman -S python-gobject gtk3
   ```
3. **Run the application**:
   After making changes, you can run the application from the src directory by using:
   `bash
	python3 app.py
	`
4. **Submit a Pull Request**:
   Once you've made your changes, create a pull request to contribute your code back to the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
