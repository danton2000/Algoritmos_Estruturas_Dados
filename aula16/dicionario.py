carro1 = {
    "modelo": "Renegade",
    "ano": 2021
}

print(carro1)

print(carro1["modelo"])

carro1["cor"] = "Prata"

print(carro1)

del carro1["cor"]

print(carro1)

carro2 = {
    "modelo": "Doblo",
    "ano": 2006,
    "cor": "Prata"
}

carro3 = {
    "modelo": "Uno",
    "ano": 2024,
    "cor": "Prata"
}

carro4 = ["Jeep", 2020, "Prata"]

frota = carro1, carro2, carro4 

#frota[1] = carro3

print(frota)

carro2["modelo"] = "Toro"

print(frota)