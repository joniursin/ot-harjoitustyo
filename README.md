# Pacman

Sovelluksen tarkoituksena on luoda Pacman peli, joka toimii pääpiirteiltää samalla tavalla kuin alkuperäinen. Pelissä pelaajan tulee vältellä vihollisia joihin osuessa menettää elämän. Kun kaikki elemät on menetetty peli loppuu. Peli osaa pitää kirjaa siinä saavutetuista high scoreista ja tallentaa ne ylös.

### Dokumentaatio

[vaatimusmaarittely.md](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/changelog.md)

### Asennus

1. Tarkista, että python versio on yli 3.8 komenolla:

python3 --version

2. Kloonaa repositorio komennolla:

git clone https://github.com/joniursin/ot-harjoitustyo

3. Asenna riippuvuudet komennolla:

poetry install

4. Käynnistä sovellus komenolla:

poetry run invoke start
