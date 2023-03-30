
Monopolia pelataan käyttäen **kahta noppaa**. 

**Pelaajia** on vähintään 2 ja enintään 8. 

Peliä pelataan **pelilaudalla** joita on yksi. 

Pelilauta sisältää **40 ruutua**. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. 

Kullakin pelaajalla on yksi **pelinappula**. Pelinappula sijaitsee aina **yhdessä ruudussa**.

```mermaid
classDiagram
Pelaaja "2..8" -- "1" Pelilauta
Noppa "2" -- "1" Pelilauta
Ruutu "40" -- "1" Pelilauta
Pelaaja "1" -- "1" Pelinappula
Pelinappula "1" -- "1" Ruutu
Kortti "*" -- "1" Sattuma_Yhteismaa
Toiminto "1" -- "1" Kortti
Toiminto "1" -- "1" Ruutu
Ruutu <|-- Aloitusruutu
Ruutu <|-- Vankila
Ruutu <|-- Sattuma_Yhteismaa
Ruutu <|-- Asema_Laitos
Ruutu <|-- Katu 
Noppa .. Pelinappula
class Ruutu{
    int id
    int edellinenRuutu
    int seuraavaRuutu
}
class Pelilauta{
    int aloitusSijainti
    int vankilaSijainti
}
class Pelaaja{
    String nimi
    int rahamaara
}
class Katu{
    String nimi
    int ryhmaVari
    int taloLkm
    int hotelliLkm
    String omistaja
    bool kiinnitetty
}
class Asema_Laitos{
    String nimi
    String omistaja
}
class Toiminto{
    int id
    String kuvaus
}
class Kortti{
    int id
    bool nostopakassa
}
Noppa: int silmaluku
Pelinappula: String hahmo
Sattuma_Yhteismaa: String nimi
```

Ruutuja on useampaa eri tyyppiä:

- Aloitusruutu
- Vankila
- Sattuma ja yhteismaa
- Asemat ja laitokset
- Normaalit kadut (joihin liittyy nimi)

Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan **sijainti**.

Jokaiseen ruutuun liittyy **jokin toiminto**.

Sattuma- ja yhteismaaruutuihin liittyy **kortteja**, joihin kuhunkin liittyy joku **toiminto**.

Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.

Normaaleille kaduille voi rakentaa korkeintaan **4 taloa** tai **yhden hotellin**. Kadun voi **omistaa** joku pelaajista. Pelaajilla on **rahaa**.