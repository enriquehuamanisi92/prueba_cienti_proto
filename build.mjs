import { mkdir, copyFile, cp, rm, readFile, writeFile, access } from 'node:fs/promises';
await rm('dist', { recursive: true, force: true });
await mkdir('dist', { recursive: true });
await copyFile('index.html', 'dist/index.html');
await copyFile('sw.js', 'dist/sw.js');
await cp('static', 'dist/static', { recursive: true });
// Usa el archivo original del usuario cuando esté disponible, sin recrearlo.
for (const filename of ['logo.jpg', 'logo.jpeg', 'logo.png', 'logo.webp', 'logo.svg']) {
  try { await access(`static/${filename}`); } catch { continue; }
  const html = await readFile('dist/index.html', 'utf8');
  await writeFile('dist/index.html', html.replace(/(<a class="brand"[^>]*>)[\s\S]*?(<\/a>)/, `$1<img class="brand-image" src="/static/${filename}" alt="Chaski Salud · Cada aviso, un cuidado">$2`));
  const worker = await readFile('dist/sw.js', 'utf8');
  await writeFile('dist/sw.js', worker.replace("const FILES=[", `const FILES=['/static/${filename}',`));
  console.log(`Logo original incorporado: ${filename}`);
  break;
}
console.log('Chaski Salud: sitio estático generado en dist/');
