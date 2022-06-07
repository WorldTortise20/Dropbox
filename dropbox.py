import dropbox
import os

#Create Transfer Data class
class TransferData (object):
    def __init__(self,access_token):
        self.access_token = access_token
    
    def uploadFile(self, ogfile, newfile):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(ogfile):
            for filename in files:
                localPath = os.path.join(root, filename)

                relativePath = os.path.relpath(localPath, ogfile)
                dbxPath = os.path.join(newfile, relativePath)
                
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dbxPath, mode = dropbox.files.WriteMode.overwrite)

def main():
    accessToken = 'sl.BJEACaY6snxiMyxlwPC3SnOIxP3bBTYDD-VWncSJkLVEwpAKz_8OzYRqn8BHTab9wT0Bf_z-gy2VZ3mhI4iTwOI_Cw-9jKInHaTo1TlUTfdkOcPK81uXvSf2OHLoCCZQxBDH-yM'
    transferData = TransferData(accessToken)

    file_from = str(input("Enter the file or folder path you wish to upload to Dropbox!- "))
    fileTo = input("Enter the full path to Dropbox- ")

    transferData.uploadFile(file_from, fileTo)
    print("File transfered!")

main()