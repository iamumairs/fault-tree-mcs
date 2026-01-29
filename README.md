# Fault Tree Minimal Cutsets (FT-MCS)

A lightweight, efficient Python library for computing **minimal cutsets** from fault trees using the legendary **MOCUS algorithm**.

> Perfect for reliability engineers, safety analysts, and system architects working with fault tree analysis!

## ✨ Features

- **Fast & Efficient**: Implements the proven MOCUS algorithm for minimal cutset computation
- **Flexible Input**: Load fault trees from CSV files or define them programmatically
- **Easy Integration**: Simple, intuitive API with zero external dependencies
- **Well-Tested**: Validated with real-world aerospace examples
- **MIT Licensed**: Use freely in your projects

## 📦 Installation

Install directly from [PyPI](https://pypi.org/project/cutsets/):

```bash
pip install cutsets
```

## 🚀 Quick Start

### Example 1: Define Fault Tree Programmatically

```python
import cutsets

# Define a simple fault tree
ft = [
    ("TOP", "Or", ["E1", "E2"]),
    ("E1", "Or", ["a", "b"]),
    ("E2", "And", ["c", "d"])
]

# Compute minimal cutsets
mcs = cutsets.mocus(ft)
print(mcs)  # Output: [['a'], ['b'], ['d', 'c']]
```

### Example 2: Load from CSV File

Create a CSV file with your fault tree structure:

```csv
TOP,And,B1 B2
B1,Or,C1 C2 C3 C4
B2,Or,C5 C6 C7
C1,And,D1 D2
C2,And,D1 E2
E2,Or,D3 D4
C3,And,D5 E3
E3,Or,D2 D6
C4,And,D1 D7
C5,And,D5 E5
E5,Or,D2 D6
C6,And,D8 E6
E6,Or,D2 D4 D6
C7,And,D8 E7
E7,Or,D4 D9
```

Then load and analyze:

```python
import cutsets

# Load fault tree from CSV
ft = cutsets.get_ft('aircraft.csv')

# Compute minimal cutsets
mcs = cutsets.mocus(ft)
print(mcs)  # Output: [['C2', 'B2'], ['B2', 'C3'], ['C4', 'B2'], ['D1', 'B2', 'D2']]
```

## 📖 Documentation

### API Reference

#### `cutsets.get_ft(filename)`
Loads a fault tree from a CSV file.

**Parameters:**
- `filename` (str): Path to CSV file with format: `gate_name,gate_type,inputs`
  - `gate_type`: Either `"And"` or `"Or"` (case-sensitive)
  - `inputs`: Space-separated list of child gate/event names

**Returns:** List of tuples representing the fault tree structure

#### `cutsets.mocus(fault_tree)`
Computes minimal cutsets using the MOCUS algorithm.

**Parameters:**
- `fault_tree` (list): Fault tree as list of tuples or from `get_ft()`

**Returns:** List of minimal cutsets (each cutset is a list of basic events)

### Fault Tree Format

Define fault trees as a list of tuples:
```python
[
    (gate_name, gate_type, [child1, child2, ...]),
    ...
]
```

- `gate_name`: Unique identifier (e.g., "TOP", "E1", "B1")
- `gate_type`: Either `"And"` or `"Or"`
- Children: List of child gate/event names

**Important:** The root gate must be named `"TOP"`

## 💡 Examples

Check the [examples](examples/) directory for more detailed demonstrations, including the classic aircraft fault tree analysis.

## 🔬 How It Works

The MOCUS (Method of Obtaining Cut Sets) algorithm:
1. Starts from the TOP event
2. Recursively expands gates according to Boolean logic
3. Identifies minimal cutsets (smallest combinations of events that cause failure)
4. Removes redundant supersets

This is particularly useful in safety-critical systems analysis where you need to understand the minimal combinations of failures that lead to system failure.

## 📚 References

- [1] N. Limnios and R. Ziani, "An Algorithm for Reducing Cut Sets in Fault-Tree Analysis," *IEEE Transactions on Reliability*, vol. 35, no. 5, pp. 559-562, Dec. 1986. [doi: 10.1109/TR.1986.4335545](https://doi.org/10.1109/TR.1986.4335545)
- [2] J. B. Fussell and W. E. Vesely, "A New Methodology for Obtaining Cut Sets for Fault Trees," *Trans. Am. Nucl. Soc.*, vol. 15, pp. 262-263, June 1972.

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## 👤 Author

**Umair Siddique**
- GitHub: [@iamumairs](https://github.com/iamumairs)
- Repository: [fault-tree-mcs](https://github.com/iamumairs/fault-tree-mcs)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the library.

---

<div align="center">

**Made with ❤️ for the reliability engineering community**

</div>
