# Een veelzijdige oplossing

In 2023 is het beeld van de Kerstman die in een kleine slee stapt om cadeautjes te bezorgen een beetje achterhaald. De slee lijkt inmiddels meer op een Boeing 737. Er wordt door de elven dag en nacht hard doorgewerkt om deze te beladen. Misschien wel te hard, want er sneuvelen altijd veel cadeautjes bij het inladen. Gelukkig heeft de Kerstman een idee om beteuterde kinderen te voorkomen: Hij wil de cadeautjes inpakken in ballonnen, zodat ze beschermd worden door een laagje lucht. Hij heeft jou de taak gegeven om uit te zoeken hoe vol de ballonnen precies moeten zijn om de pakjes goed te beschermen.

Je zit in een slecht verlicht kamertje aan een gammel bureau. Je wacht al een tijdje op de hoofdelf, met wie je een afspraak hebt, zodat ze je kan vertellen hoe het inpakken en inladen in zijn werk gaat. Of nou ja, je hád een afpraak met haar, want inmiddels is ze al meer dan 10 minuten te laat. Je vraagt je net af of ze nog op zal komen dagen, als de deur openknalt en er op hoog tempo een elf binnenloopt en een stapel papier op de tafel neergooit. "Hé... sorry, noodgeval... inpakmachine in hal 15 kapot..." hijgt de elf, terwijl ze je met een bezweet gezicht aankijkt. Je geeft haar een paar tellen om op adem te komen en probeert meelevend te zijn. "Vervelend! Maar gelukkig dat je er bent! Wat zijn di-". Je krijgt de kans niet om je vraag af te maken. "Sorry, ik moet er weer vandoor" zegt de elf terwijl ze de deur alweer uit loopt.

Je zucht en vraagt je af of dit nou inderdaad de hoofdelf was.

### Instructies
Je kijkt eens naar de stapel papier op het bureau voor je. Op elk vel lijkt een veelhoek te staan. Je kijkt eens wat beter naar het bovenste vel papier. Er staat een serie coördinaten:
```
(0, 4), (3, -2), (-1, -2), (-2, 0)
```
Daaronder staat een diagram:

```
         (0,4)
           o
          / \
         /   \
        /     \
(-2,0) o   +   \
        \       \
         o———————o
      (-1,-2)  (3,-2)
```

Je weet van eerdere jaren dat de pakjes in de slee twee-dimensionaal zijn, en herkent dit diagram gelijk als de omtrek van een pakje. De coördinaten zijn dus de hoekpunten van een pakje. In het midden, op de coördinaten (0, 0) staat een kruisje. Je gaat ervan uit dat het middelpunt van de ballon hier aan het cadeau wordt vastgemaakt.

Als we een cirkel met straal 4 tekenen om het middelpunt, zien we dat alle hoekpunten zich in of op de cirkel bevinden. Het punt op (0, 4) bevindt zich op de rand van de cirkel. Dat betekent dat als we de cirkel kleiner zouden maken, dit punt buiten de cirkel zou vallen. In dit geval heeft de kleinste ballon die alle punten bevat dus straal 4.

Je input bestaat uit een aantal regels. Elke regel beschrijft een pakje. Een regel bevat de coördinaten (x, y) van de hoekpunten van het pakje. De coördinaten zijn gescheiden door komma's. Voor elk pakje moet je de radius van de kleinste ballon berekenen, zodat elk hoekpunt in de ballon past wanneer de ballon het middelpunt op het kruisje op (0, 0) heeft.

Voor elk pakje in de lijst, **vind de straal van de kleinste ballon met middelpunt (0, 0) zodat het pakje geheel in de ballon past. Je antwoord op deel 1 is de som van deze getallen, afgerond naar beneden naar een geheel getal.**

## Deel 2
Zo, opgelost! Dat was sneller dan verwacht, de Kerstman heeft je verteld dat hij dacht dat je er wel een dagje zoet mee zou zijn. Je hebt de elven bij de inpakmachine zelf maar uitgelegd wat de bedoeling is, en besluit de rest van de dag maar wat te spelen op je telefoon. Je spelletje Candy Crush wordt bruut verstoord als de deur voor de tweede keer vandaag openzwaait. De elf waarvan je vermoedt dat het de hoofdelf is blijft deze keer in de deuropening staan. Ze kijkt niet blij.

"Waar ben jij mee bezig?" zegt de elf. Je was net met level 47 begonnen, maar houdt dat maar even voor je. "Deze ballonnen zijn veel te ver opgeblazen". De elf laat eindelijk een stilte vallen, waarin je een weerwoord zou kunnen geven, als je dat gehad zou hebben. De elf vindt je blijkbaar een beetje zielig, of misschien beseft ze dat ze wel erg aanvallend doet, want ze slaat een iets mildere toon aan. "Nou, kijk er nog eens naar." zegt ze terwijl ze een stapel papier op tafel legt. "Ik hoop dat je een betere oplossing kan vinden." zegt ze voordat ze wegloopt.

Je zucht en laat wat er zojuist gebeurde even op je inwerken. Je stopt je telefoon in je zak en kijkt met tegenzin naar de stapel.

### Instructies
Je herkent het bovenste velletje en concludeert dat dit hetzelfde diagram als eerder is.

```
         (0,4)
           o
          / \
         /   \
        /     \
(-2,0) o       \
        \       \
         o———————o
      (-1,-2)  (3,-2)
```

Over dit diagram heen is met pen een cirkel getekend, waarvan het middelpunt niet op het kruisje ligt. Bij het middelpunt van de cirkel staan de coördinaten (1, 0.75), en de straal √11.5625 = 3.400367... staat genoteerd.

Je aanname dat de ballon middelpunt (0, 0) moet hebben was dus onjuist. De ballon kan elk middelpunt hebben. Dit maakt het een stuk moeilijker om de kleinste ballon waarin alle punten passen te vinden. Voor het eerste voorbeeld is de straal van de kleinste ballon dus √11.5625 = 3.400367...

Op het volgende vel papier staan de volgende coördinaten:
```
(-1, 0), (1, 4), (1, -4)
```
Het diagram van dit pakje ziet er als volgt uit:

```
           (1,4)
            o
           /|
          / |
         /  |
(-1, 0) o   |
         \  |
          \ |
           \|
            o
         (1,-4)
```

In dit geval blijkt de kleinste cirkel die alle hoekpunten bevat middelpunt (1, 0) en straal 4 te hebben. De punten (1, 4) en (1, -4) liggen op de rand van de cirkel en het punt (-1, 0) ligt binnen de cirkel.

Voor elk pakje in de lijst: **vind de straal van de kleinste ballon zodat het pakje geheel in de ballon past. Deze keer moet je het middelpunt van de ballon zo kiezen dat de straal minimaal is. Neem de som van de stralen van de ballonnen en rond naar beneden af naar een geheel getal. Dit getal is je antwoord op deel 2.**