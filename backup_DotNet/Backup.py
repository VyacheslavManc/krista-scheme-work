import datetime
import os
import xlrd
import zipfile

constPath = {
    'DotNet': '\\DotNet\\',
    'DBPath': '\\Database\\'
}

# То что удалять нельзя
constSrvConf = [
    'Krista.FM.Server.AppServer.exe.config',
    'Krista.FM.Server.DataPumpApp.dll.config',
    'Krista.FM.Server.DataPumpConsole.exe.config',
    'Krista.FM.Server.DataPumpHost.exe.config',
    'Krista.FM.Server.FMService.exe.config',
    'ServiceInstallerParameters.txt',
    'Configuration',
    'Packages'
]
# удаляется при замене компонентов
constSrvLogs = [
    'FMServer.log',
    'FMServer1.log',
    'PlaningProvider.log'
]
# То что удалять нельзя
constRep = [
    'Configuration',
    'Packages'
]


class ReadXls(object):
    def __init__(self, srv, port):
        self.srv = srv
        self.port = port

    @property
    def read_srv_and_port(self):
        rb = xlrd.open_workbook(r"D:\VSS\Документация\Правила\ПРАВИЛА_Расположение схем.xls", formatting_info=True)
        sheet = rb.sheet_by_index(0)
        f = float(self.port)
        # print(type(f))
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            if row[1] == self.srv and row[3] == f:
                schema = row[0]
                srv_services = row[1]
                services = row[2]
                alias = row[4]
                RDS_srv = row[5]
                OLAP_srv = row[6]
            else:
                continue
        return schema, srv_services, services, alias, RDS_srv, OLAP_srv


class DotNet(object):
    def __init__(self, name):
        self.name = name
        self.bin = 'Bin' + self.name
        self.rep = 'Repository' + self.name

    def arch(self, bin_path, rep_path, temp_path):
        dt = datetime.datetime.now()  # Сегодняшняя дата
        date = dt.strftime('_%Y%m%d')
        print(bin_path)
        os.chdir(bin_path)
        with zipfile.ZipFile(os.path.join(temp_path, self.bin + date + '.zip'), 'w') as archive_bin:
            for root, dirs, files in os.walk(bin_path):
                for file in files:
                    if file in constSrvLogs:
                        continue
                    else:
                        archive_bin.write(os.path.join(root, file))
                        print(file)
        print(rep_path)
        os.chdir(rep_path)
        with zipfile.ZipFile(os.path.join(temp_path, self.rep + date + '.zip'), 'w') as archive_rep:
            for fil in constRep:
                for root, dirs, files in os.walk(fil):
                    for file in files:
                        archive_rep.write(os.path.join(root, file))
                        print(file)
        return print("Архивация завершена", archive_bin, archive_rep)