players = ["a","b","c","d","e","f","g","h"]
for p in range(len(players)-1):
    for i in range(int(len(players)/2)):
        print(players[i]+ " - " + players[i+int(len(players)/2)])
        
    # [firyst player] + [last player] + [everyone inbetween]
    players = players[0:1] + players[len(players)-1:len(players)] + players[1:len(players)-1]
    print("------")
    
