#!/usr/bin/env python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
sys.path.append('/usr/lib/lucidsystems-greeter')
sys.path.append('/usr/share/lucidsystems-greeter')
import os
import string

from greeter import GreeterEngine

from PyQt4 import QtGui, QtCore, uic
import qt_resources_rc

class GreeterWindow(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        self.ui = uic.loadUi('/usr/share/lucidsystems-greeter/qt_interface.ui')

        # Set window title
        self.ui.setWindowTitle("Welcome to LucidSystems")
        self.ui.setWindowIcon(QtGui.QIcon('/usr/share/lucidsystems/icons/lucidsystems_icon_blue_32x32.png'))

        # Show the window
        self.ui.show()
        
        # Move main window to center
        qr = self.ui.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.ui.move(qr.topLeft())
        
        # Connect the buttons
        self.connect(self.ui.button_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
