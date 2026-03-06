import random
import datetime
import itertools

teams = [
    "самые первые",
    "вторые лучше",
    "третья команда",
    "команда четвёртых",
    "команда пятых",
    "команда шестых",
    "команда седьмых",
    "супер футболисты",
    "команда девятых",
    "ультра футбол",
    "команда 11",
    "бравые футболисты",
    "сильные футболисты",
    "футбольная команда",
    "команда 15",
    "тагил"
]

timestamp = datetime.datetime(2016, 9, 14, 22, 45)
step_time = datetime.timedelta(weeks=2)

random.shuffle(teams);
groups = [teams[i:i+4] for i in range(0, 16, 4)]

for i in range(0, 4):
    print(f"{i+1}-я группа:");
    for team in groups[i]:
        print(f"\t{team}")

print("\n");

for i in range(0, 4):
    print(f"Матчи {i+1}й группы:")
    matches = itertools.combinations(groups[i], 2)
    for t1, t2 in matches:
        print(f"\t{timestamp.strftime('%d/%m/%Y, %H:%M')}: {t1} vs {t2}")
        timestamp += step_time