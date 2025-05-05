print("Digite os valores de P1(x,y) e P2(x,y): ")
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))

dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)

print(f"A distancia entre P1({x1:.2f},{y1:.2f})",
      f"e P2({x2:.2f},{y2:.2f}) é {dist:.2f}")