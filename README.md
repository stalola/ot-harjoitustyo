# Ohjelmistotekniikka, kevät 2023

## Harjoitustyö: FOG app

Perinteinen sääsovellus, jolla voit tarkistaa säätilan niin kotikaupungissasi kuin maapallon toisella puolen.

### Dokumentaatio

- [Työaikakirjanpito](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/arkkitehtuuri.md)
- [Viikon 5 release](https://github.com/stalola/ot-harjoitustyo/releases/tag/viikko5)

## Asennus:

1. Siirry hakemistoon _fogapp_ ja asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Käynnistä virtuaaliympäristö:

```bash
poetry shell
```
3. Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```
4. Luo tunnus [OpenWeather-palveluun](https://home.openweathermap.org/users/sign_up) ja hanki itsellesi oma [API-avain](https://home.openweathermap.org/api_keys). *Jos olet ohte-kurssin arvioija etkä halua rekisteröityä palveluun, lähetä viesti niin annan avaimen!*

## Käyttö

### API avaimen lisääminen:

Sovellus ei toimi ennen kuin olet lisännyt API-avaimen. *Jos olet ohte-kurssin arvioija etkä halua rekisteröityä palveluun, lähetä viesti niin annan avaimen!*

Uuden API-avaimen lisäys komennolla:

```bash
poetry run invoke apikey
```

### Sovelluksen käynnistys:

Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

### Testien ajaminen

Sovelluksen testit käynnistyvät komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti muodostuu komennolla:

```bash
poetry run invoke coverage-report
```

Valmis raportti löytyy tiedostosta _index.html_, hakemistosta _htmlcov_.

### Pylint

Tiedoston [.pylintrc](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
