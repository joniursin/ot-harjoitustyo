# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi README.md tiedostosta.

## Käynnistäminen

Asenna aluksii rippuvuudet hakemistossa pacman komennolla:

```bash
poetry install
```

Jonka jälkeen voit käynnistä sovelluksen komenolla:

```bash
poetry run invoke start
```

## Käyttö

Sovellus käynnistyy menuun, josta painamalle "Play" luo sovellus uuden pelin. Voit syöttää kohtaan username peli nimesi.
![image](https://github.com/joniursin/ot-harjoitustyo/assets/128263908/c1b813d4-e8ca-4e07-b2ee-522c5bc11422)


## Pelaaminen

Pelissä on tarkoitus kerätä keltaisia palloja ja samalla väistellä kummituksia. Kummituksia voidaan kuitenkin syödä hetkellisesti keräämällä valkoinen power up.

![image](https://user-images.githubusercontent.com/128263908/235780552-7bf8c352-3b1e-48c9-b00d-3f9b77cd3575.png)

## Tuloksen tallennus

Kun peli loppuu pelaaja tallentaa tuloksensa tietokantaan painamalla näppäintä "e", tuloksia voidaan katsoa menun kohdasta "Scoreboard".

## Lopetus

Sovellus voidaan lopettaa painamalla "Quit" nappia.

