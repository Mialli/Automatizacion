## Trabajo Practico N°3: Ejercicio integrador QA Automation

#### Lirussi, Micaela

### Prerrequisitos:

Tener

- Python
- pip
- git
- Chrome

instalados.

### Instrucciones:

#### Paso 1

Descargar el repositorio

```
git clone https://github.com/Mialli/Automatizacion.git
```

Ingresar a la carpeta

```
cd Automatizacion
```

#### Paso 2

Instalar dependencias

```
pip install -r requirements.txt
```

#### Paso 3

En windows CMD

```
venv\Scripts\activate
```

En Linux/MacOS

```
source venv/bin/activate
```

---

### Ejecutar funciones y pruebas

#### Punto 1

```
python Punto1.py
```

#### Punto 2

```
python Punto2.py
```

#### Puntos 3 y 4

```
pytest ControlAutomatizacion.py
```

### Ver reporte HTML

**En GitHub:**

1.  Ir a la Action más reciente desde la [sección de Actions](https://github.com/Mialli/Automatizacion/actions).
2.  Scrollear a la sección de Artifacts y descargar `reporte-selenium`.
3.  Abrir el zip y abrir el archivo `reporte.html` en el navegador.
