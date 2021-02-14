# FT-MCS
FT-MCS is small library which computes the minimal cutsets of a given fault tree using the famous MOCUS algorithm [1,2]. 

## Installation 

> pip install cutsets==1.0

## Usage

### 1) aircraft.csv

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
> import cutsets

> ft = cutsets.get_ft(aircraft.csv)

> cs = cutsets.mocus(ft)

> print (cs)
```
output:

[['C2', 'B2'], ['B2', 'C3'], ['C4', 'B2'], ['D1', 'B2', 'D2']]
```

### 2) example.py


```python
#!/usr/bin/env python3

import cutsets 

simple_ft = [("TOP", "Or", ["E1", "E2"]),
      ("E1", "Or", ["a", "b"]),
      ("E2", "And", ["c", "d"])]

cs = cutsets.mocus (simple_ft)
```

> ./example.py

```
Output:

[['a'], ['b'], ['d', 'c']]

```

## References

1. N. Limnios and R. Ziani, "An Algorithm for Reducing Cut Sets in Fault-Tree Analysis," in IEEE Transactions on Reliability, vol. 35, no. 5, pp. 559-562, Dec. 1986, doi: 10.1109/TR.1986.4335545.
2. J. B. Fussell, W. E. Vesely,"A New Methodology for Obtaining Cut Sets for Fault Trees", Trans. Am. Nucl. Soc., vol 15, 1972 Jun, pp 262-263.
