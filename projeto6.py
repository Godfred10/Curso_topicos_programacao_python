
displayInventory = {"rope":"1","torch":"6","gold":"42","dagger":"1","shield":"1"}

print("inventario :","\nrope:" + displayInventory["rope"],"\ntorch:"+displayInventory["torch"],"\ngold:"+displayInventory["gold"], "\ndagger:"+displayInventory["dagger"],"\nshield:"+displayInventory["shield"])
x = displayInventory.values()
x = list(x)

print("total:",int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4]),"itens")

