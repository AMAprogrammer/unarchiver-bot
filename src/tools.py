import patoolib
from os import listdir


def unarchive(chat_id, file_name, password):

    file_adress = f"/files/{chat_id}/{file_name}"
    
    if password == "the file is not locked":
        patoolib.extract_archive(file_adress, outdir=f"/files/{chat_id}/files")
    else:
        patoolib.extract_archive(file_adress, outdir=f"/files/{chat_id}/files")
    
    files_list = listdir(f"/files{chat_id}")
    
    final_file_adresses = []
    for file in files_list:
        
        final_file_adresses.append(f"/files/{chat_id}/files/{file}")
        
    return final_file_adresses