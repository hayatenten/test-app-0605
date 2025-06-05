import random

# ダミーの名前リスト（実在しそうな名前を各国から）
names = [
    "Usain Bolt", "Yohan Blake", "Justin Gatlin", "Asafa Powell", "Tyson Gay",
    "Andre De Grasse", "Akani Simbine", "Su Bingtian", "Jimmy Vicaut", "Trayvon Bromell",
    "Ramil Guliyev", "Zharnel Hughes", "Filippo Tortu", "Yoshihide Kiryu", "Abdul Hakim Sani Brown",
    "Marcell Jacobs", "Fred Kerley", "Lamont Jacobs", "Noah Lyles", "Christian Coleman",
    "Aaron Brown", "Michael Norman", "Divine Oduduru", "Enoch Adegoke", "Reece Prescod",
    "Chijindu Ujah", "Richard Kilty", "Bingtian Su", "Hassan Taftian", "Arthur Cissé",
    "Simone Collio", "Francis Obikwelu", "Kim Collins", "Nesta Carter", "Nickel Ashmeade",
    "Ronnie Baker", "Isiah Young", "Bruno Hortelano", "Adam Gemili", "Samuel Francis",
    "James Dasaolu", "Mark Lewis-Francis", "Dwain Chambers", "Julian Forte", "Michael Rodgers",
    "Christophe Lemaitre", "Jak Ali Harvey", "Emre Zafer Barnes", "Yap Kim Wai", "Shingo Suetsugu"
]

# ダミーの国リスト
countries = [
    "ジャマイカ", "アメリカ", "カナダ", "中国", "フランス", "イタリア", "イギリス", "ナイジェリア", "トルコ", "日本",
    "スペイン", "ドイツ", "ブラジル", "オーストラリア", "南アフリカ", "カタール", "ガーナ", "トリニダード・トバゴ", "韓国", "ロシア"
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
print(f"{'順位':<4} {'名前':<25} {'国':<10} {'好きな食べ物':<10} {'タイム':<5}")
for idx, athlete in enumerate(athletes_sorted, 1):
    print(f"{idx:<4} {athlete['name']:<25} {athlete['country']:<10} {athlete['food']:<10} {athlete['time']:<5}")
