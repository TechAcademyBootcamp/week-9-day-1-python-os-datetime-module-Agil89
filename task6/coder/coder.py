import os

class Coder():
    def __init__(self,project_name):
        self.project_name= project_name
        file_path = os.path.abspath(__file__)
        self.folder_path = os.path.dirname(file_path)
        mk_dir = os.path.join(self.folder_path, self.project_name)
        if not os.path.isdir(mk_dir):
            os.mkdir(mk_dir)

    def create_package(self,package_name):
        self.package_name = package_name
        files_dir = os.path.join(self.folder_path,self.project_name)
        os.chdir(files_dir)
        mkd_folder = os.path.join(files_dir,self.package_name)
        if not os.path.isdir(mkd_folder):
            os.mkdir(mkd_folder)


    def change_directory(self,package_name='project_dir'):
        self.package_name=package_name
        if self.package_name == 'project_dir':
            files_dir = os.path.join(self.folder_path,self.project_name)
            os.chdir(files_dir)
        else:
            os.chdir(self.package_name)
        return os.getcwd()

    def print_working_directory(self):
        return os.getcwd()

    def create_file(self,file_name):
        file_path = os.getcwd()
        mkd_file = os.path.join(file_path, file_name)
        open(mkd_file,'w').close()

    def write_code(self, file_name, code):
        with open(file_name,'w') as f:
            f.write(code)
    def run_code(self, file_name):
        os.system(f'python {file_name}')



codder = Coder('code2')
codder.create_package('package')
print(codder.change_directory('package'))
codder.create_file('main.py')
codder.write_code('main.py','print("hello world")')