Tarkastellaan bensatankista ja moottorista koostuvan koneen Python-koodia.

Piirrä sekvenssikaaviona tilanne, jossa kutsutaan (jostain koodin ulkopuolella olevasta metodista) ensin **Machine-luokan konstruktoria** ja sen jälkeen luodun **Machine-olion metodia drive**.

Muista, että sekvenssikaaviossa tulee tulla ilmi kaikki mainin suorituksen aikaansaamat olioiden luomiset ja metodien kutsut!

```mermaid
sequenceDiagram
    main->>kone: kone = Machine()
    kone->>bensatankki: FuelTank()
    kone->>bensatankki: fill(40)
    kone->>moottori: Engine(bensatankki)
    kone-->>main: 
    main->>kone: drive()
    kone->>moottori: start()
    moottori->>bensatankki: consume(5)
    kone->>moottori: is_running()
    moottori-->>kone: is_running = True
    kone->>moottori: use_energy()
    moottori->>bensatankki: consume(10)
    kone-->>main: 
```