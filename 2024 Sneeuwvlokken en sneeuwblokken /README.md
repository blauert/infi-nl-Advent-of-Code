# Sneeuwvlokken en sneeuwblokken

Dikke, bolle wolken volgepakt met sneeuw hangen in de lucht boven de Noordpool. Erg gezellig, maar de wolken maken het moeilijk voor de Kerstman om zijn arreslee door de lucht te manoeuvreren. Het is niet de eerste keer dat het weer tegenzit en daarom hebben de elfjes een machine uitgevonden om de wolken in kaart te brengen!

De machine modelleert de lucht als een 3D-raster; het verdeelt het luchtruim in blokjes. Voor elk blokje lucht kan de machine met Kerstmagie meten hoeveel sneeuw er in dat blokje zit. Er is alleen een probleem: de machine werkt niet zoals verwacht. In plaats van sneeuw-data uit te printen, print het computerinstructies?!

Een van de elfjes zal per ongeluk een instelling hebben veranderd, maar geen van de elfjes weet welke... Ze hebben wel een handleiding van de machine met beschrijvingen voor de instructies. Er zit niets anders op dan zelf de instructies uitvoeren om zo de gegevens te verkrijgen.

De handleiding legt uit dat de instructies bedoeld zijn voor een **XM-4S virtual stack machine**. Om de hoeveelheid sneeuw in elk blokje te berekenen, moet de code voor elk blokje worden uitgevoerd. De XM-4S machine ondersteunt vier instructies: `push`, `add`, `ret` en `jmpos`. De `program counter` houd bij welke instructie wordt uitgevoerd. 0 is de eerste instructie uit het programma, 1 de tweede, etc.

- `push [value]` neemt `value` en zet het bovenop de stack. `value` is een getal of een van de symbolen `x`, `y`, `z`. De waardes van `x`, `y` en `z` verschillen per blokje en zijn de coördinaten van het blokje in het 3D-raster.
- `add` haalt twee getallen van de stack af, telt ze bij elkaar op en zet het resultaat bovenop de stack.
- `jmpos [offset]` neemt een getal van de stack af. Als het getal groter of gelijk is aan 0, wordt `offset` bij de huidige waarde van de `program counter` opgeteld.
- `ret` is de laatste instructie die wordt uitgevoerd. Het programma stopt en het getal wat op dat moment bovenop de stack staat is de waarde voor het blokje. 

Na elke instructie wordt de `program counter` verhoogd met 1. De dimensies van het 3D-raster dat de machine gebruikt zijn 30x30x30. De coördinaten van de blokjes in het raster beginnen bij 0.

Op de machine zit een post-it geplakt met wat lijkt op een calibratiecode en het woord \`sneeuwtotaal\`. Het vermoeden is dat we met deze code kunnen verifiëren of de machine correct werkt. De consensus onder de elfjes is dat de calibratiecode te berekenen is door de waardes in alle blokjes bij elkaar op te tellen.

In de handleiding staat een voorbeeld. In het voorbeeld staat voor elke instructie de index van de instructie, die door de `program counter` wordt gebruikt. In je input staat er geen index voor de instructies.

```
0: push 999
1: push x
2: push -3
3: add
4: jmpos 2
5: ret
6: ret
7: push 123
8: ret
```

Deze code wordt uitgevoerd voor een blokje met coördinaten (7, 0, 0). De stack begint leeg en de `program counter` begint op positie 0.

__`0: push 999`__

De waarde 999 wordt op de stack gezet.

De stack is nu [999].

De program counter wordt met 1 verhoogd en is nu 1.

__`1: push x`__

De waarde 7 wordt op de stack gezet.

De stack is nu [7, 999].

De program counter wordt met 1 verhoogd en is nu 2.

__`2: push -3`__

De waarde -3 wordt op de stack gezet.

De stack is nu [-3, 7, 999].

De program counter wordt met 1 verhoogd en is nu 3.

__`3: add`__

De twee bovenste waardes worden van de stack gehaald, bij elkaar opgeteld en op de stack gezet.

De stack is nu [4, 999].

De program counter wordt met 1 verhoogd en is nu 4.

__`4: jmpos 2`__

De bovenste waarde wordt van de stack gehaald; dit is 4 en dit is groter of gelijk aan 0, dus de program counter wordt verhoogd met 2 en is nu 6.

De program counter wordt met 1 verhoogd en is nu 7.

__`7: push 123`__

De waarde 123 wordt op de stack gezet.
De stack is nu [123, 999].

De program counter wordt met 1 verhoogd en is nu 8.

__`8: ret`__

Het programma stopt en geeft de waarde van het bovenste getal op de stack: 123. Als met deze code de waarde voor ieder blokje in het 30x30x30 raster berekend wordt, is de som van alle blokjes gelijk aan __5686200__

__Wat is de som van alle blokjes?__

## Deel 2

 Je hebt met succes de data ontcijferd! Nu de lucht succesvol in kaart is gebracht, willen de elfjes weten hoeveel wolken er op dit moment zijn. Bij te veel wolken is het namelijk niet veilig voor de Kerstman om te vliegen.

Voor elk blokje geld dat het een wolk is als die sneeuwdata groter is dan 0. Het kan ook zijn dat een wolkenblokje onderdeel is van een grotere wolk. Een grotere wolk is een verzameling van aaneengesloten blokjes. Twee blokjes worden gezien als aaneengesloten wanneer ze een zijde delen. Bijvoorbeeld, een blokje op positie (0, 0, 0) en een blokje op positie (1, 0, 0) worden gezien als aaneengesloten. Een blokje op positie (0, 0, 0) en een blokje op positie (1, 1, 0) zijn niet aaneengesloten. Deze blokjes delen wel een ribbe, maar niet een zijde.

Gebruik de sneeuwdata en tel het aantal wolken. __Hoeveel wolken zijn er?__