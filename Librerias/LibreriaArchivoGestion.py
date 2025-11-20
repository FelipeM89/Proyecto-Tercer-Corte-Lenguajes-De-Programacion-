"""
LibreriaArchivoGestion.py
Lectura/escritura básica de archivos y CSV sin dependencias externas.
Funciones:
 - leer_txt, escribir_txt, append_txt
 - guardar_csv, cargar_csv
 - guardar_matriz_csv, cargar_matriz_csv
"""

def leer_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def escribir_txt(path, contenido):
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(contenido))
    return True

def append_txt(path, contenido):
    with open(path, "a", encoding="utf-8") as f:
        f.write(str(contenido))
    return True

def _split_csv_line(line, sep=','):
    parts = []
    cur = ""
    in_quote = False
    quotechar = None
    for ch in line:
        if ch in ('"', "'"):
            if not in_quote:
                in_quote = True
                quotechar = ch
                continue
            else:
                if ch == quotechar:
                    in_quote = False
                    quotechar = None
                    continue
        if ch == sep and not in_quote:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [p.strip() for p in parts]

def guardar_csv(path, rows, sep=','):
    lines = []
    for row in rows:
        lines.append(sep.join(str(x) for x in row))
    escribir_txt(path, "\n".join(lines))
    return True

def cargar_csv(path, sep=',', tipo=float):
    txt = leer_txt(path)
    lines = [ln for ln in txt.splitlines() if ln.strip() != ""]
    res = []
    for ln in lines:
        parts = _split_csv_line(ln, sep)
        res.append([tipo(p) for p in parts])
    return res

def guardar_matriz_csv(path, M):
    return guardar_csv(path, M)

def cargar_matriz_csv(path):
    return cargar_csv(path)