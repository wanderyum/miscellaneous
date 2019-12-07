import os
import sys
import shutil

class manager():
    def __init__(self):
        pass

    def install(self, silenced=False):
        sp_path = self.find_sp()
        if os.path.exists(os.path.join(sp_path, 'pfplot')):
            if not silenced:
                import pfplot
                print('Does not install as pfplot version {} found! \nLocation:\n{}'.format(pfplot.ver(), os.path.join(sp_path, 'pfplot')))
        else:
            shutil.copytree('./pfplot', os.path.join(sp_path, 'pfplot'))
            if not silenced:
                print('Successfully installed! \nLocation:\n{}'.format(os.path.join(sp_path, 'pfplot')))

    def uninstall(self, silenced=False):
        sp_path = self.find_sp()
        if os.path.exists(os.path.join(sp_path, 'pfplot')):
            shutil.rmtree(os.path.join(sp_path, 'pfplot'))
            if not silenced:
                print('Successfully uninstalled!')
        else:
            if not silenced:
                print('No pfplot installed!')

    def update(self, silenced=False):
        sp_path = self.find_sp()
        self.uninstall(silenced=True)
        self.install(silenced=True)
        if not silenced:
            import pfplot
            print('Successfully update pfplot to version {}\nLocation:\n{}'.format(pfplot.ver(), os.path.join(sp_path, 'pfplot')))

    def find_sp(self):
        if sys.platform == 'win32':
            for item in sys.path[::-1]:
                if item[-13:] == 'site-packages':
                    return item
        elif sys.platform == 'linux':
            for item in sys.path[::-1]:
                if '/home/' in item and 'site-packages' in item and item[-13:] == 'site-packages':
                    return item


if __name__ == '__main__':
    m = manager()
    #m.install()
    #m.uninstall()
    m.update()