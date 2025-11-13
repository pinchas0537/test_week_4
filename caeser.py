all_ch = [
        "a","b","c",
        "d","e","f",
        "g","h","i","j",
        "k","l","m","n",
        "o","p","q","r",
        "s","t","u","v",
        "w","x","y","z"]

def encrypted_caeser(text:str, offset:int,mood: str):
    nwe_text = ""
    for i in text:
        for j in all_ch:
            if i == j:
                a = all_ch.index(j) + offset
                nwe_text += all_ch[a]

    return {mood+"_text" : nwe_text}
