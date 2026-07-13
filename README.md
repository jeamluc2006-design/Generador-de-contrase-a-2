# 🔐 Generador Seguro de Contraseñas

## Autor

**Lucio Jeampierre Coello Vargas**

Carrera de Ciberseguridad  
Universidad Internacional del Ecuador (UIDE)

---

## Descripción

El Generador Seguro de Contraseñas es una aplicación desarrollada en Python que permite crear contraseñas aleatorias con distintos niveles de seguridad. El usuario puede seleccionar la longitud de la contraseña y el nivel de protección que desea obtener.

El objetivo del proyecto es ayudar a generar contraseñas más seguras para proteger cuentas e información personal, aplicando los conocimientos adquiridos en la asignatura de Lógica de Programación.

---

## Objetivo

Desarrollar una aplicación que permita generar contraseñas seguras mediante diferentes niveles de seguridad, utilizando estructuras lógicas, funciones y validaciones de datos en Python.

---

## Funcionalidades

- Validación de la longitud de la contraseña.
- Selección del nivel de seguridad.
- Generación automática de contraseñas aleatorias.
- Validación de las entradas del usuario.
- Opción para generar múltiples contraseñas durante una misma ejecución.

---

## Niveles de seguridad

### Nivel 1 - Bajo
Incluye:
- Letras minúsculas
- Números

### Nivel 2 - Medio
Incluye:
- Letras mayúsculas
- Letras minúsculas
- Números

Garantiza que exista al menos un carácter de cada tipo.

### Nivel 3 - Alto
Incluye:
- Letras mayúsculas
- Letras minúsculas
- Números
- Símbolos: @ # -

Garantiza que exista al menos:
- Una letra mayúscula.
- Una letra minúscula.
- Un número.
- Un símbolo.

---

## Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

Librerías utilizadas:

- random
- string

---

## Estructura del proyecto

```
Generador-Contraseñas/

│── Passgenerator.py
│── README.md
│
├── diagramas/
│   ├── Caso de uso.png
│   ├── Diagrama de flujo.png
│   └── Arquitectura.png
│
└── documentacion/
    └── Proyecto Integrador.pdf
```

---

## Cómo ejecutar el programa

1. Instalar Python 3.
2. Descargar o clonar el repositorio.
3. Abrir la carpeta del proyecto.
4. Ejecutar:

```bash
python main.py
```

5. Seguir las instrucciones mostradas en pantalla.

---

## Validaciones implementadas

El sistema verifica que:

- La longitud sea un número entero.
- La longitud esté entre 4 y 128 caracteres.
- El usuario seleccione un nivel válido.
- Se eviten entradas incorrectas durante la ejecución.

---

## Ejemplo de ejecución

```
========================================
 GENERADOR SEGURO DE CONTRASEÑAS
========================================

Ingrese la longitud de la contraseña (4 - 128): 12

Seleccione el nivel de seguridad

1. Baja
2. Media
3. Alta

Opción: 3

Nivel de seguridad: Alta

Contraseña generada:
A7@qLm9#Xp2D

¿Desea generar otra contraseña? (s/n):
```

---

## Diagramas incluidos

- Diagrama de Casos de Uso
- Diagrama de Flujo
- Diagrama de Arquitectura

---

## Competencias aplicadas

Durante el desarrollo del proyecto se aplicaron:

- Lógica de programación.
- Funciones.
- Estructuras condicionales.
- Estructuras repetitivas.
- Validación de datos.
- Programación modular.
- Organización del código.
- Control de versiones mediante GitHub.

---

## Posibles mejoras

- Interfaz gráfica.
- Copiar automáticamente la contraseña al portapapeles.
- Exportar contraseñas a un archivo.
- Historial de contraseñas generadas.
- Indicador visual de seguridad.

---

## Licencia

Proyecto desarrollado con fines académicos para la asignatura **Lógica de Programación** de la Universidad Internacional del Ecuador (UIDE).
