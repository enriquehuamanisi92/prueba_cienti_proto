"""Validación del recorrido real en Chromium; servidor en puerto 3000."""
from pathlib import Path
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1080},accept_downloads=True)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto('http://127.0.0.1:3000')
    page.wait_for_selector('#patientsTableBody tr',state='attached')
    assert page.locator('#patientsTableBody tr').count()==4
    page.screenshot(path='/tmp/chaski-desktop.png',full_page=True)
    page.locator('[data-preset=alarm]').click()
    page.locator('#consent').check()
    page.locator('#submitMeasurement').click()
    assert 'Busca ayuda' in page.locator('#result').inner_text()
    page.locator('nav [data-view=caregiver]').click()
    page.locator('#familyList [data-confirm]').first.click()
    assert 'RECEPCIÓN FAMILIAR CONFIRMADA' in page.locator('#familyList').inner_text()
    page.locator('nav [data-view=doctor]').click()
    page.locator('#patientsTableBody [data-case]').first.click()
    page.locator('#managementNote').fill('Se revisó la medición sintética y se coordinó seguimiento de demostración.')
    page.locator('#manageBtn').click()
    assert 'Gestión profesional' in page.locator('#caseContent').inner_text()
    page.locator('#closeModal').click()
    with page.expect_download() as download:
        page.locator('a[download]').click()
    assert download.value.suggested_filename=='chaski-salud-demo.csv'
    page.locator('nav [data-view=patient]').click()
    page.locator('#networkToggleBtn').click()
    page.locator('[data-preset=stable]').click()
    page.locator('#submitMeasurement').click()
    assert 'sin conexión' in page.locator('#result').inner_text()
    count=page.evaluate('JSON.parse(localStorage.getItem("chaski-demo-v1")).length')
    page.reload()
    page.wait_for_selector('#patientsTableBody tr',state='attached')
    assert page.evaluate('JSON.parse(localStorage.getItem("chaski-demo-v1")).length')==count
    assert page.evaluate('JSON.parse(localStorage.getItem("chaski-demo-v1")).every(c=>c.status!=="pendiente")')
    # Validación de medición parcial, sin fabricar un registro.
    page.locator('#vitalSys').fill('120')
    page.locator('#vitalDia').fill('')
    page.locator('#consent').check()
    page.locator('#submitMeasurement').click()
    assert 'ambos' in page.locator('#formError').inner_text()
    page.locator('nav [data-view=pitch]').click()
    page.locator('#chatInput').fill('1');page.locator('#chatForm button').click()
    page.locator('#chatConsent').check()
    page.locator('#chatInput').fill('120/80');page.locator('#chatForm button').click()
    assert 'Seguimiento' in page.locator('#chatLog').inner_text()
    page.locator('nav [data-view=doctor]').click()
    page.screenshot(path='/tmp/chaski-panel.png',full_page=True)
    page.locator('nav [data-view=patient]').click()
    # Modo realmente offline después de que el service worker controle la página.
    page.evaluate('navigator.serviceWorker.ready')
    page.reload();page.wait_for_selector('#statusCard h2')
    page.context.set_offline(True)
    page.reload();page.wait_for_selector('#statusCard h2')
    assert 'Sin conexión' in page.locator('#networkToggleBtn').inner_text()
    page.context.set_offline(False)
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path='/tmp/chaski-mobile.png',full_page=True)
    for v in ['patient','caregiver','doctor','pitch']:
        page.locator(f'nav [data-view={v}]').click()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),f'Desborde móvil en {v}'
    assert not errors,errors
    print('OK: registro, alerta, confirmación, gestión, CSV, persistencia, sincronización sin duplicados, validación, chat, modo offline real y cuatro vistas móviles. Sin errores JS.')
    browser.close()
