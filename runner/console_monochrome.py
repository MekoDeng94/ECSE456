""" Logger for console output """
class Console:
    """ Dummy logger when no gui is available """
    @classmethod
    def info(cls, message):
        """ log info messages """
        print("[INFO] " + str(message), flush=True)
    @classmethod
    def error(cls, message):
        """ log error messages """
        print("[ERR]  " + str(message), flush=True)
    @classmethod
    def warning(cls, message):
        """ log warning messages """
        print("[WARN] " + str(message), flush=True)