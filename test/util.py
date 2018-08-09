import os
import stat


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def on_rmtree_error(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)