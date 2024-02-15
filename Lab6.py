# Bartosz Borek
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych z pliku CSV
fPath = r'E:\wprowadzenie do programowania - studia\lab6\dane.csv'
readFile = pd.read_csv(fPath, sep=';')

# Uzupełnienie brakujących wartości w kolumnie 'Kalorie'
caloriesMedian = readFile['Kalorie'].median()
readFile['Kalorie'].fillna(caloriesMedian, inplace=True)

# Upiekszenie tabeli
readFile.columns = ['Duration (min)', 'Pulse', 'Max Pulse', 'Calories']
formattedDate = readFile.round(2)

# Ustawienie stylu dla wykresów
sns.set(style="whitegrid")

# Tworzenie wielu wykresów
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

# Zmiana kolorów wykresów
# Histogram czasu trwania
sns.histplot(data=formattedDate, x='Duration (min)', bins=40,
             ax=axes[0, 0], color='#1f77b4')  # Niebieski
axes[0, 0].set_title('Histogram of Duration')

# Histogram pulsu
sns.histplot(data=formattedDate, x='Pulse', bins=40,
             ax=axes[0, 1], color='#ff7f0e')  # Pomarańczowy
axes[0, 1].set_title('Histogram of Pulse')

# Scatter plot Kalorie vs Czas Trwania
sns.scatterplot(data=formattedDate, x='Duration (min)',
                y='Calories', ax=axes[1, 0], color='#2ca02c')  # Zielony
axes[1, 0].set_title('Calories vs Duration')

# Scatter plot Maksymalny Puls vs Puls
sns.scatterplot(data=formattedDate, x='Pulse', y='Max Pulse',
                ax=axes[1, 1], color='#d62728')  # Czerwony
axes[1, 1].set_title('Max Pulse vs Pulse')

# Dostosowanie layoutu i wyświetlenie wykresów
plt.tight_layout()
plt.show()

# Eksport oczyszczonych danych do nowego pliku CSV
finalResult = 'E:\wprowadzenie do programowania - studia\lab6\formatted.csv'
formattedDate.to_csv(finalResult, index=False)

# Wynik
print(formattedDate)
