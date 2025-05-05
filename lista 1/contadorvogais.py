frase = input("Digite uma frase: ")
print(f"Na frase \"{frase}\" tem:\n",
      f"A ou a: {frase.count("a")+frase.count("A")}\n",
      f"E ou e: {frase.count("e")+frase.count("E")}\n",
      f"I ou i: {frase.count("i")+frase.count("I")}\n",
      f"O ou o: {frase.count("o")+frase.count("O")}\n",
      f"U ou u: {frase.count("u")+frase.count("U")}\n")