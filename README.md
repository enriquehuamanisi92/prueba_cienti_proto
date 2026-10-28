# Chaski Salud · Demo para hackatón

Propuesta interactiva con datos sintéticos. Sitio estático en HTML, CSS y JavaScript, basado en la navegación, formulario, panel y ficha del HTML TeleVigía entregado. El original se conserva en `docs/TeleVigia-base.html`.

## Ver la demo

Desde esta carpeta:

```sh
npm run dev
```

Abrir el puerto 3000 en el navegador. Para generar la versión publicable:

```sh
npm run build
npm run preview
```

Node 18+ y Python 3 para el servidor local. No necesita `npm install`, API, claves, cuentas ni base de datos. `dist/` contiene el sitio generado.

## Publicar en Vercel

1. Sube los archivos del proyecto al repositorio `enriquehuamanisi92/prueba_cienti_proto` en GitHub.
2. En Vercel, elige **Add New → Project** e importa ese repositorio.
3. Framework: **Other**. Root Directory: raíz del repositorio.
4. Build Command: `npm run build`. Output Directory: `dist`. Sin variables de entorno. El archivo `vercel.json` ya define estos valores.
5. Pulsa **Deploy** y usa la URL que Vercel genere para la exposición.

Alternativa con Vercel CLI desde esta carpeta: `npx vercel` y luego `npx vercel --prod`, iniciando sesión en tu propia cuenta. Este proyecto no se ha publicado automáticamente ni enviado a GitHub.

## Recorrido recomendado

Ver `docs/GUION_EXPOSICION.md`. También existe una vista “El proyecto” dentro de la demo.

- Paciente: perfiles ficticios, mediciones opcionales, síntomas sin aparato y escenarios precargados.
- Resultado inmediato con cuatro colores y motivos explicables.
- Familia: confirmación de recepción separada de la gestión.
- Profesional: filtros, prioridad, gestión escrita, historial y trazabilidad.
- Coordinación: simulación explícita del vencimiento del plazo, reintento y escalamiento.
- Laboratorio: conversación guiada que registra mediciones, sin WhatsApp ni IA externos.
- Modo sin conexión: cola persistente local, sincronización simulada sin duplicados y service worker que permite recargar después de la primera visita.
- CSV: descarga de los eventos, actores y fechas del recorrido.

## Límites de la demostración

Todos los datos son sintéticos. Las vistas de roles son un selector de exposición, no autenticación o autorización. Los registros viven en localStorage del navegador: no se comparten entre personas, pestañas o dispositivos de forma coordinada. El botón de borrado restaura los ejemplos. No ingreses información personal o clínica real.

El estado “enviada” representa un envío simulado. No hay mensajería real, contactos con establecimientos, verificación profesional, n8n, RENIPRESS, OCR, agenda ni atención médica. Se usa una familia precargada por paciente, sin proceso real de invitación. Los tiempos son los realmente transcurridos en la demo; el escalamiento se activa manualmente para representar un plazo vencido.

El informe concreta el umbral de presión 180/120 y los síntomas de alarma; los otros umbrales son ilustrativos, no están clínicamente validados. No diagnostica, receta ni cambia tratamientos. La pantalla de ayuda ofrece 106 y 113 con la aclaración de cobertura. La PWA requiere HTTPS o localhost y compatibilidad del navegador.

## Validación

`node --check static/app.js` y `npm run build`.

La prueba `tests/browser_smoke.py` usa Playwright y Chromium para registrar, confirmar, gestionar, exportar, recargar, sincronizar sin duplicados, validar entradas, probar el chat y verificar las cuatro vistas en móvil y recarga offline real. Requiere el sitio servido en puerto 3000, el paquete Python `playwright` y Chromium en `/usr/bin/chromium`.
