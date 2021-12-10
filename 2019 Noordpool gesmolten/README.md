# Noordpool gesmolten: Rendieren verkouden

Vanwege de klimaatverandering smelt het ijs op de noordpool erg hard en hebben alle rendieren natte voeten gekregen. Daardoor zijn ze verkouden geworden en moet de kerstman dit jaar zonder rendieren op pad. Dit jaar zal de kerstman daarom niet met zijn slee door de lucht vliegen om iedereen cadeautjes te bezorgen.

Een kerst zonder cadeautjes kan natuurlijk niet, daarom heeft de kerstman zich door zijn elven een paar springlaarzen aan laten meten waarmee hij van flatgebouw naar flatgebouw kan springen om zo snel door de stad te kunnen reizen en toch bij alle kinderen een cadeautje te bezorgen.

De kerstman moest wel even wennen aan zijn springlaarzen en heeft de afgelopen maanden geoefend. Daarbij ging het ook nog wel eens mis, waardoor de kerstman, nogal pijnlijk, op de grond belandde in plaats van op het volgende flatgebouw en kon hij opnieuw beginnen.

Ook de Noordpool doet aan big data en de elven hebben alle oefentochtjes van de kerstman gevolgd, gecodeerd en opgeslagen.

De bewegingen van de kerstman hebben de big data elven gecodeerd naar 'stappen':

-   Voor de eerste stap staat de kerstman op het dak van het eerste flatgebouw.
-   Elke stap beweegt hij 1 plaats naar rechts (+1 in de x positie).
-   Tijdens elke stap kan de kerstman 1 keer zijn springlaarzen gebruiken.
-   Met de springlaarzen kan de kerstman een extra verplaatsing doen in de positieve x en positieve y richting waarbij `0 =< x + y =< 4`.
-   Als de kerstman zich na de verplaatsing op of boven het dak van een flatgebouw bevindt dan landt hij veilig op dat dak. Zijn nieuwe y positie is dan de hoogte van het dak.
-   Als de kerstman zich na de verplaatsing niet op of boven het dak van een flatgebouw bevindt dan valt hij op de grond en is de tocht mislukt.
-   De kerstman kan voor een ander gebouw langs springen, mits deze sprong voldoet aan de verplaatsingsregels.
-   Een flatgebouw heeft altijd een breedte van 1.

### Voorbeeld

Gegeven de volgende input:
```
{

"flats": [[1,4],[3,8],[4,3],[5,7],[7,4],[10,3]],

"sprongen": [[2,0],[0,4],[1,0],[0,0]]

}
```
Wordt de puzzel op de volgende manier opgelost:

-   De kerstman begint op de eerste flat (positie x = 1, y = 4).
-   Tijdens de eerste stap maakt de kerstman een sprong van 2 posities naar rechts en 0 posities omhoog. De totale verplaatsing tijdens de eerste stap is dus 3 naar rechts en 0 omhoog.
-   De kerstman eindigt na deze stap op de derde flat (positie x = 4, y = 3). Tijdens zijn sprong is hij voor de tweede flat langs gesprongen en na zijn sprong is hij op het derde flatgebouw gevallen.
-   Tijdens de tweede stap maakt de kerstman een sprong van 0 posities naar rechts en 4 posities omhoog. De totale verplaatsing tijdens de tweede stap is dus 1 naar rechts en 4 omhoog.
-   De kerstman eindigt na deze stap op de vierde flat (positie x = 5, y = 7).
-   Tijdens de derde stap maakt de kerstman een sprong van 1 positie naar rechts en 0 omhoog. De totale verplaatsting is dus 2 posities naar rechts en 0 omhoog.
-   De kerstman komt na deze sprong uit boven de vijfde flat (positie x = 7, y = 7), maar zal door zwaartekracht vallen op het dak van de flat. Zijn eindpositie is dus de vijfde flat (positie x = 7, y = 4)
-   Tijdens de vierde stap gebruikt de kerstman zijn springlaarzen niet. Hij beweegt dus enkel 1 positie naar rechts.
-   De kerstman eindigt na deze stap op de grond en bereikt het zesde flatgebouw (positie x = 10, y = 3) niet.
-   Het antwoord op deze vraag "na hoeveel stappen valt de kerstman op de grond?" is met deze input dus 4.

**Na hoeveel stappen valt de kerstman op de grond?**. Het antwoord is het stapnummer van de stap waarbij de kerstman op de grond valt, of 0 als de kerstman het dak van het laatste flatgebouw bereikt.

## Deel 2

Het gebruik van de magische springlaarzen kost energie. Het is belangrijk de verbruikte energie tot een minimum te beperken, zodat de kerstman zelf niet ook nog eens bijdraagt aan de klimaatverandering.

De energie wordt bepaald door de x en y waarde van de extra kracht bij elkaar op te tellen. Wanneer de kerstman in de lucht boven een flatgebouw hangt in een stap en naar het dak zakt, dan kost dat geen energie.

Bepaal voor de flatgebouwen uit opdracht 1 welke combinatie van stappen het meest efficient is. Het antwoord is de totale hoeveelheid energie nodig om van het eerste naar het laatste flatgebouw te lopen. Omdat de kerstman stoute kinderen overslaat hoeft hij niet op het dak van elk flatgebouw te landen.

**Hoeveel energie kost het meest efficiente pad van het dak van het eerste flatgebouw naar het dak van het laatste flatgebouw?**