# Usage Guide

This guide provides practical examples and best practices for using the FT-MCS library.

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Working with CSV Files](#working-with-csv-files)
3. [Interpreting Results](#interpreting-results)
4. [Common Patterns](#common-patterns)
5. [Troubleshooting](#troubleshooting)

## Basic Usage

### Simple Fault Tree

The most basic way to use the library is to define a fault tree as a list of tuples:

```python
import cutsets

# Define gates and their children
ft = [
    ("TOP", "Or", ["E1", "E2"]),
    ("E1", "And", ["A", "B"]),
    ("E2", "And", ["C", "D"]),
]

# Compute minimal cutsets
mcs = cutsets.mocus(ft)
print(mcs)
# Output: [['A', 'B'], ['C', 'D']]
```

### Understanding Gate Types

- **OR Gate**: Output is True if ANY input is True (minimal sets are single inputs)
- **AND Gate**: Output is True if ALL inputs are True (all must occur together)

## Working with CSV Files

### Creating a CSV File

Format your CSV as follows:

```
GateName,GateType,ChildrenSpace-Separated
TOP,Or,E1 E2 E3
E1,And,A B
E2,And,C D
```

### Loading and Processing

```python
import cutsets

# Load the fault tree
ft = cutsets.get_ft('my_fault_tree.csv')

# Compute minimal cutsets
mcs = cutsets.mocus(ft)

# Save results
with open('results.txt', 'w') as f:
    for cutset in mcs:
        f.write(str(cutset) + '\n')
```

## Interpreting Results

Each minimal cutset is a list of events. The cutsets together describe all minimal combinations that lead to system failure:

```python
mcs = [['A', 'B'], ['C', 'D'], ['E']]
```

This means:
- System fails if events A AND B both occur, OR
- System fails if events C AND D both occur, OR
- System fails if event E occurs

## Common Patterns

### Aerospace Example

Analyzing aircraft system failures:

```python
import cutsets

# Aircraft power system fault tree
ft = [
    ("TOP", "Or", ["GeneratorFailure", "BatteryFailure"]),
    ("GeneratorFailure", "And", ["EngineShutdown", "RegulatorFault"]),
    ("BatteryFailure", "Or", ["BatteryDepleted", "ChargerFault"]),
]

mcs = cutsets.mocus(ft)
print("Critical failure combinations:", mcs)
```

### Safety System Analysis

Analyzing redundant safety systems:

```python
import cutsets

# Safety system with redundancy
ft = [
    ("TOP", "And", ["Sensor1Down", "Sensor2Down"]),
    ("Sensor1Down", "Or", ["Sensor1Fail", "Sensor1Offline"]),
    ("Sensor2Down", "Or", ["Sensor2Fail", "Sensor2Offline"]),
]

mcs = cutsets.mocus(ft)
print("System needs both sensors to fail:", mcs)
```

### Nested Gate Example

Complex hierarchical systems:

```python
import cutsets

ft = [
    ("TOP", "Or", ["MainSystemFail", "BackupSystemFail"]),
    ("MainSystemFail", "And", ["Control", "Power"]),
    ("Control", "Or", ["CPU1Down", "CPU2Down"]),
    ("Power", "Or", ["PSU1Down", "PSU2Down"]),
    ("BackupSystemFail", "And", ["BackupControl", "BackupPower"]),
]

mcs = cutsets.mocus(ft)
```

## Troubleshooting

### Common Issues

**Issue: "Exception: Only And/OR gates are accepted"**
- Ensure gate types are exactly `"And"` or `"Or"` (case-sensitive)
- Check CSV file formatting

**Issue: Empty result or unexpected cutsets**
- Verify all gate names in children exist as gate definitions
- Ensure `"TOP"` gate is defined
- Check for typos in gate/event names

**Issue: Very long execution time**
- Consider if your fault tree is very large (deep nesting/many gates)
- Try simplifying or decomposing the fault tree
- Verify the fault tree structure is correct

### Tips for Large Fault Trees

1. **Decompose**: Break complex systems into smaller subsystems
2. **Validate**: Use smaller test cases first before processing large trees
3. **Organize**: Keep CSV files well-structured and documented
4. **Review**: Manually verify results for critical systems

## Examples Directory

See the [examples](../examples/) directory for complete working examples including:
- Simple fault tree
- Aircraft system analysis
- Run scripts for batch processing

## Further Reading

For more information on fault tree analysis and the MOCUS algorithm, see the [References](../README.md#-references) in the main README.
