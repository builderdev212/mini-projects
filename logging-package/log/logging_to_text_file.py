import os

class log_to_file:
    def __init__():
        pass
    @classmethod
    def log(cls, file_name, string_to_write):
        """
        Make sure your file name ends with .txt. The point of this method is to make logging to a file simple
        """
        file_name = str(file_name)
        string_to_write = str(string_to_write)

        if '.txt' not in file_name: #make sure file has .txt suffix
            raise InvalidFileName
        else:
            if os.path.isfile(file_name) == False: #if file is being made
                try:
                    log = open(file_name, "w")
                    log.write(string_to_write)
                    log.close()
                except:
                    raise FileMakeFail
            elif os.path.isfile(file_name) == True: #if file already exists
                try:
                    log = open(file_name, "a")
                    log.write(string_to_write)
                    log.close()
                except:
                    raise FileAppendFail
            else: #if there is another error.
                raise InvalidFileName
