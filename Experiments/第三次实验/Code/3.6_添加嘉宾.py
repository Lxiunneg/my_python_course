Ren = ["Liuxiunneg", "JayR", "gag"]

Ren.insert(0, "FirstMen")
Ren.insert(2, "TheMiddleMan")
Ren.append("LastMen")

for men in Ren:
    print(f"{men},Can you join my party?")

print('\n')

while len(Ren) != 2:
    Ren.pop()


for men in Ren:
    print(f"{men},Can you join my party?")
