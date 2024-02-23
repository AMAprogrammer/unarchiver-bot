import os
import pyunpack
def unarchive(chat_id, file_name, password):

    file_adress = f"/home/container/downloads/{file_name}"
    
    parent_dir = "/home/container/users_file"
    path = os.path.join(parent_dir, str(chat_id))
    os.mkdir(path)
    
    if password == "the file is not locked":
        pyunpack.Archive(filename=file_adress).extractall(directory=f"/home/container/users_file/{chat_id}/")
    else:
        pyunpack.Archive(filename=file_adress,password=password).extractall(directory=f"/home/container/users_file/{chat_id}/")
    
    files_list = os.listdir(f"/home/container/users_file/{chat_id}/")
    
    final_file_adresses = []
    for file in files_list:
        
        final_file_adresses.append(f"/home/container/users_file/{chat_id}/{file}")
        
    return final_file_adresses