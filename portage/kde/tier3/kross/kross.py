import info


class subinfo(info.infoclass):
    def setTargets( self ):
        self.versionInfo.setDefaultValues( )

        self.shortDescription = "Multi-language application scripting"

    def setDependencies( self ):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/extra-cmake-modules"] = "default"
        self.dependencies['libs/qttools'] = "default"
        self.dependencies['frameworks/kcompletion'] = "default"
        self.dependencies['frameworks/kcoreaddons'] = "default"
        self.dependencies['frameworks/kdoctools'] = "default"
        self.dependencies['frameworks/ki18n'] = "default"
        self.dependencies['kde/kiconthemes'] = "default"
        self.dependencies['kde/kio'] = "default"
        self.dependencies['kde/kparts'] = "default"
        self.dependencies['kde/kservice'] = "default"
        self.dependencies['frameworks/kwidgetsaddons'] = "default"
        self.dependencies['kde/kxmlgui'] = "default"

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        CMakePackageBase.__init__( self )


    

