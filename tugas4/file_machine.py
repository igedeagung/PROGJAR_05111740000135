from file import File
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = File()

class FileMachine:
    def proses(self,string_to_process, data):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                p.Upload(nama,data)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                hasil = p.List()
                hasil={"file":hasil}
                return json.dumps(hasil)
            elif (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                hasil = p.Download(nama)
                # hasil = nama
                return hasil
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = FileMachine()
    # data=open("File Client/number.txt", "rb")
    #     # pm.proses("upload number.txt", data.read())
    #     # hasil = pm.proses("list", "null")
    #     # print(hasil)
    # print(p.Download("pms.txt"))
    hasil = pm.proses("download pms.txt", "null")
    print(hasil)