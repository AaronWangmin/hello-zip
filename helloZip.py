import os
import zipfile

# f = zipfile.ZipFile("test1.zip",'w',zipfile.ZIP_DEFLATED)
# f.setpassword("1234".encode())
# f.write('./test.txt')
# print("zip ok...")

# f.extractall("./test1/",pwd = b"1234")
# print(unzip ok...)
# f.close()

passwordList = [
    "jica311",
    "jica314",
    "1234"]

sourcePath = "./nas/output/online/simple/"
targetDir = "./uuu/"

zipFileDir = "./ttt/test2.zip"

def unzipOneFileByPasswords(zipFileDir,unzipfilePath,passwordList):
    f = zipfile.ZipFile(zipFileDir)

    pwdIndex = 0
    while (pwdIndex < len(passwordList)):
        password = passwordList[pwdIndex]
        try:
            print("hello....")
            f.extractall(unzipfilePath,pwd = password.encode())        
            print("unzip ok...")
            break        
        except Exception:        
            pwdIndex += 1  

    f.close()

#
totalOfUnzipFiles = 0
for zf in os.listdir(sourcePath):
    unzipOneFileByPasswords(sourcePath + zf,targetDir,passwordList)
    totalOfUnzipFiles =+ 1
print("the total of unzip files: %d ",totalOfUnzipFiles)









