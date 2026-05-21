# Warframe-Bot

> Bot en Python que consulta en tiempo real los eventos activos de Warframe sin necesidad de abrir el juego.

---

## ¿Por qué existe este bot?

Warframe es un juego con contenido rotativo que cambia constantemente: reliquias con tiempo de expiración, invasiones activas, misiones de alerta, ciclos de día/noche en zonas abiertas. Toda esa información requiere entrar al juego para consultarla, lo que no siempre es práctico.

Este bot nació de esa necesidad: poder preguntarle al bot qué está pasando en Warframe ahora mismo, sin tener que cargar el juego.

---

## ¿Qué hace?

- Consulta eventos activos en tiempo real (invasiones, alertas, misiones especiales)
- Muestra el contenido y las recompensas de cada reliquía disponible
- Indica el tiempo de expiración de cada evento o reliquía
- Responde a comandos directamente desde Telegram

---

## Stack tecnológico

| Componente | Tecnología |
|-----------|-----------|
| Lenguaje | Python |
| Fuente de datos | [Warframe Status API](https://api.warframestat.us) |
| Variables de entorno | dotenv |
| Plataforma | Telegram (bot) |

---

## Cómo funciona

El bot se conecta a la **Warframe Status API** — una API pública no oficial que expone el estado del juego en tiempo real. Ante cada comando del usuario, realiza una petición a la API, parsea la respuesta y formatea la información relevante en un mensaje de Discord.

```
Usuario en Telegram
      ↓ comando
  Warframe-Bot
      ↓ request
Warframe Status API (api.warframestat.us)
      ↓ JSON
  Warframe-Bot
      ↓ mensaje formateado
Usuario en Telegram
```

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TobyX73/Warframe-Bot.git
cd Warframe-Bot

# Instalar dependencias Python
cd "Proyecto Bot Warframe - py"
pip install -r requirements.txt

# Configurar variables de entorno
# Crear un archivo .env con:
TELEGRAM_TOKEN=tu_token_de_bot_aqui

# Ejecutar el bot
python main.py
```
---

## API utilizada

El bot consume la **[Warframe Status API](https://api.warframestat.us)**, una API REST pública que expone el estado del juego en JSON. No requiere autenticación.

Endpoints relevantes:
- `GET /pc` — estado general del juego en PC
- `GET /pc/invasions` — invasiones activas
- `GET /pc/alerts` — alertas activas
- `GET /pc/fissures` — fisuras y reliquias disponibles

---

## Estado del proyecto

El bot está funcional para consulta de eventos y reliquias. Posibles extensiones futuras:
- Notificaciones automáticas cuando aparezcan recompensas específicas
- Sistema de suscripción por tipo de evento
- Soporte para múltiples plataformas (PC, PS, Xbox, Switch)
