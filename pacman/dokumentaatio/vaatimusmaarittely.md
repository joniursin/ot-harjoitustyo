# Vaatimusmäärittely

## Sovelluksen tarkoitus

- Sovelluksen tarkoituksena on luoda Pacman peli, joka toimii pääpiirteiltää samalla tavalla kuin alkuperäinen, mutta ei ole identtinen klooni.
- Pelissä pelaajan tulee vältellä vihollisia joihin osuessa menettää elämän pelaaja aloittaa kolmella elämällä.
- Kun kaikki elämät on menetetty peli loppuu.
- Pelaajan tarkoituksena on kerätä palloja joista saa pistetä.
- Pelaaja voi myös kerätä power upeja, joka mahdollistaa vihollisten syömisen hetkellisesti.
- Kun kaikki pallot sekä power upit on kerättä siirtyy peli seuraavalle tasolle, jolloin kaikesta saa enemmän pisteitä.
- Peli osaa pitää kirjaa siinä saavutetuista high scoreista ja tallentaa ne ylös tietokantaan pelin loppuessa.
- Pelin menusta kohdasta scoreboard voidaan katsoa tuloksia, jotka järjestetään tuloksen mukaan.

## Suunnitellut toiminnallisuudet

Pelin suunnitellut runko-ominaisuudet:
- Käynnistäessä sovellus luo pacman pelikentän ja sinne pelihahmon (tehty)
- Pelissä saadaan pisteitä samalla tavalla kuin alkupäräisessä pacmanissa ja se toimii pitkälti identtisesti. (tehty)
- Peliä voidaan pelata nii kauan kunnes pelaajalta loppuu kaikki elämät (tehty)
- Hävitessä pelaaja voi tallentaa tuloksensa nimellä sijoitus listaan (tehty)
- Aloitus ruudussa näytetään nämä tallennetut tuloksen parhausjärjestyksessä (tehty)
- Tuloksiin tallennetaan myös päivämäärä (tehty)

## Jatkokehitysideoita

Ideoita millä peliä voitaisiin laajentaa sen ollessa pelattava:
- Peli vaikeutuu ajankuluessa, kuten alkuperäisessäkin
- Pelikenttää voidaan kustomoida esimerkiksi eri väreillä/teemoilla
- Mahdollisesti pelaaja voisi luoda omia kenttiä/kenttiä voisi olla useampia ja jokaisella omat sijoitustalukot
- Sijoitustaulukkoa voidaan tarkastella, joko ajan tai sijoituksen mukaan
- Pelissä voisi olla useampia vaikeustasoja
