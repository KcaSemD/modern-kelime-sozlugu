meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FAKE":"Gerçek olmayan sahte",
            "TROLL":"ironik bir şey",
            "BRUH":"bir şey olacakken olmamış olması"
}

while True:
    word = input("Anlamadığınız bir kelime girin(Gireceğiniz kelime büyük harfli olmalı):")
    
    if word in meme_dict.keys():
        print("Girdiğiniz kelimenin anlamı:",meme_dict[word])
    else:
        print("Maalesef aradığınız kelime yanış veye sözlükte yok...")
