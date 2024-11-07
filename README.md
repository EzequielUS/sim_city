# 🏗️ Trabajo Práctico: Desarrollo de un Juego en Python basado en SimCity 🏙️

## Descripción General
El objetivo de este trabajo práctico es desarrollar un juego inspirado en **SimCity** utilizando **Python**. El juego se jugará en un tablero de **10x10** y la interfaz gráfica estará basada en la **terminal**. Se deberán usar **clases** para representar los diferentes elementos del juego e implementar un sistema de gestión de tiempo que simule el paso de los días y meses, afectando el estado del tablero y las finanzas del jugador.

---

## Especificaciones del Juego

### 🌍 Tablero e Interfaz
- **Dimensiones**: Tablero de 10x10.
- **Interfaz gráfica**: Consola/terminal.

### 🏞️ Elementos del Tablero
Cada posición del tablero puede representar uno de los siguientes tipos de terreno:
- 💧 Agua
- 🌱 Tierra
- 🛣️ Calle
- 🏠 Casa

### 🎲 Inicialización del Juego
- **Sorteo de posiciones**: Al iniciar, el tablero se debe llenar aleatoriamente con los distintos tipos de terreno, utilizando un porcentaje predeterminado de cada tipo.
- **Saldo inicial**: El jugador comenzará con un saldo de 💰 **1000 USD**.

### 🏗️ Reglas de Construcción y Transiciones

- **Migración de construcción**:
  - 🌱 Tierra → 🛣️ Calle → 🏠 Casa
  - Cada transición tiene un costo específico que debe ser pagado con el saldo del jugador.
  
- **Transición automática**:
  - Después de un período de tiempo, las calles se convertirán automáticamente en casas.

- **Condiciones de construcción de una casa**:
  - Para que una 🛣️ calle se convierta en 🏠 casa, debe estar rodeada de otras calles en sus lados laterales.

- **Impuestos y flujo de ingresos**:
  - Después de un mes de tiempo de juego, las casas comenzarán a pagar un impuesto al jugador, generando ingresos periódicos. 🏦

- **Demolición**:
  - El jugador puede demoler calles y casas por un costo de 💸 **10 USD**. Una vez demolido, el terreno vuelve a ser 🌱 tierra.

### ⛈️ Eventos del Juego
- **Gestión del tiempo**:
  - El juego no es por turnos, sino que un evento externo simula el paso del tiempo (por ejemplo, un temporizador). ⏳

- **Eventos climáticos**:
  - Deben implementarse eventos climáticos aleatorios que causen pérdidas monetarias, afectando el saldo del jugador. 🌪️💥

### 💵 Costos de Construcción
- Construir una casa: 🏠 **50 USD**.
- Demoler: 🛠️ **10 USD** (solo aplicable a calles y casas).

---

## 📐 Requisitos Técnicos

- **Diagrama de clases**:
  - Se debe diseñar un diagrama de clases que represente las entidades del juego y sus relaciones.

- **Programación orientada a objetos**:
  - El juego debe estar programado utilizando clases para organizar los distintos elementos y funcionalidades. 🧩

- **Interfaz gráfica en consola**:
  - La representación del tablero y las acciones del jugador se deben mostrar en la terminal. 💻

---

## 📜 Reglas de Juego y Condiciones

- **Saldo inicial**: El jugador comienza con una cantidad de dinero definida por el programador (ejemplo: **1M USD**). 💰🤑
- **Avance en el juego**: El actor principal que marca el avance en el juego es el tiempo. 🕰️
- **Visualización del tablero**: La capacidad de dibujar el tablero en la consola debe estar implementada para mostrar el estado actual del juego. 📊
