# FusionPDF2

FusionPDF2 es un programa que fusiona 2 o más archivos PDF en un solo archivo PDF sin importar cuántos o qué número de hojas contengan.

## Dónde se ejecuta:

Este programa requiere un intérprete de Python, ya sea local o remoto, y las siguientes bibliotecas adicionales:

- `tkinter`
- `PyPDF2`

Estas bibliotecas no forman parte de la biblioteca estándar de Python, por lo que deben instalarse con un gestor como pip. En intérpretes remotos (como Google Colab), las bibliotecas pueden venir preinstaladas o requerir configuración manual. Este programa puede ejecutarse en sistemas operativos compatibles con Python, como Windows, Linux, macOS, y Android (utilizando herramientas como Termux si no tienes un intérprete de Python).

Para instalar las bibliotecas necesarias con pip:

```bash
pip install PyPDF2
```

Para instalar PyPDF2 con conda:

```bash
conda install -c conda-forge pypdf2
```

La bibioteca `tkinter` suele venir por defecto instalada en Python. Sin embargo, si no la tienes, puedes instalarla manualmente:

#### Windows:

```bash
pip install tk
```

#### Linux:

En Linux, `tkinter` se puede instalar desde los repositorios del sistema:

```bash
sudo apt-get install python3-tk
```

#### macOS:

En macOS `tkinter` generalmente está incluido en la instalación de Python. Para instalarlo manualmente:

```bash
brew install python-tk
```

## Dónde no se ejecuta:

El programa no puede ejecutarse en sistemas sin soporte para Python, como dispositivos con sistemas operativos propietarios cerrados (por ejemplo, consolas de videojuegos) o sistemas empotrados sin un intérprete de Python. Para dispositivos móviles como Android, es necesario un entorno compatible con Python.

### Cómo usar:

Ejecuta el programa FusionPDF2.

Utiliza el botón "Agregar PDF" para seleccionar los archivos PDF que deseas fusionar.

Una vez seleccionados los archivos, haz clic en el botón "Fusionar PDFs".

Nombra tu nuevo PDF y selecciona la ubicación donde deseas guardar el archivo PDF fusionado.
