from backup_DotNet import removing, Search_scheme, Backup

constPath = {
    'DotNet': '\\DotNet\\',
    'DBPath': '\\Database\\'
}

constSrvConf = [
    'Krista.FM.Server.AppServer.exe.config',
    'Krista.FM.Server.DataPumpApp.dll.config',
    'Krista.FM.Server.DataPumpConsole.exe.config',
    'Krista.FM.Server.DataPumpHost.exe.config',
    'Krista.FM.Server.FMService.exe.config',
    'ServiceInstallerParameters.txt',
]

constRep = [
    'Configuration',
    'Packages'
]

srv = input("введите имя сервера: ")
port = input("введите имя порта: ")

cell_1 = Backup.ReadXls(srv, port)
srv_services = cell_1.read_srv_and_port[1]
services = cell_1.read_srv_and_port[2]
ar_name = cell_1.read_srv_and_port[3]
RDS_server = cell_1.read_srv_and_port[4]
OLAP_server = cell_1.read_srv_and_port[5]

search_scheme = Search_scheme.Search_scheme(ar_name, services, srv_services)
bin_path = search_scheme.search_bin_path()
rep_path = search_scheme.search_rep_path()
temp_path = search_scheme.search_temp_path()

cell_2 = Backup.DotNet(ar_name)
cell_2.arch(bin_path, rep_path, temp_path)

answer = input(print("Delete? y/n"))
answer = answer.lower
if answer == "y":
    try:
        removing.delete_files_from_server(bin_path, constSrvConf)  # Удаление
        removing.delete_files_from_repository(rep_path, constRep)
    except:
        print("Не верный символ")
else:
    print("Резервная копия Сервеной и репозиторной части создана")