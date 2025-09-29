# 🧩 Sudoku Validator (Python)

Este proyecto es un **validador de Sudokus** escrito en Python.  
Permite al usuario introducir un tablero de Sudoku y comprueba si cumple con las reglas básicas:

- Todos los valores deben estar en el rango `1–9`.
- No se permiten duplicados en filas, columnas ni bloques 3×3.
- El tablero completo debe ser válido para que la respuesta sea positiva.

---

## 🚀 Ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/sudoku-validator.git
   cd sudoku-validator

2. Ejecuta el script principal:
	python3 sudoku.py

3. Introduce tus valores fila a fila.	
   Ejemplo de entrada para la fila 1:
	Introduce 9 valores para la fila 1: 295743861

4. Al finalizar, se mostrará:
	- El tablero en formato 9x9.
	- El resultado de la validación: "Sí" si es correcto, "No" si hay algún error.

## 🖥️ Ejemplo de salida

---- S U D O K U ----

[2, 9, 5, 7, 4, 3, 8, 6, 1]
[4, 3, 1, 8, 6, 5, 9, 2, 7]
[8, 7, 6, 1, 9, 2, 5, 4, 3]
[3, 8, 7, 4, 5, 9, 2, 1, 6]
[6, 1, 2, 3, 8, 7, 4, 9, 5]
[5, 4, 9, 2, 1, 6, 7, 3, 8]
[7, 6, 3, 5, 2, 4, 1, 8, 9]
[9, 2, 8, 6, 7, 1, 3, 5, 4]
[1, 5, 4, 9, 3, 8, 6, 7, 2]

Sí

## 🛠️ Futuras mejoras

✅ Tests unitarios para garantizar que la función es_correcta() funciona en todos los casos.


⏳ Mejorar el sistema de entrada (ej. leer desde un archivo en lugar de introducir fila a fila).

⏳ Implementar un generador de sudokus válidos.

⏳ Interfaz gráfica sencilla con Tkinter o PyQt.

## 📚 Conocimientos puestos en práctica

Listas y slicing en Python.

Validación de entrada de usuario.

Manejo de estructuras de datos (filas, columnas, bloques).

Programación modular con funciones.

## 🤝 Contribuciones

Las contribuciones son bienvenidas.
Si quieres mejorar este validador, abre un issue o haz un pull request 🚀.

### 📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para aprender, practicar o extenderlo.