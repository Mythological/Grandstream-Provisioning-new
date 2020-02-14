import pymysql
from credentials import *

Template_2160 = "Create_CFG_Grandstream/Configs/Config_Example_GXP21XX_Gakk.txt"
Template_1610 = "Create_CFG_Grandstream/Configs/Config_Example_GXP1610_Gakk.txt"
Template_1611 = "Create_CFG_Grandstream/Configs/Config_Example_GXP1610_Remote_220.txt"

conn = pymysql.connect(host,user,password, db)
x = conn.cursor()

def OpenTemplate(a):
    with open(a, 'r') as file_object:
        lines = []
        for line in file_object:
            if line.lstrip().startswith('#'):
                continue
            lines.append(line)
    return lines

#Remove blank newlines
def Pvalues(lines):
    rlines = []
    for line in lines:
        if line.strip() != '':
            t = line.rstrip()
            e = rlines.append(t)
    return rlines

def listModel():
    sql = "SELECT * FROM users;"
    x.execute(sql)
    list = []
    for row in x:
        print(row[11])
        list.append(row[11])
    return list

def cfg(mac):
    sql3 = "SELECT model FROM users WHERE mac = '{}';".format(mac)
    #print(sql3)
    x.execute(sql3)
    #print(x)
    for row in x:
        #print(row[0])
        if row[0] == 1610:
            print(1610)
            template = Template_1610
            liness = Pvalues(OpenTemplate(template))
            dictt = {}
            for line in liness:
                lst = line.split("=")
                dictt.update({lst[i]: lst[i + 1] for i in range(0, len(lst), 2)})
            for key in dictt:
                if dictt[key] == '':
                    if key == "P270 ":
                        sql = "SELECT ext FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt["P270 "] = str(row[0])
                            dictt["P35 "] = str(row[0])
                            dictt["P36 "] = str(row[0])
                            dictt["P3 "] = str(row[0])
                        sql = "SELECT secret FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt["P34 "] = str(row[0])
            with open("./Create_CFG_Grandstream/Configs/1610/cfg" + mac + ".xml", "a") as file_object:
                file_object.truncate(0)
                logo = '<?xml version="1.0" encoding="UTF-8" ?>\n' \
                       '<!-- BroadSoft XML Provisioning Configuration -->\n' \
                       '<gs_provision version="1">\n' \
                       '<mac>{}</mac>\n' \
                       '  <config version="2">\n' \
                       '<!--###############################################################################################-->\n' \
                       '<!--####      1610  Configuration Template Exmaple for testing the converting tool             ####-->\n' \
                       '<!--###############################################################################################-->\n'.format(
                    mac)
                print(logo, file=file_object)
                dictt = {k.replace(" ", ""): v for k, v in dictt.items()}
                dictt = {k: v.strip() for k, v in dictt.items()}
                for key in dictt:
                    print("    " + "<" + key + ">" + dictt[key] + "</" + key + ">", file=file_object)
                footer = '	</config>\n' \
                         '</gs_provision>'
                print(footer, file=file_object)

        if row[0] == 2160 or row[0] == 2130:
            print(2160)
            template = Template_2160
            liness = Pvalues(OpenTemplate(template))
            dictt1 = {}
            for line in liness:
                lst = line.split("=")
                dictt1.update({lst[i]: lst[i + 1] for i in range(0, len(lst), 2)})
            for key in dictt1:
                if dictt1[key] == '':
                    if key == "P270 ":
                        sql = "SELECT ext FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt1["P270 "] = str(row[0])
                            dictt1["P35 "] = str(row[0])
                            dictt1["P36 "] = str(row[0])
                            dictt1["P3 "] = str(row[0])
                        sql = "SELECT secret FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt1["P34 "] = str(row[0])
            with open("./Create_CFG_Grandstream/Configs/21XX/cfg" + mac + ".xml", "a") as file_object:
                file_object.truncate(0)
                logo = '<?xml version="1.0" encoding="UTF-8" ?>\n' \
                       '<!-- BroadSoft XML Provisioning Configuration -->\n' \
                       '<gs_provision version="1">\n' \
                       '<mac>{}</mac>\n' \
                       '  <config version="2">\n' \
                       '<!--###############################################################################################-->\n' \
                       '<!--####      2160  Configuration Template Exmaple for testing the converting tool             ####-->\n' \
                       '<!--###############################################################################################-->\n'.format(
                    mac)
                print(logo, file=file_object)
                dictt1 = {k.replace(" ", ""): v for k, v in dictt1.items()}
                dictt1 = {k: v.strip() for k, v in dictt1.items()}
                for key in dictt1:
                    print("    " + "<" + key + ">" + dictt1[key] + "</" + key + ">", file=file_object)
                footer = '	</config>\n' \
                         '</gs_provision>'
                print(footer, file=file_object)

        if row[0] == 1611:
            print(1611)
            template = Template_1611
            liness = Pvalues(OpenTemplate(template))
            dictt1 = {}
            for line in liness:
                lst = line.split("=")
                dictt1.update({lst[i]: lst[i + 1] for i in range(0, len(lst), 2)})
            for key in dictt1:
                if dictt1[key] == '':
                    if key == "P270 ":
                        sql = "SELECT ext FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt1["P270 "] = str(row[0])
                            dictt1["P35 "] = str(row[0])
                            dictt1["P36 "] = str(row[0])
                            dictt1["P3 "] = str(row[0])
                        sql = "SELECT secret FROM users WHERE mac = '{}';".format(mac)
                        x.execute(sql)
                        for row in x:
                            dictt1["P34 "] = str(row[0])
            with open("./Create_CFG_Grandstream/Configs/1611/cfg" + mac + ".xml", "a") as file_object:
                file_object.truncate(0)
                logo = '<?xml version="1.0" encoding="UTF-8" ?>\n' \
                       '<!-- BroadSoft XML Provisioning Configuration -->\n' \
                       '<gs_provision version="1">\n' \
                       '<mac>{}</mac>\n' \
                       '  <config version="2">\n' \
                       '<!--###############################################################################################-->\n' \
                       '<!--####      1611  Configuration Template Exmaple for testing the converting tool             ####-->\n' \
                       '<!--###############################################################################################-->\n'.format(
                    mac)
                print(logo, file=file_object)
                dictt1 = {k.replace(" ", ""): v for k, v in dictt1.items()}
                dictt1 = {k: v.strip() for k, v in dictt1.items()}
                for key in dictt1:
                    print("    " + "<" + key + ">" + dictt1[key] + "</" + key + ">", file=file_object)
                footer = '	</config>\n' \
                         '</gs_provision>'
                print(footer, file=file_object)

def main():
    sql = "SELECT * FROM users;"
    x.execute(sql)
    list1 = []
    for row in x:
        list1.append(row[9])
    for x1 in list1:
        cfg("{}".format(x1))

main()
#if __name__ == '__main__':
#    main()
