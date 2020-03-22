import shelve
import uuid
import os
import io


class File:
    def Upload(self,nama=None,data=None):
        f=open("File Server/"+nama, "wb")
        f.write(data)
        f.close()
        return True
    def Download(self,nama=None):
        if os.path.isfile("File Server/"+nama):
            myfile = open("File Server/"+nama, "rb")
            data=myfile.read()
            myfile.close()
        else:
            data=b'File not Exist'
        return data
    def List(self):
        list = os.listdir("File Server")
        f = []
        for filename in list:
            f.append(filename)
        return f

if __name__=='__main__':
    p = File()
    # data=open("File Client/171076.jpg", 'rb')
    # p.Upload("171076.jpg",data.read())
    # print(p.List())
    print(p.Download("IC.png"))
