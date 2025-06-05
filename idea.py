# 簡単な選択式クイズプログラム

quiz = [
    {
        "question": "100m走の世界記録保持者は誰？",
        "choices": ["1. ウサイン・ボルト", "2. カール・ルイス", "3. ジャスティン・ガトリン", "4. アサファ・パウエル"],
        "answer": 1
    },
    {
        "question": "野球で1試合に必要なアウトの数（片方のチーム）は？",
        "choices": ["1. 9", "2. 18", "3. 27", "4. 36"],
        "answer": 3
    },
    {
        "question": "サッカーのフィールドにいる選手の人数（1チーム）は？",
        "choices": ["1. 7", "2. 9", "3. 10", "4. 11"],
        "answer": 4
    }
]

score = 0

for idx, q in enumerate(quiz, 1):
    print(f"Q{idx}: {q['question']}")
    for choice in q["choices"]:
        print(choice)
    ans = input("番号で答えてください: ")
    if ans.isdigit() and int(ans) == q["answer"]:
        print("正解！\n")
        score += 1
    else:
        print(f"不正解。正解は {q['choices'][q['answer']-1]} です。\n")

print(f"あなたの正解数: {score} / {len(quiz)}")