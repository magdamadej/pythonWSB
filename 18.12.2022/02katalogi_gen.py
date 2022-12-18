import os

if os.path.isdir('RAPORT') != True:
    os.mkdir("RAPORT")

names_list = ["Kowalski", "Nowak", "Podolski", "Kupczyk", "Urban", "Rakoczy", "Misztal", "Nawrocki", "Lewandowski", "Czapski"]
years_list = [str(i) for i in range(2010, 2022)]
print(years_list)
months_list = [f"{str(i).zfill(2)}_raport" for i in range(1, 13)]

for name in names_list:
    path = os.path.join('RAPORT', name)
    os.mkdir(path)
    for year in years_list:
        path1 = os.path.join('RAPORT', name, year)
        os.mkdir(path1)
        for month in months_list:
            path2 = os.path.join('RAPORT', name, year, month)
            os.mkdir(path2)