# Guion para presentar en 3 minutos

## 0:00–0:30 · El problema

“Una medición enviada por chat no garantiza que alguien la haya visto ni que alguien se haga cargo. Chaski Salud propone cerrar ese circuito entre el adulto, su familia y el personal de salud.”

## 0:30–1:15 · Registro y aviso

En la pantalla inicial elige **Paciente** e inicia sesión con la cuenta de ejemplo (código público `246810`). Abre **Mi salud**. Presenta a Rosa, un perfil totalmente ficticio. Pulsa **Alarma**, acepta el consentimiento de demo y guarda.

“Este escenario genera una alerta roja y muestra ayuda de inmediato. No esperamos a que una persona abra el aviso. Los criterios son ilustrativos y necesitan revisión clínica; la plataforma no diagnostica.”

## 1:15–1:45 · Confirmación familiar

Cierra sesión desde la parte superior y elige **Familiar** para entrar con su cuenta de ejemplo. Abre **Familia**. Pulsa **He recibido el aviso** sobre el nuevo registro.

“El familiar confirma la recepción. Eso no significa que Rosa recibió atención. Por eso mantenemos un estado de gestión distinto.”

## 1:45–2:20 · Profesional y trazabilidad

Cierra sesión, elige **Profesional** e inicia sesión con la cuenta de ejemplo. Abre **Profesional** y revisa el caso rojo nuevo. Escribe “Se revisó el registro sintético y se coordinó seguimiento de demostración”. Pulsa **Registrar gestión**.

“Cada paso conserva una hora y un responsable. La bandeja ayuda a priorizar; la acción de seguimiento la registra el profesional.”

## 2:20–2:45 · Sin conexión

Cierra el detalle, cierra sesión e ingresa como paciente para volver a **Mi salud**, pulsa **En línea** para desconectar y carga **Control habitual**. Guarda y señala “pendiente”. Reconecta.

“Se conserva el registro en este dispositivo y se sincroniza una sola vez dentro de la simulación. No pretendemos que un aviso pendiente ya fue recibido.”

## 2:45–3:00 · Cierre

Abre **El proyecto**.

“Hoy mostramos una propuesta con datos ficticios y canales simulados. Para llevarla al piloto hacen falta validación profesional, convenios, protección de datos e integración de mensajería. Nuestra diferencia es confirmar quién recibió y quién gestionó cada aviso.”

## Antes de exponer

- Abre la URL de Vercel al menos una vez con conexión para cargar los archivos.
- Usa el botón “Borrar datos del navegador” para recuperar los cuatro ejemplos.
- Cada navegador conserva su propia historia; al compartir la URL no se comparten registros.
- La demo no envía mensajes, solicita ambulancias ni agenda citas.
- Si preguntan por la arquitectura futura: React/PWA, FastAPI, PostgreSQL, n8n y canales con convenios, tal como plantea el informe; este entregable es estático para facilitar la presentación.

## Nuevo recorrido de registro (opcional)

En **Registrarme**, selecciona el tipo de cuenta y usa un correo ficticio diferente a los ejemplos. El código público siempre es `246810`; no ingreses contraseñas personales.

- **Paciente**: nombre, celular ficticio, distrito y consentimiento. Se usa la historia sintética de Rosa para representar el seguimiento.
- **Familiar**: agrega parentesco y elige un paciente. El código de invitación aparece junto al nombre (por ejemplo `CHASKI-ROSA`). Acepta el vínculo antes de registrar.
- **Profesional**: usa colegiatura ficticia `123456`, un establecimiento de ejemplo activo y su ubicación. `654321` representa un profesional no habilitado; otro número representa ausencia de coincidencia. Una posta inactiva bloquea la solicitud. Tras la validación ficticia pulsa **Simular aprobación del coordinador**. Explica que este control representa la revisión futura y no verifica una identidad real.

Pacientes y familiares no tienen la opción Profesional en su sesión. Para cambiar el personaje de la exposición hay que cerrar sesión. Esto es separación de interfaz en un sitio estático, no seguridad de producción.

## Invitación desde el paciente

En **Mi salud → Tu red de cuidado**, pulsa **Enviar mi código de vinculación a un familiar**. Se muestra `CHASKI-ROSA`, un mensaje que puedes copiar y el botón **Simular envío al familiar**. No se envían mensajes reales. Para cerrar el recorrido, cierra sesión, abre **Registrarme → Familiar**, elige a Rosa e introduce ese código, junto con el consentimiento del familiar.
