import random

# ダミーの女性選手名リスト（各国から実在しそうな名前）
names = [
    "Shelly-Ann Fraser-Pryce", "Elaine Thompson-Herah", "Dina Asher-Smith", "Marie-Josée Ta Lou", "Sha'Carri Richardson",
    "Blessing Okagbare", "Murielle Ahouré", "Tori Bowie", "Carmelita Jeter", "Tianna Bartoletta",
    "Veronica Campbell-Brown", "Natasha Morrison", "Michelle-Lee Ahye", "Evelyn Ashford", "Mireille Ahouré",
    "Juliet Cuthbert", "Ewa Swoboda", "Ivet Lalova", "Christina Manning", "Asha Philip",
    "Rosângela Santos", "Daryll Neita", "Gina Lückenkemper", "Tatjana Pinto", "Ajla Del Ponte",
    "Mujinga Kambundji", "Marie Gayot", "Carina Horn", "Geraldine Pillay", "Ezinne Okparaebo",
    "Blessing Okagbare", "Kelly-Ann Baptiste", "Barbara Pierre", "Tianna Madison", "English Gardner",
    "Jodie Williams", "Maja Mihalinec", "Ewa Swoboda", "Dafne Schippers", "Murielle Ahouré",
    "Marie-Josée Ta Lou", "Natasha Morrison", "Michelle-Lee Ahye", "Elaine Thompson", "Shelly-Ann Fraser",
    "Carmelita Jeter", "Dina Asher", "Asha Philip", "Tatjana Pinto", "Gina Lückenkemper"
]

# ダミーの国リスト
countries = [
    "ジャマイカ", "アメリカ", "イギリス", "コートジボワール", "ナイジェリア", "ポーランド", "ブルガリア", "ドイツ", "スイス", "ブラジル",
    "フランス", "南アフリカ", "ノルウェー", "トリニダード・トバゴ", "カナダ", "スペイン", "イタリア", "オランダ", "オーストラリア", "日本"
]

# ダミーの好きな食べ物リスト
foods = [
    "寿司", "ピザ", "ハンバーガー", "パスタ", "カレー", "ラーメン", "タコス", "ステーキ", "サラダ", "焼肉",
    "餃子", "パンケーキ", "サンドイッチ", "チョコレート", "アイスクリーム", "フライドチキン", "うどん", "そば", "天ぷら", "お好み焼き"
]

# 50人分の選手データ生成
athletes = []
for i in range(50):
    name = names[i % len(names)]
    country = random.choice(countries)
    food = random.choice(foods)
    time = round(random.uniform(9.56, 12.99), 2)
    athletes.append({
        "name": name,
        "country": country,
        "food": food,
        "time": time
    })

# タイムが良い順（昇順）に並び替え
athletes_sorted = sorted(athletes, key=lambda x: x["time"])

# 結果表示
print(f"{'順位':<4} {'名前':<30} {'国':<15} {'好きな食べ物':<10} {'タイム':<5}")
for idx, athlete in enumerate(athletes_sorted, 1):
    print(f"{idx:<4} {athlete['name']:<30} {athlete['country']:<15} {athlete['food']:<10} {athlete['time']:<5}")