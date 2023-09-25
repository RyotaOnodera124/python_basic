users_info = [["Bob", 79],
              ["Tom", 59],
              ["Ken", 61]]

# users_infoの各要素から名前と年齢を取得し、指定されたフォーマットで出力
for user in users_info:
    name = user[0]
    age = user[1]
    print(f"Name: {name}, Age: {age}")
