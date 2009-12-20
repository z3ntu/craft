# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets( self ):
        self.targets['1.6.3'] = "http://winkde.org/pub/kde/ports/win32/repository/other/Git-1.6.3-preview20090507-2.tar.bz2"
        self.targets['1.6.4'] = "http://msysgit.googlecode.com/files/PortableGit-1.6.4-preview20090729.7z"
        self.targetInstSrc['1.6.3'] = ""
        self.defaultTarget = '1.6.4'

    def setDependencies(self):
        self.hardDependencies['dev-util/7zip']   = 'default'

        
from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__( self):
        self.subinfo = subinfo()
        self.subinfo.options.merge.ignoreBuildType = True
        self.subinfo.options.merge.destinationPath = "dev-utils/git";
        BinaryPackageBase.__init__(self)
        
    def unpack(self):
        if not BinaryPackageBase.unpack(self):
            return False
        utils.copyFile(os.path.join(self.packageDir(),"git.bat"),os.path.join(self.rootdir,"dev-utils","bin","git.bat"))
        return True

if __name__ == '__main__':
    Package().execute()
