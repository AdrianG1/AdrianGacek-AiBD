# TIER protocol i tidy data

W celu zapoznania z protokołem TIER oraz zagadnieniem tidy data należało pobrać i uporządkować przydzielony zbiór danych. W niniejszym projekcie należało pracować nad danymi zawartymi w pliku weather.txt dostępnym w [`konspekcie`](https://github.com/KAIR-ISZ/public_lectures/tree/master/Analiza%20i%20Bazy%20Danych%202021/Lab%202) do laboratorium.

Projekt został zorganizowany wg zasad protokołu TIER. Podstawą struktury są cztery następujące foldery: [`Dane analizy`](#Dane-analizy), [`Dane oryginalne`](#Dane-oryginalne), [`Dokumenty`](#Dokumenty) oraz [`Pliki poleceń`](#Pliki-poleceń).


## Dane oryginalne

Folder zawiera:

- weather.txt - nieprzetworzony plik który jest tematem analizy.

- Metadane - folder zawierający plik przewodnik metadanych opisujący dane zawarte w weather.txt

## Dane analizy

Folder zawiera plik z przetworzonymi danymi przygotowanymi do analizy (weather.csv) w formacie: 

indeks, id stacji, data (rrrr-mm-dd), TMAX, TMIN, PRCP

## Pliki poleceń

Folder zawiera:

- formatowanie.py - skrypt przetwarzający dane oryginalne do formy zgodnej z zasadami "tidy data", wygodnej do dalszej analizy. Kolejne operacje wykonywane na danych:
    
    1. Zapis danych do dataframe z pliku

    2. Usunięcie kolumn wyłącznie ze znakami podziału 'I' tzn. co drugiej kolumny z zakresu 2-55

    3. Usunięcie znaków podziału z błędnie dzielonych kolumn poprzez usunięcie pierwszego znaku i konwersję na typ int

    4. Nazwanie pozostałych kolumn id oraz kolejnymi numerami dni

    5. Podział kolumny id na id stacji, datę (rrrrmm) oraz nazwę zmiennej

    6. Usunięcie rozdzielonej kolumny
    
    7. Przeniesienie zmiennej dni do kolumny

    8. Połączenie kolumny daty z kolumną dni oraz sformatowanie w typie string do postaci możliwej do skonwertowania na typ datetime

    9. Usunięcie wyników pustych oraz tych z wartościami -9999 oznaczających brak wartości oraz zbędnej kolumny dni

    10. Konwersja daty na typ datetime

    11. Podział dataframe'u na mniejsze zawierające różne typy wartości dla tych samych dni oraz złożenie ponowne na podstawie wspólnych kolumn

    12. Sortowanie wg dat dla czytelności

    13. Ponowne przypisanie indeksów w kolejności rosnącej

## Dokumenty

Folder zawiera plik README.md opisujący projekt
