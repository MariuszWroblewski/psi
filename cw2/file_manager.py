class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        uchwyt = open(self.file_name)
        dane = uchwyt.read()
        print(dane)
        uchwyt.close()

    def update_file(self, text):
        uchwyt = open(self.file_name, 'a+')
        uchwyt.write(text)
