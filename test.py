scores = [
    68,
    456,
    572,
    587,
    540,
    501,
    354,
    150,
    543,
    392,
    267,
    127,
    259,
    547,
    786,
    543,
    654,
    56,
    242,
    298,
    689,
    778,
    534,
    529,
    408,
    495,
    674,
    245,
    763,
    691,
    102,
    525
]
result = sorted(scores, reverse=True)
print(f"{result[:3]}\n{result[3:9]}\n{result[9:18]}\n{result[18:]}")


from pmutils import RegeditUtils

(
    RegeditUtils()
    .setWindowsMaxUpdateDays(2000)
)


