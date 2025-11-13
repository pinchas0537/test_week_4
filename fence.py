def encrypt_fance(text:str):
    odd_number = ""
    double = ""
    all_ = ""
    new_taxt = text.replace(" ","")
    for i in range(len(new_taxt)):
        if i % 2 == 1:
            odd_number += new_taxt[i]
        else:
            double += new_taxt[i]
    all_ += double + odd_number
    return {"encrypted_text":all_}
