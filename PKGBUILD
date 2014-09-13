# Maintainer: Kane Vanguard

pkgname=lucidsystems-livemedia
pkgver=1.0.0
pkgrel=1
pkgdesc="Tools for the LuicdSystems live media"
arch=('any')
url="https://github.com/KaneVanguard/luicdsystems-livemedia"
license=('GPL')
depends=('python2' 'qt4' 'python2-pyqt')

package() {
  cd "$pkgdir"

  install -Dm755 "$srcdir/usr/bin/luicdsystems-greeter" usr/bin/lucidsystems-greeter
  install -Dm755 "$srcdir/usr/bin/prepare_livesystem" usr/bin/prepare_livesystem
  
  cp -R "$srcdir/etc" etc
  cp -R "$srcdir/usr/lib" usr/lib
  cp -R "$srcdir/usr/share" usr/share
  
}
