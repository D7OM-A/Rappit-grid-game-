garden = [["🥕","🥕","🥕"] , ["🥕","🥕","🥕"] , ["🥕","🥕","🥕"]]
print("Welcome to place the rabbit\n")
print(f"{garden[0]}\n{garden[1]}\n{garden[2]}\n")
print("Where should the rabbit go? 🐇")
choose = input("Please chhose a row and a column: ")
row = int(choose[0]) -1
col = int(choose[1]) -1 
garden [row][col] = "🐇"
print("\nSuccess .....\n")
print(f"{garden[0]}\n{garden[1]}\n{garden[2]}\n")
