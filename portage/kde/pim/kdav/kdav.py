import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.versionInfo.setDefaultValues( )

        self.shortDescription = "KDav library"
        self.patchToApply['17.04.0'] = [("001-fix_missing_include.diff", 1)]
        self.patchToApply['17.04.1'] = [("001-fix_missing_include.diff", 1)]
        
    def setDependencies( self ):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "master"
        self.buildDependencies["libs/qtbase"] = "default"
        self.dependencies["frameworks/kcoreaddons"] = "default"
        self.dependencies["frameworks/kio"] = "default"

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        CMakePackageBase.__init__( self )
