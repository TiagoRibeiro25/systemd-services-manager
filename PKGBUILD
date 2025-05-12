# Maintainer: Tiago Ribeiro <tiago.d.ribeiro@hotmail.com>
pkgname=systemd-services-manager
pkgver=1.0.0
pkgrel=1
pkgdesc="A GUI application to manage systemd services"
arch=('x86_64')
url="https://github.com/TiagoRibeiro25/systemd-services-manager"
license=('GPL3')
depends=('python-gobject' 'gtk3' 'python')
makedepends=('git')
source=()
sha256sums=()

package() {
    # Ensure we are in the right directory
    cd "$srcdir/$pkgname/src"  # Go to the src directory of your local repository

    # Create the directory where the app will be installed
    mkdir -p "$pkgdir/usr/local/bin/systemd-services-manager"

    # Install the Python files from the src directory into the package
    cp -r * "$pkgdir/usr/local/bin/systemd-services-manager/"

    # Create a desktop entry for the application
    mkdir -p "$pkgdir/usr/share/applications"
    cat > "$pkgdir/usr/share/applications/systemd-services-manager.desktop" <<EOF
[Desktop Entry]
Name=Systemd Services Manager
Exec=python3 /usr/local/bin/systemd-services-manager/app.py
Icon=systemd-services-manager
Type=Application
Categories=Utility;
EOF
}
