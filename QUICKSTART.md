# 🚀 Quick Start Guide

Get up and running with FT-MCS in 2 minutes!

## Installation

```bash
pip install cutsets
```

## Your First Minimal Cutsets Computation

### Method 1: Define Fault Tree in Code

```python
import cutsets

# Define your fault tree
ft = [
    ("TOP", "Or", ["Engine1Fail", "Engine2Fail"]),
    ("Engine1Fail", "And", ["FuelPump1", "Ignition1"]),
    ("Engine2Fail", "And", ["FuelPump2", "Ignition2"]),
]

# Compute minimal cutsets
mcs = cutsets.mocus(ft)

# View results
for cutset in mcs:
    print(cutset)
```

**Output:**
```
['FuelPump1', 'Ignition1']
['FuelPump2', 'Ignition2']
```

### Method 2: Load from CSV File

Create a file `system.csv`:
```
TOP,Or,Module1Fail Module2Fail
Module1Fail,And,Component1 Component2
Module2Fail,And,Component3 Component4
```

Then in Python:
```python
import cutsets

# Load and analyze
ft = cutsets.get_ft('system.csv')
mcs = cutsets.mocus(ft)

print(mcs)
```

## What Are Minimal Cutsets?

Minimal cutsets tell you the **minimum combinations of failures** that cause system failure:

```
MCS: [['A', 'B'], ['C']]

Meaning:
  - System fails if A AND B both fail, OR
  - System fails if C fails
```

## Next Steps

- 📖 Read [USAGE.md](USAGE.md) for detailed examples
- 🔍 Check [examples/](examples/) for real-world case studies
- ❓ Visit [README.md](README.md) for complete API documentation

## Common Use Cases

### 🛩️ Aerospace/Aviation
Identify critical failure combinations in aircraft systems

### 🏭 Industrial Systems
Analyze production line dependencies and critical failures

### ⚡ Power Systems
Determine minimal power outage scenarios

### 🏥 Medical Devices
Safety-critical system failure analysis

---

**Ready to analyze your fault tree?** Start with one of the examples above!
