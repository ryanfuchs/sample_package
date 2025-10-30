# libafc

A modern football analysis library (modular, PEP8-compliant).

## Install

```
pip install .
```

## Usage

```python
import libafc as FC
match = FC.core.Match(id=1, teams=["A", "B"])
ev = FC.core.Event(1.23, "kickoff")
print(ev.serialize())
```
