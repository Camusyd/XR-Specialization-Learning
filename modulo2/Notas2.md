# 🧠 Notas del Módulo 2 – Conceptos y Tecnologías XR

## 📘 Introducción
En este módulo, el enfoque se centra en **comprender la relación entre los conceptos XR** (que son estables y universales) y las **tecnologías XR** (que evolucionan rápidamente).  
Mientras los conceptos definen *cómo percibimos* la experiencia inmersiva, las tecnologías determinan *cómo la implementamos*.

---

## 🧩 1. Conceptos Fundamentales

### 🔹 Realidad Virtual (VR)
La **RV** sumerge completamente al usuario en un entorno digital generado por computadora.  
El mundo físico desaparece y se reemplaza por una simulación visual y auditiva.

**Conceptos clave:**
- Inmersión total.
- Interacción mediante controladores o sensores de movimiento.
- Entornos generados por motor gráfico (Unity, Unreal Engine).
- Ejemplo: *Meta Quest 3*, *HTC Vive XR Elite*.

---

### 🔹 Realidad Aumentada (AR)
La **RA** mezcla el mundo real con elementos digitales superpuestos.  
El usuario sigue viendo su entorno físico, pero con capas de información virtual.

**Conceptos clave:**
- Integración de lo real y lo virtual.
- Requiere cámara o visor transparente.
- Aplicaciones móviles o headsets (HoloLens, Magic Leap, ARKit, ARCore).
- Ejemplo: *Pokémon GO*, *IKEA Place*.

---

### 🔹 Realidad Mixta (MR)
La **RM** permite la interacción entre objetos reales y virtuales de manera coherente y en tiempo real.  
Es una evolución de la RA con mayor interactividad y percepción espacial.

**Conceptos clave:**
- Reconocimiento espacial avanzado (mapa del entorno 3D).  
- Interacción bidireccional (objeto físico afecta al virtual y viceversa).  
- Ejemplo: *Microsoft HoloLens 2*.

---

### 🔹 Realidad Extendida (XR)
XR es el **término paraguas** que abarca RA, RV y RM.  
Representa el espectro completo de experiencias inmersivas y su posición se visualiza en el **Continuo Realidad–Virtualidad (Milgram & Kishino, 1994)**.

---

## ⚙️ 2. Tecnologías XR Actuales

### 🎧 Tipos de Displays
| Tipo | Descripción | Ejemplos |
|------|--------------|-----------|
| **Head-Worn** | Gafas o visores montados en la cabeza | Meta Quest, HoloLens, Magic Leap |
| **Handheld** | Dispositivos portátiles como smartphones o tablets | ARCore, ARKit |
| **Monitor-Based** | Experiencias XR mostradas en pantallas tradicionales | WebXR, simuladores |
| **Projective / Spatial** | Proyección en superficies reales o entornos físicos | Reality Room, sistemas CAVE |
| **Room-Scale** | Sistemas inmersivos con sensores en la habitación | HTC Vive Pro, Valve Index |

---

### 🎯 Tipos de Seguimiento (Tracking)
| Tipo | Características | Uso común |
|------|------------------|------------|
| **Marker-Based** | Requiere imágenes o patrones de referencia (QR, fiduciales) | AR con objetos físicos |
| **Marker-Less** | Usa visión computacional y sensores espaciales | AR móvil, MR |
| **Inside-Out** | Cámaras en el dispositivo rastrean el entorno | Meta Quest, HoloLens |
| **Outside-In** | Sensores externos rastrean al usuario | HTC Vive |
| **3DoF (Degrees of Freedom)** | Rastrea rotación del dispositivo | Headsets básicos |
| **6DoF** | Rastrea rotación y posición | Sistemas inmersivos avanzados |

---

## 🧮 3. Criterios para Evaluar Tecnologías XR
- **Inmersión:** nivel de presencia sensorial y emocional.  
- **Accesibilidad:** facilidad de uso y disponibilidad del hardware.  
- **Costo:** económico y de implementación.  
- **Movilidad:** libertad de movimiento del usuario.  
- **Precisión del rastreo:** fidelidad del posicionamiento espacial.  
- **Colaboración:** soporte multiusuario local o remoto.  
- **Compatibilidad:** interoperabilidad con otras plataformas o motores gráficos.

---

## 🧠 4. Reflexiones Clave
- Los **conceptos XR son estables**, pero las **tecnologías cambian rápido**, por lo que un diseñador XR debe mantenerse actualizado.  
- La elección de tecnología depende del **escenario y objetivo de la experiencia**.  
- El análisis **QOC (Questions, Options, Criteria)** ayuda a tomar decisiones racionales y justificadas.  
- La **interoperabilidad** entre plataformas XR será clave en la próxima década.

---

## 🔍 5. Ejemplo: Aplicación del QOC en un Juego Colaborativo VR

**Pregunta:** ¿Cómo facilitar la colaboración entre jugadores en diferentes espacios físicos?  
**Opciones:**  
- Entorno VR totalmente virtual (alta inmersión).  
- Sistema XR híbrido (AR + VR).  
- Interfaz basada en escritorio con VR parcial.  

**Criterios:**  
- Comunicación fluida ✅  
- Sincronización estable ✅  
- Accesibilidad global ⚠️  
- Costo del hardware ⚠️  

**Resultado:** la opción **XR híbrida** ofrece el mejor equilibrio entre inmersión y accesibilidad.

---

## 🧾 Referencias
- Milgram, P., & Kishino, F. (1994). *A Taxonomy of Mixed Reality Visual Displays.* IEICE Transactions on Information Systems.  
- Nebeling, M. (2020). *Extended Reality for Everybody – University of Michigan / Coursera.*  
- MacLean, A., Young, R. M., Bellotti, V. M. E., & Moran, T. P. (1991). *Questions, Options, and Criteria: Elements of Design Space Analysis.*

---

📌 *Estas notas resumen los fundamentos conceptuales y tecnológicos que sirven de base para la selección estratégica de tecnologías XR en escenarios aplicados.*
