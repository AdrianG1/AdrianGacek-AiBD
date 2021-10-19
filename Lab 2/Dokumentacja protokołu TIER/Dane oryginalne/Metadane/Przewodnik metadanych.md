# Przewodnik metadanych
Dane oryginalne zawierają się w pliku weather.txt w folderze Dane oryginalne. Zostały one pobrane z  [`konspektu`](https://github.com/KAIR-ISZ/public_lectures/tree/master/Analiza%20i%20Bazy%20Danych%202021/Lab%202) do laboratorium 2. przedmiotu Analizy i Bazy Danych

Plik weather.txt zawiera dane pogodowe z Global Historical Climatology Network dla jednej stacji pogodowej (MX17004) w Meksyku przez pięć miesięcy w 2010 roku. 

Pierwsza kolumna zawiera dane (id, rok, miesiąc,nazwa zmiennych), w pozostałych kolumnach są wartości zmiennych na dany dzien miesiąca (dzień, d1 – d31). Miesiące z mniej niż 31 dni mają strukturalne brakujące wartości reprezentowane jako liczba -9999 dla ostatniego dnia (dni) miesiąca.