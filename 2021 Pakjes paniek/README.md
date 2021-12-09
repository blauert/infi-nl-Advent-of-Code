# Pakjes paniek

Santa wil zijn elfjes speelgoed laten maken, maar hij heeft zijn administratie nog niet op orde. Hij heeft een lijst van onderdelen die in elk soort speelgoed zitten. Het probleem is alleen dat sommige onderdelen weer uit verdere onderdelen bestaan, wat het tellen van het aantal onderdelen moeilijk maakt.

Stel bijvoorbeeld dat hij deze lijst zou krijgen (de missende onderdelen kan je voor nu negeren):
```
46 onderdelen missen
Zoink: 9 Oink, 5 Dink
Floep: 2 Flap, 4 Dink
Flap: 4 Oink, 3 Dink
```
In dit voorbeeld zijn Zoinks makkelijk: er zitten in totaal **14 (9+5)** onderdelen in. Een Floep is lastiger, omdat de Flappen die erin zitten elk ook uit meerdere onderdelen bestaan. Elke Flap bestaat uit **7** onderdelen. In een Floep zitten dus **18 (2*7+4)** onderdelen.

Gegeven de speelgoedlijst, **vind het stuk speelgoed met het grootste aantal onderdelen. Dit aantal is vervolgens het antwoord op deel 1**.

## Deel 2

Terwijl je bezig was met het tellen van de onderdelen, waren een paar ijverige elfjes al begonnen! Ze hebben speelgoed in elkaar gezet en ingepakt, maar zijn alweer vergeten wat erin zat. Gek genoeg weten ze nog wel hoeveel onderdelen ze hebben gebruikt.

De elfjes hebben alleen speelgoed ingepakt, en geen onderdelen zoals accu's of ijzer. Blijkbaar is er niemand stout geweest dit jaar.

In het eerdere voorbeeld waren er 46 missende onderdelen. Stel dat er 3 cadeaus al ingepakt waren. Zoinks en Floepen zijn hier de mogelijke stukken speelgoed, want ze worden niet als onderdelen gebruikt. Er is maar 1 manier om met alle missende onderdelen onderdelen precies 3 stukken speelgoed te maken: **2** Zoinks en **1** Floep **(14+14+18=46)**.

Als je de stukken speelgoed weet, kan je je antwoord vinden door de eerste letters van het speelgoed op alfabetische volgorde te zetten. In het bovenstaande voorbeeld zou dat dus `FZZ` worden.

Er zijn al 20 cadeaus ingepakt. Gegeven het aantal missende onderdelen in de speelgoedlijst, **wat zijn dan de beginletters (op alfabetische volgorde)?**