import info
from Package import VirtualPackageBase


class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets[ "master" ] = "[git]kde:craft"
        self.defaultTarget = "master"


    def setDependencies( self ):
        self.buildDependencies['dev-util/git'] = 'default'
        self.buildDependencies['dev-util/7zip'] = 'default'


from Package.SourceOnlyPackageBase import *

class Package(SourceOnlyPackageBase, GitSource):
    def __init__( self):
        SourceOnlyPackageBase.__init__(self)
        GitSource.__init__(self,subinfo=self.subinfo)

    def checkoutDir(self):
        return os.path.join(CraftStandardDirs.craftBin(), "..")

    def fetch(self):
        return GitSource.fetch(self)

    def install( self ):
        utils.utilsCache.clear()
        return SourceOnlyPackageBase.install(self)