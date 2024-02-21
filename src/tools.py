import patoolib
from os import listdir


def unarchive(chat_id, file_name, password):

    file_adress = f"/home/container/downloads/{file_name}"
    
    if password == "the file is not locked":
        patoolib.extract_archive(file_adress, outdir=f"/home/container/users_file/{chat_id}/files/")
    else:
        patoolib.extract_archive(file_adress, outdir=f"/home/container/users_file/{chat_id}/files/")
    
    files_list = listdir(f"/home/container/users_file{chat_id}/files/")
    
    final_file_adresses = []
    for file in files_list:
        
        final_file_adresses.append(f"/home/container/users_file/{chat_id}/files/{file}")
        
    return final_file_adresses