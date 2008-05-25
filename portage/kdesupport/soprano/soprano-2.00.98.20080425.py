import base
import os
import sys
import info

class subinfo(info.infoclass):
    def setDependencies( self ):
        self.hardDependencies['virtual/base'] = 'default'
        self.hardDependencies['libs/qt'] = 'default'
        self.hardDependencies['kdesupport/clucene-core'] = 'default'

    def setTargets( self ):
        self.svnTargets['svnHEAD'] = 'trunk/kdesupport/soprano'
        self.svnTargets['2.0.0'] = 'tags/soprano/2.0.0'
        self.svnTargets['2.0.1'] = 'tags/soprano/2.0.1'
        self.svnTargets['2.0.2'] = 'tags/soprano/2.0.2'
        self.svnTargets['2.0.3'] = 'tags/soprano/2.0.3'
        self.targets['2.0.98'] = 'http://downloads.sourceforge.net/sourceforge/soprano/soprano-2.0.98.tar.bz2'
        self.targetInstSrc['2.0.98'] = 'soprano-2.0.98'
        self.defaultTarget = 'svnHEAD'

class subclass(base.baseclass):
    def __init__( self, **args ):
        base.baseclass.__init__( self, args=args )
        self.instsrcdir = "soprano"
        self.subinfo = subinfo()

    def unpack( self ):
        return self.kdeSvnUnpack()

    def compile( self ):
        return self.kdeCompile()

    def install( self ):
        return self.kdeInstall()

    def make_package( self ):
        if not self.buildTarget == 'svnHEAD':
            return self.doPackaging( "soprano", self.buildTarget, True )
        else:
            return self.doPackaging( "soprano", os.path.basename(sys.argv[0]).replace("soprano-", "").replace(".py", ""), True )

if __name__ == '__main__':
    subclass().execute()
