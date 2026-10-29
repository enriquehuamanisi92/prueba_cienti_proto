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

El estado “enviada” representa un envío simulado. No hay mensajería real, contactos con establecimientos, verificación profesional, n8n, RENIPRESS, OCR, agenda ni atención médica. Se usa una familia precargada por paciente, con invitación por código ficticio. Los tiempos son los realmente transcurridos en la demo; el escalamiento se activa manualmente para representar un plazo vencido.

El informe concreta el umbral de presión 180/120 y los síntomas de alarma; los otros umbrales son ilustrativos, no están clínicamente validados. No diagnostica, receta ni cambia tratamientos. La pantalla de ayuda ofrece 106 y 113 con la aclaración de cobertura. La PWA requiere HTTPS o localhost y compatibilidad del navegador.

## Validación

`node --check static/app.js` y `npm run build`.

La prueba `tests/browser_smoke.py` usa Playwright y Chromium para registrar, confirmar, gestionar, exportar, recargar, sincronizar sin duplicados, validar entradas, probar el chat y verificar las cuatro vistas en móvil y recarga offline real. Requiere el sitio servido en puerto 3000, el paquete Python `playwright` y Chromium en `/usr/bin/chromium`.

## Acceso y registros simulados

La pantalla inicial separa **Iniciar sesión** y **Registrarme**, con roles Paciente, Familiar y Profesional. Las cuentas de ejemplo se precargan al elegir un rol; el código público de exposición es `246810`. Los registros ficticios se conservan en este navegador, sin almacenar contraseñas ni conectarse a una API. Cada sesión muestra solo su vista de rol y la ficha del proyecto. La historia de paciente sigue siendo sintética y precargada.

El profesional registra colegiatura, establecimiento, distrito y dirección ficticios. El catálogo simulado acepta `123456`, rechaza `654321`, rechaza establecimientos inactivos y exige representar una aprobación de coordinación. No consulta CMP, RENIPRESS o MINSA, no acredita identidad y no pretende ser una plataforma oficial. El control de aprobación está disponible solo como paso del guion antes de ingresar; no es un sistema administrativo real.

La separación de pantallas y los controles JavaScript son demostrativos. Un sitio estático no puede garantizar permisos ni impedir manipulación desde herramientas del navegador. Para producción se requiere servidor, autenticación, autorización y validación institucional.

Prueba adicional: `python3 tests/access_smoke.py` verifica los registros, rechazos, aprobación, reingreso y menús por rol.

## Foto, QR, solicitudes por teléfono y contacto adicional

- Registro manual de valores. Se retiró la opción de foto porque no hay extracción automática de números.
- QR real local: cada imagen `static/qr-p*.svg` codifica el código ficticio del paciente. Se puede leer con el lector del teléfono y pegar el texto en el registro familiar. El botón de lectura simulada representa ese paso durante la exposición; no es un escáner de cámara propio. Los QR no caducan ni verifican identidad en esta demo.
- Método por teléfono: muestra la coincidencia con el perfil sintético y crea una solicitud pendiente. El paciente puede aceptar o rechazar. El familiar no ingresa hasta la aceptación. Cambia de sesión en el mismo navegador para representar ambos roles.
- Contacto de emergencia: se configura en el perfil del paciente con nombre, teléfono ficticio, SMS/WhatsApp y plazo de 5, 10 o 15 minutos. El temporizador local registra un envío simulado a ese contacto si falta confirmación del familiar principal, sin exigir que el contacto tenga app. Excluye registros verdes, pendientes, gestionados o ya escalados. El conteo comienza cuando el aviso y el contacto están disponibles. No corre como servicio en segundo plano; requiere la demo abierta y en línea.
- Métrica: alertas amarillas/naranjas/rojas con evento de recepción / alertas amarillas/naranjas/rojas con evento de envío × 100. Cuenta alertas únicas, no personas o reintentos, y muestra el numerador y denominador. Sin envíos muestra “Sin envíos”.

Prueba: `python3 tests/extras_smoke.py` inicia un servidor temporal y verifica solicitud/aprobación, QR, escalamiento automático sin duplicación e indicador exacto.

El contacto de emergencia está al final de la columna derecha, en una sección contraíble inicialmente cerrada. Los contactos guardados con antiguos plazos cortos pasan a 5 minutos al cargar la demo. El CSV usa separador `;`, comillas en cada campo y UTF-8 con BOM para conservar tildes en Excel. El saludo, nombre e iniciales de la vista paciente siguen la cuenta iniciada; la historia sigue siendo sintética.
