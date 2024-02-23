from os import listdir
import pyunpack
def unarchive(chat_id, file_name, password):

    file_adress = f"/home/container/downloads/{file_name}"
    
    if password == "the file is not locked":
        pyunpack.Archive(filename=file_adress).extractall(directory=f"/home/container/users_file/{chat_id}/files/")
    else:
        pyunpack.Archive(filename=file_adress,password=password).extractall(directory=f"/home/container/{chat_id}/")
    
    files_list = listdir(f"/home/container/users_file/{chat_id}/files/")
    
    final_file_adresses = []
    for file in files_list:
        
        final_file_adresses.append(f"/home/container/users_file/{chat_id}/files/{file}")
        
    return final_file_adresses