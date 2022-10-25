from genericpath import isfile
import os

#postgresql
#----------


#logging
#-------
def refresh_logger(filename):
    """Remove old logs and create new ones."""
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except Exception:
            pass

    open(filename, 'a').close()