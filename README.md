
---

# ASSIGNMENT 2

---

## Authors

- David Arismendy
- Johan Rico
- Laura Restrepo

---

## Class Number

7308

---

## Versions

- **Operating System**: Windows 10 / Ubuntu 22.04  
- **Programming Language**: 🐍 Python 3.11 
- **IDE**: PyCharm  
- **Additional Tools**:
  - Git & GitHub (for version control)
  - Markdown (for documentation)
  - Python Standard Libraries: `random`, `string`

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/EAFIT-AACS/assignment2-los-formales.git
cd assignment2-los-formales
```

#### File Structure

Please save all algorithms in the same folder:

```bash
.
├── ALGORITHM_1_LFCO_2025_JR_LR_DA.py  # Strings generator
├── ALGORITHM_2_LFCO_2025_JR_LR_DA.py  # PDA implementation
├── ALGORITHM_3_LFCO_2025_JR_LR_DA.py  # Tree and transitions printer
├── MAIN_ALGORITHM_LFCO_2025_JR_LR_DA.py # Main menu
└── README.md
```

### 2. Run the Program

Ensure Python is installed and available in your system path (no third-party libraries are required). Then run each algorithm:

#### Algorithm 1
```bash
python ALGORITHM_1_LFCO_2025_JR_LR_DA.py
```

#### Algorithm 2
```bash
python ALGORITHM_2_LFCO_2025_JR_LR_DA.py
```

#### Algorithm 3
```bash
python ALGORITHM_3_LFCO_2025_JR_LR_DA.py
```

If you want to run the process step-by-step or test the PDA, use the main algorithm:

```bash
python MAIN_ALGORITHM_LFCO_2025_JR_LR_DA.py
```

#### Menu Options

Upon execution, a menu will be displayed with the following options:

1. **Generate Strings** – Use Algorithm 1 to generate random palindromic and non-palindromic strings and save them in the list.
2. **Add Strings** – Manually enter strings to test and add them to the list.
3. **Test Strings** – Validate if each string is accepted by the PDA using Algorithm 2.
4. **Print Tree** – Show the transition steps from Algorithm 3.
5. **Clear String List** – Empty the list of strings.
6. **Print Grammar Rules** – Show the grammar rules used in the PDA.
7. **Exit** – Close the program.

---

## Explanation of the Algorithm

