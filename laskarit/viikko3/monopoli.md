
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
```
