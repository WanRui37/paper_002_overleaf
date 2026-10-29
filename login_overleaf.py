#!/usr/bin/env python3
from pathlib import Path
import os
import sys
root = Path(__file__).resolve().parent
python = root / '.venv/bin/python'
os.environ['PATH'] = str(python.parent) + os.pathsep + os.environ.get('PATH', '')
os.execv(str(python), [str(python), str(root.parent / 'paper_003/tools/003_overleaf/login_overleaf.py')])
