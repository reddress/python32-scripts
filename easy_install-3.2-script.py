#!c:\Python32\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'distribute==0.6.49','console_scripts','easy_install-3.2'
__requires__ = 'distribute==0.6.49'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('distribute==0.6.49', 'console_scripts', 'easy_install-3.2')()
    )
