#!/usr/bin/env python
import subprocess

proc = subprocess.Popen(["pip", "list"], stdout=subprocess.PIPE)
out, err = proc.communicate()

out_str = out.decode("utf-8")

if proc.returncode < 0:
    print("Please install python")

if "black" in out_str and "flake8" in out_str:
    print("Formatter start")
    proc = subprocess.Popen(["black", "."], stdout=subprocess.PIPE)
    out, err = proc.communicate()

    if proc.returncode < 0:
        print("Please check your error")
        print(out.decode("utf-8"))
        raise SystemExit(1)

    print("Linter start")
    proc = subprocess.Popen(["flake8", "."], stdout=subprocess.PIPE)
    out, err = proc.communicate()

    if len(out.decode("utf-8")) > 0:
        print("Please check below files with PEP8")
        print(out.decode("utf-8"))
        raise SystemExit(-1)

    print("It's ready to commit")
    raise SystemExit(0)
else:
    print(
        "black and flake9 are not found.  Did you forget to activate your virtualenv?"
    )
    raise SystemExit(-1)
