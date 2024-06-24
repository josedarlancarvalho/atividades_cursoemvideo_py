#sabendo se nasceu em uma cidade que comeca com santo no nome

cidade = str(input("qual cidade voce nasceu?")).strip()
print(cidade[:5].upper() == "SANTO")
