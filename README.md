# Elektroniczny System Kwaterowania Studentów

Projekt w ramach przedmiotu Podstawy Informatyki i Programowania 2023Z

## Spis Treści

- [Elektroniczny System Kwaterowania Studentów](#elektroniczny-system-kwaterowania-studentów)
  - [Wprowadzenie](#wprowadzenie)
  - [Struktura Projektu](#struktura-projektu)
    - [Moduły](#moduły)
    - [Pozostałe pliki](#pozostałe-pliki)
  - [Jak Uruchomić Projekt](#jak-uruchomić-projekt)
  - [Dane Wejściowe](#dane-wejściowe)
  - [Struktura Danych](#struktura-danych)
    - [Student](#student)
    - [Akademik](#akademik)
    - [Pokój](#pokój)
    - [Segment](#segment)
    - [Typ Segmentu](#typ-segmentu)
  - [Proces Akcji Kwaterunkowej](#proces-akcji-kwaterunkowej)
  - [Przyszły rozwój](#przyszły-rozwój)

## Wprowadzenie

Elektroniczny System Kwaterowania Studentów został stworzony w celu ułatwienia procesu zakwaterowania studentów na Politechnice Warszawskim i lepsze dopasowanie przyszłych współlokatorów do siebie. Obejmuje funkcje importowania danych o akademikach i studentach, wyświetlania informacji o akademikach, studentach oraz zarządzania procesem zakwaterowania.

## Struktura Projektu

Projekt podzielony jest na kilka modułów i plików, z których każdy odpowiada za określone zadania. Poniżej przedstawiamy krótki opis każdego z nich:

### Moduły:
1. **student.py:** Zawiera definicję klasy `Student`, reprezentującej studenta w systemie.
2. **dormitory.py:** Odpowiada za definicję klasy `Dormitory`, która reprezentuje akademik w systemie.
3. **room.py:** Odpowiada za definicję klasy `Room`, która reprezentuje pokój w systemie.
4. **segment.py:** Odpowiada za definicję klasy `Segment`, która reprezentuje segment w systemie.
5. **segmentType.py:** Zawiera definicję klasy `SegmentType`, reprezentującej typ segmentu w akademiku.
6. **funcStudents.py:** Zawiera funkcje związane z przetwarzaniem i manipulacją listy studentów.
7. **funcDorms.py:** Odpowiada za funkcje związane z akademikami, takie jak pobieranie konkretnych segmentów i znajdowanie typów segmentów.
8. **exceptions:** Katalog zawierający moduły definiujące niestandardowe klasy wyjątków używane w projekcie.
    - **student.py:** Zawiera klasy wyjątków związanych z klasą `Student`.
    - **dormitory.py:** Zawiera klasy wyjątków związanych z klasą `Dormitory`.
    - **room.py:** Zawiera klasy wyjątków związanych z klasą `Room`.
    - **segment.py:** Zawiera klasy wyjątków związanych z klasą `Segment`.
    - **segmentType.py:** Zawiera klasy wyjątków związanych z klasą `SegmentType`.
    - **rest.py:** Zawiera pozostałe klasy wyjątków.
9. **importFile.py:** Zawiera funkcje służące do importu danych z plików zewnętrznych.
10. **inputOutput.py:** Odpowiada za funkcje związane z interakcją z użytkownikiem, takie jak edycja danych, wyświetlanie informacji o akademikach itp.
11. **accommodationAction.py:** Zawiera funkcje związane z procesem akcji kwaterunkowej, czyli przydzielaniem studentów do segmentów akademików.
12. **graphs.py:** Zawiera funkcje związane z operacjami na grafach, wykorzystywane dla studentów, którzy wskazali w systemie, że chcą mieszkać z konkrentym innym studentem.

### Pozostałe pliki:
1. **main.py:** Plik, którego celem jest tylko uruchomienie funkcji `esks()`
2. **esks.py:** Główny plik aplikacji, zawiera funkcję `esks`, która obsługuje interfejs użytkownika.
3. **dorms.json:** Plik JSON zawierający dane o akademikach.
4. **raport.txt:** Plik tekstowy, w którym zapisywane są informacje o studentach.
5. **README.md:** Plik z dokumentacją
6. **generatory:** Katalog zawierający pliki służące do generowania danych wejściowych
    - **siri wygeneruj mi studentów.py:** Plik generujący losowe dane wejściowe ze studentami biorącymi udział w danej akcji kwaterunkowej w formacie txt
    - **siri wygeneruj mi akademiki.py:** Plik generujący plik `dorms.json` będący danymi wejściowymi z informacjami o akademikach
7. **pytest files:** Katalog zawierający z plikami z testami jednostkowymi za pomocą `pytest`
    - **test_student.py:** Zawiera testy dla klasy `Student`.
    - **test_dormitory.py:** Zawiera testy dla klasy `Dormitory`.
    - **test_room.py:** Zawiera testy dla klasy `Room`.
    - **test_segment.py:** Zawiera testy dla klasy `Segment`.
    - **test_segmentType.py:** Zawiera testy dla klasy `SegmentType`.
    - **test_funcStudents.py:** Zawiera testy dla modułu `funcStudents`
    - **test_funcDorms.py:** Zawiera testy dla modułu `funcDorms`
    - **test_graphs.py:** Zawiera testy dla modułu `graphs`

## Jak Uruchomić Projekt

1. **Uruchomienie Aplikacji:** Uruchom plik `main.py` w terminalu lub IDE, aby uruchomić aplikację.
2. **Interakcja z Aplikacją:** Aplikacja poprosi Cię o podjęcie różnych działań, takich jak edycja danych, wyświetlanie informacji o akademikach, składanie wniosków itp.

```bash
python3 main.py
```

## Dane Wejściowe

- **dorms.json:** Plik JSON zawierający dane o akademikach. Struktura pliku musi być zgodna z oczekiwanym formatem.
- **students.txt:** Plik txt zawierający dane o studentach. Struktura pliku musi być zgodna z oczekiwanym formatem.

## Struktura Danych

### Student
Klasa `Student` przechowuje informacje o pojedynczym studencie, takie jak numer identyfikacyjny, rok urodzenia, płeć, wydział, kierunek studiów, preferencje dotyczące zakwaterowania itp.

### Akademik
Klasa `Dormitory` reprezentuje pojedynczy akademik. Zawiera informacje o dostępnych pokojach, segmentach i innych istotnych szczegółach.

### Pokój
Klasa `Room` reprezentuje pojedynczy pokój. Zawiera informacje o dostępnych segmentach, wielkości oraz wyposażeniu pokoju.

### Segment
Klasa `Segment` reprezentuje pojedynczy segment. Zawiera informacje o dostępnych ilości łóżek oraz mieszkańcach.

### Typ Segmentu
Klasa `SegmentType` definiuje różne typy segmentów w akademiku, takie jak lokalizacja, liczba lokatorów itp.

## Proces Akcji Kwaterunkowej

1. Import danych o akademikach i studentach z odpowiednich plików.
2. Studenci, którzy wskazali, że chcą mieszkać razem są grupowani i przydzielany jest im segment najbardziej zbliżony im wspólnej preferencji
3. Studenci dzieleni są na grupy studentów, którzy będą mieszkać w segmentach o tym samym typie w poniższej kolejności:
   - studenci, którzy dokładnie wskazali, gdzie chcą mieszkać
   - studenci, którzy wskazali typ segmentu, który faktycznie istnieje
   - studenci, którzy wskazali nieistniejący typ segmentu, ale taki, dla którego istnieje inny zdecydowanie lepszy
   - pozostali studenci do najbardziej zbliżonego typu segmentu do tego, który wskazali
4. Studenci w danych grupach są dobierani w pary, trójki, czwórki itd w taki sposób, żeby jak najbardziej do siebie pasowali jako przyszli współlokatorzy

## Przyszyły rozwój

Niestety w wielu miejscach w kodzie wpisane są sztywne wartości dotyczące informacji o akademikach lub studiach na PW. Należałoby to zamienić na importowany plik np w formacie JSON
