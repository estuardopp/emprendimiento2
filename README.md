# SAVIA · Prototipo en Streamlit

Aplicación demostrativa basada en la presentación de avances y el Business Model Canvas de SAVIA.

## Ejecutar en tu computadora

1. Instala Python 3.10 o posterior.
2. Abre una terminal en esta carpeta y ejecuta:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit mostrará la dirección local de la aplicación. Para compartirla mediante Streamlit Community Cloud, sube `app.py` y `requirements.txt` a un repositorio de GitHub y selecciona `app.py` como archivo principal.

## Qué se puede demostrar

- Inicio con métricas y búsqueda.
- Explorar tres fichas botánicas, fuentes externas, precauciones y biblioteca personal.
- Plan con objetivo editable y seguimiento de hábitos del día.
- Marketplace con precios en quetzales, carrito y confirmación simulada.
- Perfil y avisos generales sobre medicamentos, embarazo y lactancia.

Los datos se guardan solo en la sesión activa del navegador. No hay cuentas, base de datos, IA, pagos, verificación de proveedores ni evaluación de interacciones. Los precios y proveedores son ilustrativos; no se recomiendan dosis ni tratamientos. En `app.py`, edita las listas `PLANTS` y `PRODUCTS` para agregar contenido después de revisarlo profesionalmente.

Fuentes de las fichas: NCCIH, [passionflower](https://www.nccih.nih.gov/health/passionflower), [chamomile](https://www.nccih.nih.gov/health/chamomile), [peppermint oil](https://www.nccih.nih.gov/health/peppermint-oil).
