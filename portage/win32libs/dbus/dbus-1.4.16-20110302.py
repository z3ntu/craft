# -*- coding: utf-8 -*-
import utils
import os
import info
import emergePlatform
import compiler

class subinfo(info.infoclass):
    def setTargets( self ):
        svnurl = "https://windbus.svn.sourceforge.net/svnroot/windbus/"
        self.svnTargets['1.2.4'] = svnurl + 'tags/1.2.4'
        self.targetInstSrc['1.2.4'] = 'tags/1.2.4'
        self.targetConfigurePath['1.2.4'] = 'cmake'

        self.svnTargets['svnHEAD'] = svnurl + 'trunk'
        self.targetConfigurePath['svnHEAD'] = 'cmake'

        self.targets['1.4.0'] = 'http://cgit.freedesktop.org/dbus/dbus/snapshot/dbus-1.4.0.tar.bz2'
        self.targetDigests['1.4.0'] = '3983d9a1456e5772fa4cb5e2818ed015b2f6131b'
        self.targetInstSrc['1.4.0'] = 'dbus-1.4.0'
        self.targetConfigurePath['1.4.0'] = 'cmake'

        for ver in ['1.4.1','1.4.16', '1.4.24']:
            self.targets[ver] = 'http://dbus.freedesktop.org/releases/dbus/dbus-%s.tar.gz' % ver
            self.targetInstSrc[ver] = 'dbus-%s' % ver
            self.targetConfigurePath[ver] = 'cmake'
        self.targetDigests['1.4.1'] = '112279ff58305027294fe0eb5bee600f68cf0b50'
        self.targetDigests['1.4.24'] = '02de59fe8a05a04b81e96acbac7d88c9513d1a0b'
       
        for ver in ['1.6.8']:
            self.targets[ver] = 'http://dbus.freedesktop.org/releases/dbus/dbus-%s.tar.gz' % ver
            self.targetInstSrc[ver] = 'dbus-%s' % ver
            self.targetConfigurePath[ver] = 'cmake'

        for ver in ['1.4.6', '1.4.8', '1.4.10', '1.4.12', '1.4.14']:
            self.svnTargets[ver] = 'git://anongit.freedesktop.org/git/dbus/dbus||dbus-' + ver
            self.targetSrcSuffix[ver] = 'git'
            self.targetConfigurePath[ver] = 'cmake'

        self.svnTargets['gitHEAD'] = 'git://anongit.freedesktop.org/git/dbus/dbus'
        self.targetSrcSuffix['gitHEAD'] = 'git'
        self.targetConfigurePath['gitHEAD'] = 'cmake'


        if emergePlatform.isCrossCompilingEnabled():
            self.patchToApply['1.4.0'] = [('dbus-1.4.0.diff', 1),
                                          ('0001-tentative-workaround-for-the-random-hangs-on-windows.patch', 1),
                                          ('no-auth.diff', 1),
                                          ('msvc2010-has-errnoh.diff', 1),
                                          ('live-lock-fix.diff', 1),
                                          ('wince-splashscreen.diff', 1)
                                          ]
            self.patchToApply['1.4.1'] = [('no-auth.diff', 1),
                                          ('msvc2010-has-errnoh.diff', 1),
                                          ]
        else:
            self.patchToApply['1.4.0'] = [('dbus-1.4.0.diff', 1),
                                          ('0001-tentative-workaround-for-the-random-hangs-on-windows.patch', 1),
                                          ('msvc2010-has-errnoh.diff', 1),
                                          ('live-lock-fix.diff', 1)
                                          ]
            self.patchToApply['1.4.1'] = [('msvc2010-has-errnoh.diff', 1),
                                          ('live-lock-fix.diff', 1),
                                          ('replace_path_with_current_installdir.diff', 1)
                                         ]
            self.patchToApply['1.4.6'] = [('live-lock-fix.diff', 1),
                                          ('0001-Do-not-use-ELEMENT_TYPE-which-is-reserved.patch', 1),
                                          ('16e6236b8310d41d0f21923bb87fa4cf148919d0.patch', 1)
                                         ]
            self.patchToApply['1.4.10'] = [('workaround-for-inline-keyword-in-msvc10.patch', 1),
                                           ('16e6236b8310d41d0f21923bb87fa4cf148919d0.patch', 1)
                                         ]

        self.shortDescription = "Freedesktop message bus system (daemon and clients)"
        if emergePlatform.isCrossCompilingEnabled():
            self.defaultTarget = '1.4.0'
        else:
            self.defaultTarget = '1.4.24'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['win32libs/expat'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.package.packageName = 'dbus'
        self.subinfo.options.make.slnBaseName = 'dbus'
        self.subinfo.options.configure.defines = (
                "-DDBUS_BUILD_TESTS=OFF "
                "-DDBUS_ENABLE_XML_DOCS=OFF "
                "-DDBUS_USE_EXPAT=ON "
                "-DDBUS_REPLACE_LOCAL_DIR=ON ")

        if (self.buildType == "Release"):
            self.subinfo.options.configure.defines += (
                    "-DDBUS_ENABLE_VERBOSE_MODE=OFF "
                    "-DDBUS_DISABLE_ASSERTS=ON ")

        if emergePlatform.isCrossCompilingEnabled():
            self.subinfo.options.configure.defines += (
                    "-DDBUS_SESSION_BUS_DEFAULT_ADDRESS:"
                    "STRING=tcp:host=localhost,port=12434 ")
        elif self.buildTarget == "gitHEAD":
            self.subinfo.options.configure.defines += (
                "-DDBUS_SESSION_BUS_LISTEN_ADDRESS:STRING=autolaunch:scope=*install-path "
                "-DDBUS_SESSION_BUS_CONNECT_ADDRESS:STRING=autolaunch:scope=*install-path ")
            # kde uses debugger output, so dbus should do too
            self.subinfo.options.configure.defines += (
                    "-DDBUS_USE_OUTPUT_DEBUG_STRING=ON ")
        else:
            # for 1.4.1 and greater switch to official
            # supported scopes -> autolaunch:scope=*install-path
            self.subinfo.options.configure.defines += (
                    "-DDBUS_SESSION_BUS_DEFAULT_ADDRESS:"
                    "STRING=autolaunch:scope=install-path ")
            # kde uses debugger output, so dbus should do too
            # not sure if this works for wince too, so limited to win32
            self.subinfo.options.configure.defines += (
                    "-DDBUS_USE_OUTPUT_DEBUG_STRING=ON ")

if __name__ == '__main__':
    Package().execute()
