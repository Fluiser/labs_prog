import pandas as pd 

data = pd.read_csv('countries.csv')

small_area = data.nsmallest(10, "area")
large_area = data.nlargest(10, "area")
fr_speaking = data[data["languages"].str.contains("French", case=False, na=False)]
islands = data[(data["landlocked"] == False) & (data["borders"].isna() | (data["borders"] == "[]"))]
S_countries = data[data["latlng"].apply(lambda x: float(x.split(",")[0]) < 0 if pd.notna(x) else False)]



print('10 самых больших стран по территории:')
print(small_area[["translations.rus.common", "area"]])


print('10 самых маленьких стран по территории:')
print(large_area[["translations.rus.common", "area"]])

if 'population' in data:
    small_pop = data.nsmallest(10, "population")
    large_pop = data.nlargest(10, "population")
    print('10 самых больших стран по популяции:')
    print(large_pop[["translations.rus.common", "area"]])
    print('10 самых маленьких стран по популяции:')
    print(small_pop[["translations.rus.common", "area"]])
else:
    print("Нет столбца population")

print(f'Франкоязычные страны:')
print(fr_speaking[["translations.rus.common"]])
print(f'Острова:')
print(islands[["translations.rus.common"]])
print(f'Страны на южном полушарии: ')
print(S_countries[["translations.rus.common"]])

print("Группировки\nГруппировка по первой букве:")
group_by_char = data.groupby(data["translations.rus.common"].str[0])
print(
    "; ".join([
        f'{char}: {len(cnts)} стран' for char, cnts in group_by_char
    ])
)

if 'population' in data:
    print("Группировка по населению:")
    population_bins = [0, 100_000, 500_000, 1_000_000, 10_000_000, 50_000_000, 200_000_000, 2_000_000_000]
    group_by_population = data.groupby(pd.cut(data['population'], bins=population_bins), observed=True)
    print(
        "; ".join([
            f'{pop}: {len(cnts)} стран' for pop, cnts in group_by_population
        ])
    )

print("Группировка по территории")
area_bins = [0, 100, 1_000, 10_000, 100_000, 1_000_000, 20_000_000]
group_by_area = data.groupby(pd.cut(data['area'], bins=area_bins), observed=True)
print(
    "; ".join([
        f'{ar}: {len(cnts)} стран' for ar, cnts in group_by_area
    ])
)

columns = [
    "translations.rus.common",
    "capital",
    "area",
    "currencies",
    "latlng"
]

if "population" in data:
    colums += ["population"]

data[columns].to_excel("excel_file.xlsx")