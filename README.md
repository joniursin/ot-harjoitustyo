# Pacman

Sovelluksen tarkoituksena on luoda Pacman peli, joka toimii pääpiirteiltää samalla tavalla kuin alkuperäinen. Pelissä pelaajan tulee vältellä vihollisia joihin osuessa menettää elämän. Kun kaikki elemät on menetetty peli loppuu. Peli osaa pitää kirjaa siinä saavutetuista high scoreista ja tallentaa ne ylös.

### Release

[Release 1](https://github.com/joniursin/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/joniursin/ot-harjoitustyo/releases/tag/viikko6)

### Dokumentaatio

[Käyttöohje](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

[Vaatimusmaarittely](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/arkkitehtuuri.md)

[Testaus](https://github.com/joniursin/ot-harjoitustyo/blob/main/pacman/dokumentaatio/testaus.md)

### Asennus

1. Tarkista, että python versio on yli 3.8 komenolla:

```bash
python3 --version
```

2. Kloonaa repositorio komennolla:

```bash
git clone https://github.com/joniursin/ot-harjoitustyo
```

3. Siirry kansioon pacman ja asenna riippuvuudet komennolla:

```bash
poetry install
```

4. Käynnistä sovellus komenolla:

```bash
poetry run invoke start
```

### Testaus

Pelkät testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylint tarkistukset voidaan suorittaa komenolla:

```bash
poetry run invoke lint
```
