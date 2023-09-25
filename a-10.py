import random

def dice():
    return random.randint(1, 6)

# dice() 関数を呼び出してランダムな整数を取得し、出力
result = dice()
print(result)
