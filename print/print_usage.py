# デフォルト状態
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

mugiwara = ["Luffy","Zoro","Nami"]

print("Hello")                      # Hello

print(mugiwara)                     # ['Luffy', 'Zoro', 'Nami']
print(*mugiwara)                    # Luffy Zoro Nami

print(*mugiwara, sep=' $ ')         # Luffy $ Zoro $ Nami
print(*mugiwara, end=' $ ')         # Luffy Zoro Nami $   <- 改行していない
print("")                           # 改行
     
for i in mugiwara:                  # Luffy
    print(i)                        # Zoro
                                    # Nami  <- 列で出力
for i in mugiwara:
    print(i, end=' ')               #Luffy Zoro Nami  <- 行で出力