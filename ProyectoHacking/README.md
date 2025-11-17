# Damn Vulnerable RESTaurant API Game – Explotación y Defensa

Este repositorio contiene el análisis, explotación, pruebas, correcciones y documentación técnica del proyecto Damn Vulnerable RESTaurant API Game.

## 📌 Contenido del proyecto

### 1. Código original del juego
Incluye la estructura del proyecto DVRA tal como fue descargado.

### 2. Pruebas y scripts utilizados
- requests/ → Scripts en Python o archivos de Burp Suite utilizados para las pruebas.
- poc/ → Capturas y pruebas de concepto de cada vulnerabilidad.
- test/ → Pruebas automatizadas relacionadas a la vulnerabilidad adicional.

### 3. Parche o extensión del juego
Se incluye una vulnerabilidad nueva basada en:
- *Mass Assignment / Broken Object Property Level Authorization (BOPLA)*
- Endpoint afectado: PATCH /profiLE
- Archivos modificados:
  - app/apis/auth/services/patch_profile_service.py

### 4. Corrección aplicada
El parche consiste en:
- Reemplazar extra = Extra.allow
- Por extra = Extra.forbid
Evitando asignación masiva de propiedades no autorizadas.

### 5. Cómo ejecutar el proyecto

```bash
# Modo ofensivo
docker compose up

# Modo defensivo (juego)
./start_game.sh