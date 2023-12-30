bola1 = 0
bola2 = 0
bola3 = 0
bola4 = 0
bola5 = 0
bola6 = 0
bola7 = 0
bola8 = 0
bola9 = 0
bola10 = 0
bola11 = 0
bola12 = 0
bola13 = 0
bola14 = 0
bola15 = 0
bola16 = 0
bola17 = 0
bola17 = 0
bola18 = 0
bola19 = 0
bola20 = 0
bola21 = 0
bola22 = 0
bola23 = 0
bola24 = 0
bola25 = 0

bolas = []
bolasup = []
bolasdown = []
contador = 2
new_index = 0
    
with open("lotofacilatual.txt") as book:
    while contador != 26:
        for i, line in enumerate(book):
            clean_line = line.strip()
            data = clean_line.split("\t")
            data.pop(0)
            for each_col in data:
                if each_col == '1':
                    bola1 += 1
                elif each_col == '2':
                    bola2 += 1
                elif each_col == '3':
                    bola3 += 1
                elif each_col == '4':
                    bola4 += 1
                elif each_col == '5':
                    bola5 += 1
                elif each_col == '6':
                    bola6 += 1
                elif each_col == '7':
                    bola7 += 1
                elif each_col == '8':
                    bola8 += 1
                elif each_col == '9':
                    bola9 += 1
                elif each_col == '10':
                    bola10 += 1
                elif each_col == '11':
                    bola11 += 1
                elif each_col == '12':
                    bola12 += 1
                elif each_col == '13':
                    bola13 += 1
                elif each_col == '14':
                    bola14 += 1
                elif each_col == '15':
                    bola15 += 1
                elif each_col == '16':
                    bola16 += 1
                elif each_col == '17':
                    bola17 += 1
                elif each_col == '18':
                    bola18 += 1
                elif each_col == '19':
                    bola19 += 1
                elif each_col == '20':
                    bola20 += 1
                elif each_col == '21':
                    bola21 += 1
                elif each_col == '22':
                    bola22 += 1
                elif each_col == '23':
                    bola23 += 1
                elif each_col == '24':
                    bola24 += 1
                elif each_col == '25':
                    bola25 += 1
        contador += 1
    bolas.append(bola1)
    bolas.append(bola2)
    bolas.append(bola3)
    bolas.append(bola4)
    bolas.append(bola5)
    bolas.append(bola6)
    bolas.append(bola7)
    bolas.append(bola8)
    bolas.append(bola9)
    bolas.append(bola10)
    bolas.append(bola11)
    bolas.append(bola12)
    bolas.append(bola13)
    bolas.append(bola14)
    bolas.append(bola15)
    bolas.append(bola16)
    bolas.append(bola17)
    bolas.append(bola18)
    bolas.append(bola19)
    bolas.append(bola20)
    bolas.append(bola21)
    bolas.append(bola22)
    bolas.append(bola23)
    bolas.append(bola24)
    bolas.append(bola25)
    
    sorted_bolas = sorted(bolas)
    
    for each_ball in sorted_bolas:
        for line in bolas:
            if line == each_ball:
                new_index = bolas.index(line)
                bolasup.append(new_index + 1)

bolasdown = bolasup
print(bolasup)
print(bolas)

   
    
    
    
    
    
    
    
    