import os
import winreg
import xml.etree.ElementTree as ET


class Search_scheme(object):
    def __init__(self, ar_name, services, srv_services):
        self.ar_name = ar_name
        self.services = services
        self.srv_services = srv_services

    def search_bin_path(self):
        key = winreg.ConnectRegistry(r'\\' + self.srv_services, winreg.HKEY_LOCAL_MACHINE)
        hkey = winreg.OpenKey(key, r"SYSTEM\CurrentControlSet\Services\%s" % self.services)
        bin_path = winreg.QueryValueEx(hkey, r"ImagePath")[0].replace('Krista.FM.Server.FMService.exe', '')
        winreg.CloseKey(hkey)
        winreg.CloseKey(key)

        bin_path = bin_path.replace('"', '')
        bin_path = bin_path.replace(bin_path[:2], '')
        bin_path = r'\\' + self.srv_services + bin_path
        return bin_path

    def search_rep_path(self):
        XML_FILE = os.path.join(self.search_bin_path(), 'Krista.FM.Server.FMService.exe.config')
        tree = ET.parse(XML_FILE)
        root = tree.getroot()
        rep_path = None
        for elem in root.iter():
            if elem.attrib.get('key') == 'RepositoryPath':
                path = elem.attrib.get('value')
                print(path)
                rep_path = path.replace(path[:2], '')
                rep_path = r'\\' + self.srv_services + rep_path
                break
        print(rep_path)
        return rep_path

    def search_temp_path(self):
        temp_path = self.search_bin_path().replace('Bin' + self.ar_name, 'temp')
        print(self.search_bin_path(), self.search_rep_path, temp_path)
        return temp_path
