import os

home = os.curdir

if 'HOME' in os.environ:
    home = os.environ['HOME']
elif os.name == 'posix':
    home = os.path.expanduser('~/')
elif os.name == 'nt':
    if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
elif 'HOMEPATH' in os.environ:
    home = os.environ['HOMEPATH']

CRAWLABUNIT_ROOT = os.path.join(home, '.crawUnit')
CRAWLABUNIT_TMP = os.path.join(CRAWLABUNIT_ROOT, 'tmp')

if not os.path.exists(CRAWLABUNIT_ROOT):
    os.mkdir(CRAWLABUNIT_ROOT)

if not os.path.exists(CRAWLABUNIT_TMP):
    os.mkdir(CRAWLABUNIT_TMP)
