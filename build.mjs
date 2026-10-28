import { mkdir, copyFile, cp, rm } from 'node:fs/promises';
await rm('dist', { recursive: true, force: true });
await mkdir('dist', { recursive: true });
await copyFile('index.html', 'dist/index.html');
await copyFile('sw.js', 'dist/sw.js');
await cp('static', 'dist/static', { recursive: true });
console.log('Chaski Salud: sitio estático generado en dist/');
