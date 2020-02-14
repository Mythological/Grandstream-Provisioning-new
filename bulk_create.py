from os import remove
import csv
import re
import pymysql
from credentials import *

conn = pymysql.connect(host,user,password, db)

x = conn.cursor()

def csv_writer(data, path):
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


sql="SELECT * FROM users;"
x.execute(sql)

for row in x:
        ext = row[2]
        secret = row[10]
        if secret == None:
            secret = "REGEN"
        name = row[1]
        recording = "yes"
        try:
            outboundcid = row[12]
        except AttributeError:
            outboundcid = ""
        try:
            callgroup = row[7]
        except:
            callgroup = ""
        try:
            pickupgroup = row[6]
        except:
            pickupgroup = ""
        try:
            print(callgroup)
            callgroup = callgroup.replace('«', r'"')
            callgroup = callgroup.replace('»', r'"')
            callgroup1 = ('"'+str(callgroup)+'"')
            callgroup = callgroup1
        except:
            pass
        try:
            pickupgroup = pickupgroup.replace('«', r'"')
            pickupgroup = pickupgroup.replace('»', r'"')
            pickupgroup1 = ('"'+str(pickupgroup)+'"')
            pickupgroup = pickupgroup1
        except:
            pickupgroup = ""
        chanunavail_dest = '"app-blackhole,no-service,1"'
        busy_dest = '"app-blackhole,busy,1"'
        permit = "172.1.0.0/255.255.0.0"
        ring = "default"
        findme_ena = "yes"
        data1 = [['{},{},{},{},{},{},{},{},{},{},{},{}'.format(ext, secret, name, recording, recording, recording, recording, callgroup, pickupgroup, chanunavail_dest, busy_dest, permit)]]
        path1 = "BULK_tmp.csv"
        csv_writer(data1,path1)

fw = open("BULK_tmp.csv","r")
text_in7 = fw.read()
text_out6 = re.sub(r'"(?!")', '', text_in7)
text_out5 = re.sub(r'""', '"', text_out6)
print(text_out5)
text_out_end = "extension,secret,name,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,namedcallgroup,namedpickupgroup,chanunavail_dest,busy_dest,permit\n" + text_out5
f11 = open("BULK_Freepbx_MYSQL.csv","wb")
text_out65_bytes = bytes(text_out_end, encoding = 'utf-8')
f11.write(text_out65_bytes)

try:
    remove('BULK_tmp.csv')
except OSError:
    pass

print("extension,secret,name,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,namedcallgroup,namedpickupgroup,chanunavail_dest,busy_dest,permit  ¯\_(ツ)_/¯")
