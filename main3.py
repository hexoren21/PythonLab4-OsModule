import sys
print(sys.version_info)
if sys.version_info.major < 3:
    print("powinienes zaktualizwoac swoja wersje python")
elif sys.version_info.minor < 7:
     print("Twoja werja Python nie jest najnowsza")
else:
    print("wszysto w porzadku")