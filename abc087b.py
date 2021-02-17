#ABC087B Coins

a = int(input())
b = int(input()) # number of 500yen coin
c = int(input()) #100yen
x = int(input()) #50yen
num_combination = 0 #Total amount
for n500 in range(0, a+1):
    for n100 in range(0, b+1):
         #for n50 in range(0, c+1):
        n50 = (x - n500*500 - n100*100) // 50
            #amount = n500*500+n100*100+n50*50
            #print(n500, n100, n50, amount)
            #if amount == x :
        if n50 <= c and n50>=0:
                #print(n500, n100, n50)
                num_combination += 1

print(num_combination)