import info


class subinfo(info.infoclass):
    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['libs/qtbase'] = 'default'
        # qtquick1 is optional
        #self.dependencies['libs/qtquick1'] = 'default'

    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:phonon'        
        for ver in ['4.9.0']:
            self.targets[ver] = 'http://download.kde.org/stable/phonon/%s/phonon-%s.tar.xz' % (ver ,ver)
            self.targetInstSrc[ver] = 'phonon-%s' % ver
        self.targetDigests['4.9.0'] = (['bb74b40f18ade1d9ab89ffcd7aeb7555be797ca395f1224c488b394da6deb0e0'], CraftHash.HashAlgorithm.SHA256)

        self.shortDescription = "a Qt based multimedia framework"
        self.defaultTarget = '4.9.0'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = " -DPHONON_BUILD_EXAMPLES=OFF -DPHONON_BUILD_TESTS=OFF -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON -DPHONON_BUILD_PHONON4QT5=ON"
        if not self.subinfo.options.isActive("win32libs/dbus"):
            self.subinfo.options.configure.defines += " -DPHONON_NO_DBUS=ON "
            

        
