import os
import shutil
main_files = os.listdir("./")
main_files.remove("main.py")

def move(folderName, files):
    for file_element in files:
        shutil.move(file_element, folderName)

def createFolder(folder):
    if folder not in main_files:
        os.makedirs(folder)

createFolder("Images")
createFolder("Medias")
createFolder("Documents")
createFolder("Others")
createFolder("Compressed Files")

    
imgExtList = ['.jpg', '.jpeg', '.heif', '.png', '.svg']
images = [index for index in main_files if os.path.splitext(index)[1].lower() in imgExtList]

DocumentExtList = ['.docx', '.doc', '.pdf', '.pages', '.ppt', '.pptx']
Documents = [index for index in main_files if os.path.splitext(index)[1].lower() in DocumentExtList]

compressedExt = ['.zip', '.rar']
compressedFiles = [index for index in main_files if os.path.splitext(index)[1].lower() in compressedExt]

MediaExtList = ['.mp3', '.mp4', '.3gp', 'mkv' '.flv']
Medias = [index for index in main_files if os.path.splitext(index)[1].lower() in MediaExtList]

others = []
for i in main_files:
    if(i not in images) and (i not in Documents) and (i not in Medias) and (i not in compressedFiles) and os.path.isfile(i):
        others.append(i)


# Moving Files into their corresponding folders
move("Images", images)
move("Medias", Medias)
move("Documents", Documents)
move("Others", others)
move("Compressed Files", compressedFiles)

