import random

# ダミーの男性野球選手名リスト（実在しそうな名前）
names = [
    "Shohei Ohtani", "Aaron Judge", "Mike Trout", "Bryce Harper", "Vladimir Guerrero Jr.",
    "Fernando Tatis Jr.", "Juan Soto", "Ronald Acuña Jr.", "Mookie Betts", "Freddie Freeman",
    "Yordan Alvarez", "Jose Ramirez", "Rafael Devers", "Pete Alonso", "Corey Seager",
    "Kyle Schwarber", "Matt Olson", "Paul Goldschmidt", "Nolan Arenado", "Manny Machado",
    "Trea Turner", "Francisco Lindor", "Bo Bichette", "Julio Rodriguez", "Jose Altuve",
    "Alex Bregman", "George Springer", "Anthony Rizzo", "Giancarlo Stanton", "Javier Baez",
    "Xander Bogaerts", "Christian Yelich", "Cody Bellinger", "Joey Gallo", "Teoscar Hernandez",
    "Eugenio Suarez", "Josh Donaldson", "Nelson Cruz", "J.D. Martinez", "Tim Anderson",
    "Dansby Swanson", "Ozzie Albies", "Willson Contreras", "Salvador Perez", "Whit Merrifield",
    "Charlie Blackmon", "Max Muncy", "Hunter Renfroe", "Brandon Lowe", "Austin Riley"
]

# 50人分の選手データ生成
players = []
for i in range(50):
    name = names[i % len(names)]
    homeruns = random.randint(10, 30)
    players.append({
        "name": name,
        "homeruns": homeruns
    })

# ホームラン数が多い順（降順）に並び替え
players_sorted = sorted(players, key=lambda x: x["homeruns"], reverse=True)

# 結果表示
print(f"{'順位':<4} {'名前':<25} {'ホームラン数':<10}")
for idx, player in enumerate(players_sorted, 1):
    print(f"{idx:<4} {player['name']:<25} {player['homeruns']:<10}")