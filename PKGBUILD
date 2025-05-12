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
source=("git+https://github.com/TiagoRibeiro25/systemd-services-manager.git")
sha256sums=('SKIP')

package() {
    cd "$srcdir/$pkgname"

    # Install the app files from the src directory
    mkdir -p "$pkgdir/usr/local/bin"
    cp -r src/* "$pkgdir/usr/local/bin/$pkgname/"

    mkdir -p "$pkgdir/usr/share/applications"
    cat > "$pkgdir/usr/share/applications/systemd-services-manager.desktop" <<EOF
[Desktop Entry]
Name=Systemd Services Manager
Exec=python3 /usr/local/bin/systemd-services-manager/app.py
Type=Application
Categories=Utility;
EOF
}
