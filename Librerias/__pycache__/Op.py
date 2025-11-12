import os
import shutil
import subprocess
import datetime

def ask_confirm(prompt="¿Continuar? (si/no): "):
    r = input(prompt).strip().lower()
    return r in ("s", "si", "y", "yes")

def safe_backup(paths, dest_dir="backups"):
    """Crea un archivo .tar.gz con las rutas indicadas. No borra nada."""
    os.makedirs(dest_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = os.path.join(dest_dir, f"backup-{timestamp}")
    # shutil.make_archive genera archive_name + .tar.gz
    base = shutil.make_archive(archive_name, 'gztar', root_dir='.', base_dir='.')
    return base

def conditional_action(value, trigger_a, trigger_b, dry_run=True):
    """
    Si `value` == trigger_a realiza acción A (respaldo).
    Si `value` == trigger_b realiza acción B (notificación).
    dry_run=True => no ejecutar acciones que cambien el sistema sin confirmación.
    """
    if value == trigger_a:
        print(f"[INFO] Se activó trigger A (valor={value}). Acción: crear respaldo.")
        if dry_run:
            print("[DRY RUN] Se habría creado un respaldo. Para ejecutarlo, llama con dry_run=False y confirma.")
            return {"action":"backup","status":"dry-run"}
        if not ask_confirm("Se va a crear un respaldo. ¿Confirmas? (si/no): "):
            print("Cancelado por el usuario.")
            return {"action":"backup","status":"cancelled"}
        archive = safe_backup(["."])  # ajusta rutas si quieres
        print(f"Backup creado en: {archive}")
        return {"action":"backup","status":"done","archive":archive}

    elif value == trigger_b:
        print(f"[INFO] Se activó trigger B (valor={value}). Acción: notificar por consola.")
        # Aquí puedes ampliar: enviar correo, registrar en fichero, etc. (no destructivo)
        log_file = "events.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().isoformat()} - Trigger B activado (valor={value})\n")
        print(f"Evento registrado en {log_file}")
        return {"action":"notify","status":"done","log":log_file}

    else:
        print(f"[INFO] Valor {value} no coincide con triggers ({trigger_a}, {trigger_b}). No se hace nada.")
        return {"action":"none","status":"noop"}