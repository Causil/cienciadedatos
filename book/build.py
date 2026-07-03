"""Compila main.tex: pdflatex -> bibtex -> pdflatex -> pdflatex."""
import subprocess
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).parent

STEPS = [
    ["pdflatex", "-interaction=nonstopmode", "main.tex"],
    ["bibtex", "main"],
    ["pdflatex", "-interaction=nonstopmode", "main.tex"],
    ["pdflatex", "-interaction=nonstopmode", "main.tex"],
]

for cmd in STEPS:
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=BOOK_DIR)
    if result.returncode != 0:
        if cmd[0] == "bibtex":
            print("Advertencia: bibtex falló (probablemente no hay \\cite{} en el texto aún). Continuando...")
            continue
        print(f"Fallo en: {' '.join(cmd)} (código {result.returncode})")
        sys.exit(result.returncode)

print("main.pdf generado correctamente.")
