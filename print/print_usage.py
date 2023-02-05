# デフォルト状態
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

gl = ['alpha','beta','gamma']

print('Hello')                      # Hello

print(gl)                     # ['alpha', 'beta', 'gamma']
print(*gl)                    # alpha beta gamma

print(*gl, sep=' $ ')         # alpha $ beta $ gamma  <-separate
print(*gl, end=' $ ')         #  alpha beta gamma $   <- 改行していない
print("")                           # 改行
     
for i in gl:                        # alpha
    print(i)                        # beta
                                    # gamma  <- 列で出力
for i in gl:
    print(i, end=' ')               # alpha beta gamma  <- 行で出力
