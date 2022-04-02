class FileExtension:
    def __init__(self,file_name):
        self.__file_name = file_name
        self.__allowed_file_extensions = ['.pdf','.jpeg',
                              '.png','.txt',
                              '.docx']

    def __repr__(self):
        return 'FileExtension(%s)'%self.__file_name

    def __check_extension(self):
        ext = '.'+self.__file_name.split('.')[-1]
        if ext in self.__allowed_file_extensions:
            return True
        else: 
            return False
        
    def checkExtension(self):
        return self.__check_extension()