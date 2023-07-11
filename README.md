# Maszyna-Turinga-Wyszukiwanie-Tekstu-Turing-Machine-Text-Search
Ten projekt zawiera prostą implementację Maszyny Turinga, napisaną obiektowo, do wyszukiwania tekstu. Maszyna Turinga to teoretyczny model obliczeniowy, który może symulować dowolny proces algorytmiczny poprzez manipulację symbolami na nieskończonej taśmie, zgodnie z góry zdefiniowanymi regułami.

Klasa **TuringMachine** w tym kodzie reprezentuje uproszczoną wersję Maszyny Turinga, która wykonuje operacje wyszukiwania tekstu. Odczytuje zestaw stanów i przejść z pliku stanów oraz operuje na taśmie, która reprezentuje wprowadzony tekst. Taśma jest modyfikowana na podstawie bieżącego stanu i reguł przejść zdefiniowanych w pliku stanów.

**Działanie:**

**Program odczytuje stany z pliki "states.txt"**. 
Stan jest reprezentowany jako:
**"nazwa_stanu: [('symbol/e_wejściowy/e', 'nowy_symbol', 'ruch_głowicy', 'następny_stan'), ...]"**.

Przykład: **del:[[['0','1'],' ',"R", 'start']].** 
Jeśli głowica natrafi na "0" lub "1" to zmienia znak na taśmie na puste pole " ", przesuwa głowicę w prawo (czyli +1 do idexu taśmy), następnie przechodzi do stanu "start".

**Program odczytuje taśmę z pliku "tape.txt".**
W tym przypadku tekst jest reprezentowany binarnie. 
Na przykład słowo _"ala ma kota"_ wpowadzamy jako "01100001 01101100 01100001 00100000 01101101 01100001 00100000 01101011 01101111 01110100 01100001 00100000". Po znaku "#" wprawadzany szukane słowo, np. "_kota_" - "01101011 01101111 01110100 01100001", co w tym przypadku zwróci "acc", czyli accept/true. **W pliku tape.txt należy zapisać tekst binarny _BEZ_ spacji.**

**Diagram**

![zdj1](https://github.com/maxyymmm/Maszyna-Turinga-Wyszukiwanie-Tekstu-Turing-Machine-Text-Search/assets/120425774/f4bc31c4-5a91-48e9-bccd-0fff4afdac05)
![zdj2](https://github.com/maxyymmm/Maszyna-Turinga-Wyszukiwanie-Tekstu-Turing-Machine-Text-Search/assets/120425774/684aaa1b-4aa8-4fc1-8bc8-6eba9f6c6e06)

**Acc/Accept/True**

![acc](https://github.com/maxyymmm/Maszyna-Turinga-Wyszukiwanie-Tekstu-Turing-Machine-Text-Search/assets/120425774/e401fbbc-e1ca-474d-bba9-db8516e61112)

**False**

![false](https://github.com/maxyymmm/Maszyna-Turinga-Wyszukiwanie-Tekstu-Turing-Machine-Text-Search/assets/120425774/c7a010bb-bb8e-453e-9c8d-a4a8cad770ba)





