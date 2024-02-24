import os
import pyunpack
def unarchive(chat_id, file_name, password):

    file_adress = f"/home/container/downloads/{file_name}"
    
    path = f"/home/container/users_file/{str(chat_id)}"
    os.mkdir(path)
    
    if password == "the file is not locked":
        pyunpack.Archive(filename=file_adress).extractall(directory=f"{path}/")
    else:
        pyunpack.Archive(filename=file_adress,password=password).extractall(directory=f"{path}/")
    
    files_list = os.listdir(f"{path}/")
    
    final_file_adresses = []
    for file in files_list:
        
        final_file_adresses.append(f"/home/container/users_file/{chat_id}/{file}")
        
    return final_file_adresses