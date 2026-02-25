# ✈ SKY TRACER — Flight Track Monitor

> Aplicação web para rastreamento de voos em tempo real utilizando a API pública do [OpenSky Network](https://opensky-network.org/).

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Leaflet](https://img.shields.io/badge/Leaflet.js-199900?style=flat-square&logo=leaflet&logoColor=white)
![OpenSky](https://img.shields.io/badge/OpenSky%20Network-API-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## 📸 Preview

```
┌────────────────────────────────────────────────────────────────┐
│  ✈ SKY TRACER                             ● RASTREANDO  UTC   │
├──────────────────┬─────────────────────────────────────────────┤
│  IDENTIFICAÇÃO   │                                             │
│  ICAO24: [____]  │           🗺  MAPA INTERATIVO               │
│  [▶ RASTREAR]   │                                              │
│                  │     ─────────────────────────────           │
│  DADOS DO VOO    │    /   RASTRO DO VOO (linha azul)           │
│  Callsign: XXX   │                              ✈ (posição)   │
│  Alt: 10500 m    │                                             │
│  Vel: 480 kt     │                                             │
│  Rumo: 270°      │                                             │
└──────────────────┴─────────────────────────────────────────────┘
```

---

## 🚀 Funcionalidades

- **Campo de busca por ICAO24** — identifique qualquer aeronave pelo seu código hexadecimal único
- **Mapa interativo com Leaflet.js** — rastro completo do voo desenhado em tempo real
- **Ícone de avião animado** — posicionado na última localização registrada, com rotação baseada no rumo
- **Painel de dados do voo** — callsign, altitude, velocidade, rumo, lat/lon e status de solo
- **Histórico de waypoints** — tabela com todos os pontos registrados no trajeto
- **Atualização automática a cada 15 segundos**
- **Visual estilo cockpit** — tema escuro com fontes monoespaçadas e efeitos de scanline

---

## 🛠 Tecnologias

| Tecnologia | Uso |
|---|---|
| HTML5 / CSS3 / JavaScript | Estrutura, estilo e lógica da aplicação |
| [Leaflet.js 1.9.4](https://leafletjs.com/) | Renderização do mapa interativo |
| [OpenStreetMap](https://www.openstreetmap.org/) | Tiles do mapa base |
| [OpenSky Network REST API](https://openskynetwork.github.io/opensky-api/) | Dados de voos em tempo real |
| [Google Fonts — Orbitron + Share Tech Mono](https://fonts.google.com/) | Tipografia temática |

---

## 📦 Instalação e Uso

Este projeto é uma aplicação **frontend pura** — sem dependências, sem build, sem servidor.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sky-tracer.git
cd sky-tracer
```

### 2. Abra no navegador

```bash
# Opção A: Abrir diretamente
open flight-tracker.html

# Opção B: Servir localmente (recomendado para evitar restrições de CORS)
npx serve .
# ou
python3 -m http.server 8080
```

### 3. Rastreie um voo

1. Acesse a aplicação no navegador
2. Insira um código **ICAO24** no campo de busca (ex: `3C4B26`)
3. Clique em **▶ RASTREAR**
4. O mapa exibirá o rastro do voo com atualização automática

---

## 🔑 Autenticação na API do OpenSky

A API do OpenSky Network possui dois modos de acesso:

| Tipo | Limite de requisições | Histórico de track |
|---|---|---|
| **Anônimo** | ~10 req/min | Limitado |
| **Autenticado (conta gratuita)** | ~100 req/min | Completo |

Para obter acesso completo, crie uma conta gratuita em [opensky-network.org](https://opensky-network.org/index.php?option=com_users&view=registration) e adicione autenticação Basic nas requisições:

```javascript
// Exemplo de autenticação Basic (modifique fetchTrack em flight-tracker.html)
const resp = await fetch(url, {
  headers: {
    'Authorization': 'Basic ' + btoa('seu_usuario:sua_senha')
  }
});
```

> ⚠️ **Nunca commite credenciais diretamente no código.** Use variáveis de ambiente ou um backend proxy para produção.

---

## 🔍 Como encontrar um código ICAO24

O código ICAO24 é um identificador hexadecimal de 6 dígitos único para cada aeronave. Você pode encontrá-lo em:

- [FlightRadar24](https://www.flightradar24.com/) — clique em um avião e veja "Mode S"
- [FlightAware](https://www.flightaware.com/)
- [OpenSky Explorer](https://opensky-network.org/network/explorer)
- [ADSBExchange](https://globe.adsbexchange.com/)

**Exemplos de códigos para teste:**

| Código | Companhia (aproximado) |
|---|---|
| `3C4B26` | Lufthansa (Alemanha) |
| `A0F123` | American Airlines (EUA) |
| `E49F0E` | LATAM (Brasil) |
| `894418` | ANA (Japão) |

---

## 📡 Endpoint da API utilizado

```
GET https://opensky-network.org/api/tracks/all?icao24={icao24}&time=0
```

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `icao24` | string | Endereço ICAO24 da aeronave (hexadecimal) |
| `time` | int | Timestamp Unix. `0` = voo atual em tempo real |

**Exemplo de resposta:**

```json
{
  "icao24": "3c4b26",
  "callsign": "DLH441 ",
  "startTime": 1700000000,
  "endTime": 1700003600,
  "path": [
    [1700000000, 48.1351, 11.5820, 295.0, 1200.0, false],
    [1700001800, 49.4521, 8.4521, 290.0, 10500.0, false]
  ]
}
```

**Estrutura de cada waypoint `path[i]`:**

| Índice | Campo | Descrição |
|---|---|---|
| `[0]` | `time` | Timestamp Unix |
| `[1]` | `latitude` | Latitude em graus decimais |
| `[2]` | `longitude` | Longitude em graus decimais |
| `[3]` | `true_track` | Rumo verdadeiro em graus (0-360) |
| `[4]` | `baro_altitude` | Altitude barométrica em metros |
| `[5]` | `on_ground` | `true` se a aeronave está em solo |

---

## 🗂 Estrutura do Projeto

```
sky-tracer/
│
├── flight-tracker.html   # Aplicação completa (single-file)
├── README.md             # Documentação
└── LICENSE               # Licença MIT
```

---

## 🌐 Deploy

Por ser um arquivo HTML único sem dependências externas além de CDNs, o projeto pode ser publicado facilmente em:

- **GitHub Pages** — vá em *Settings > Pages* e selecione a branch `main`
- **Netlify** — arraste o arquivo para [app.netlify.com/drop](https://app.netlify.com/drop)
- **Vercel** — `vercel --prod`

---

## ⚠️ Limitações Conhecidas

- A API do OpenSky pode retornar `404` para aeronaves sem voo ativo recente.
- Voos muito antigos (>1h encerrado) podem não estar disponíveis no endpoint de tracks sem conta premium.
- O campo `true_track` pode ser `null` em alguns waypoints; nesses casos, o ícone do avião usa o valor anterior.
- A atualização automática pode ser bloqueada por CORS em alguns navegadores ao abrir o arquivo diretamente (`file://`). Use um servidor local para evitar isso.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'feat: adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- [OpenSky Network](https://opensky-network.org/) pela API pública de dados aeronáuticos
- [Leaflet.js](https://leafletjs.com/) pela biblioteca de mapas open source
- [OpenStreetMap](https://www.openstreetmap.org/) pelos dados cartográficos

---

<div align="center">
  Feito com ☕ e JavaScript puro
</div>


