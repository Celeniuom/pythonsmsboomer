import requests

while True:
    kime=input("kim:")
    mesaj=input("mesaj:")
    if "" in kime or mesaj =="":
        break
    resp=requests.post("https://textbelt.com/test", {
        'phone':'{}'.format(kime)
        'message':'{}'.format(mesaj) 
        'key':'textbelt'   

    })    
    print("İşlem:{} kalan hakkınız: {}".format('Basarili'if resp.json()['success'] == 'True'
                                                else 'basarisiz!!!' ,resp.json()['quotaRemaining']))
    c = input("'exit()' or 'Enter' ")
    if c == "exit()"
        break
    else
        pass