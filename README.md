# Ohjelmistotekniikka, kevät 2023

## Harjoitustyö: FOG app

Perinteinen sääsovellus, jolla voit tarkistaa säätilan niin kotikaupungissasi kuin maapallon toisella puolen.

### Dokumentaatio

- [Työaikakirjanpito](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/stalola/ot-harjoitustyo/blob/main/fogapp/dokumentaatio/arkkitehtuuri.md)

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

## Käyttö

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
