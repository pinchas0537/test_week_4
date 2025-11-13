all_ch = [
        "a","b","c",
        "d","e","f",
        "g","h","i","j",
        "k","l","m","n",
        "o","p","q","r",
        "s","t","u","v",
        "w","x","y","z"]

def encrypted_caeser(text:str):
    nwe_text = ""
    body = { "text": text, "offset":4}
    for i in text:
        for j in all_ch:
            if i == j:
                a = all_ch.index(j) + body["offset"]
                nwe_text += all_ch[a]
    return {"encrypted_text": nwe_text}