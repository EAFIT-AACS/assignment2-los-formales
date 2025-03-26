
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

- **Operating System**: Windows 10 
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
2. **Add Strings** – Manually enter strings and add them to the list.
3. **Test Strings** – Validate if each string is accepted by the PDA using Algorithm 2.
4. **Print Tree** – Show the transition steps from Algorithm 3.
5. **Clear String List** – Empty the list of strings.
6. **Print Grammar Rules** – Show the grammar rules used in the PDA.
7. **Exit** – Close the program.

---

## Explanation of the Automats

Our grammar accepts any palindrome composed of the symbols from the alphabet.  

### Grammar G = (N, Σ, P, S)

- **N** = {Ψ, A, B, C, D, ..., Z}      <- Set of non-terminals  
- **Σ** = {a, b, c, d, ..., z}      <- Set of terminals  
- **P** = {      <- Derivation rules  
  (Ψ, ωΨΩ),      <- Rule I
  (Ψ, ω),      <- Rule II
  (Ψ, ε),      <- Rule III
  (Ω, ω)      <- Rule IV
}  
- **S** = Ψ      <- Initial symbol  

#### Transitions
- Ψ -> ωΨΩ | ω | ε
- Ω -> ω

### PDA M = (Q, Σ, Γ, δ, s, F)

- **Q** = {q}  <- Set of states  
- **Σ** = {a, b, c, d, ..., z}      <- Set of terminals  
- **Γ** = {Ψ, A, B, C, D, ..., Z}      <- Stack alphabet  
- **δ** = {  
  ((q, ω, Ψ), (q, ΨΩ)),      <- Rule I  
  ((q, ω, Ψ), (q, ε)),      <- Rule II  
  ((q, ε, Ψ), (q, ε)),      <- Rule III  
  ((q, ω, Ω), (q, ε))      <- Rule IV       
}  
- **s** = q      <- Initial state  
- **F** = {q}      <- Final states

#### Transitions
- (q, ω, Ψ) -> (q, ΨΩ)
- (q, ω, Ψ) -> (q, ε)
- (q, ε, Ψ) -> (q, ε)
- (q, ω, Ω) -> (q, ε)

### Explanation of Transitions  

These transitions apply to all the strings in the language, where:  
- Ψ is the initial symbol in **G** or the initial stack symbol in **M**.  
- ε is the empty string.  
- ω is a symbol from the alphabet **Σ**.  
- Ω is specifically a symbol from the set of non-terminals **N** in the grammar **G** or from the stack alphabet **Γ** in the PDA **M**, corresponding to ω in **Σ**. This means it is not an arbitrary symbol but rather the uppercase version of ω.  

---

## **Explanation of the Algorithms**

### **1. String Generation Algorithm**

This first algorithm is designed to generate a set of **8 strings**:  
- **4 palindromes**  
- **4 non-palindromes**

Duplicate strings are avoided, and it returns a list of the generated strings, replacing empty strings with **ε**.

#### Example Output

```bash
Strings generated:
1. ε
2. tahowljozvj
3. kzoozk
4. rfbexoenp
5. o
6. wqiba
7. ajhsshja
8. uwjqi
```

### **2. PDA Implementation Algorithm**

This algorithm implements a **Pushdown Automaton (PDA)** based on a given grammar to accept palindromic strings.

Step-by-step **PDA()**:
1. If the entire string has been read **and** the stack is empty, the string is accepted.
2. It checks all possible transitions from the current state.
3. If a match is found:
   - It updates the state and the stack according to the transition.
   - It recursively calls itself with the new values.
4. If no transition leads to acceptance, the string is rejected.

It keeps track of the steps for debugging (although they are not printed by default, as they will be used in Algorithm 3).

- Using Algorithm 1 to provide the input strings, it prints in columns which strings were **accepted** (they are palindromes) and which were **rejected** (they are not).

#### Example Output

```bash
Strings Accepted and Rejected by the PDA:
---------------------------------------------------------------
|           ACCEPTED           |           REJECTED           |
|------------------------------+------------------------------|
|              ε               |             vbq              |
|           lhtllthl           |             dyoj             |
|         bgsxeeexsgb          |            cwoefm            |
|         spexrffrxeps         |           ybgccbit           |
---------------------------------------------------------------
```

## **3. Tree Algorithm**

This algorithm displays the steps of the PDA for each string that is accepted (is a palindrome).

- It simulates the PDA step by step.
- If the string is **accepted**, it prints a **table** showing:
  - The applied **grammar rule**.
  - The **derivation** (how the string is being parsed).
  - The **PDA state**, the **remaining input**, and the **stack contents**.
- If the string is **not accepted**, it simply reports that.

It uses the result of Algorithm 1 (string generation) to validate and print only accepted strings.

#### Example Output

```bash
Configurations on input "":
-----------------------------------------------------------------------------------------
|      |            CFG G             |                      PDA M                      |
|------+------------------------------+-------------------------------------------------|
| Rule |       Derivation in G        | State |       String       |       Stack        |
|------+------------------------------+-------+--------------------+--------------------|
|      |              Ψ               |   q   |         ε          |         Ψ          |
| III  |              ε               |   q   |         ε          |         ε          |
-----------------------------------------------------------------------------------------

String "neli" was not accepted by the PDA.

Configurations on input "u":
-----------------------------------------------------------------------------------------
|      |            CFG G             |                      PDA M                      |
|------+------------------------------+-------------------------------------------------|
| Rule |       Derivation in G        | State |       String       |       Stack        |
|------+------------------------------+-------+--------------------+--------------------|
|      |              Ψ               |   q   |         u          |         Ψ          |
|  II  |              u               |   q   |         ε          |         ε          |
-----------------------------------------------------------------------------------------

String "athrewbvhfrs" was not accepted by the PDA.

Configurations on input "czc":
-----------------------------------------------------------------------------------------
|      |            CFG G             |                      PDA M                      |
|------+------------------------------+-------------------------------------------------|
| Rule |       Derivation in G        | State |       String       |       Stack        |
|------+------------------------------+-------+--------------------+--------------------|
|      |              Ψ               |   q   |        czc         |         Ψ          |
|   I  |             cΨC              |   q   |         zc         |         ΨC         |
|  II  |             czC              |   q   |         c          |         C          |
|  IV  |             czc              |   q   |         ε          |         ε          |
-----------------------------------------------------------------------------------------

Configurations on input "ytty":
-----------------------------------------------------------------------------------------
|      |            CFG G             |                      PDA M                      |
|------+------------------------------+-------------------------------------------------|
| Rule |       Derivation in G        | State |       String       |       Stack        |
|------+------------------------------+-------+--------------------+--------------------|
|      |              Ψ               |   q   |        ytty        |         Ψ          |
|   I  |             yΨY              |   q   |        tty         |         ΨY         |
|   I  |            ytΨTY             |   q   |         ty         |        ΨTY         |
| III  |             ytTY             |   q   |         ty         |         TY         |
|  IV  |             yttY             |   q   |         y          |         Y          |
|  IV  |             ytty             |   q   |         ε          |         ε          |
-----------------------------------------------------------------------------------------

String "deqsdierpy" was not accepted by the PDA.

String "vmezyqvajw" was not accepted by the PDA.
```

## **Main Algorithm**

The main menu allows interaction with the system through the console.
This menu makes the PDA system interactive and user-friendly, allowing the user to test strings, view PDA steps, and understand the language structure being processed.

#### Example Output

```bash
=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 1
Strings generated:
1. yymqppqmyy
2. kook
3. acdfsmxtodl
4. ame
5. xqgjqssqjgqx
6. hjrpdwzsqx
7. zfwhf
8. nn

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 5
String list cleared.

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 2
Enter strings separated by commas: ana,sofia
New List:
Strings generated:
1. ana
2. sofia

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 3

Strings Accepted and Rejected by the PDA:
---------------------------------------------------------------
|           ACCEPTED           |           REJECTED           |
|------------------------------+------------------------------|
|             ana              |            sofia             |
---------------------------------------------------------------

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 4

Configurations on input "ana":
-----------------------------------------------------------------------------------------
|      |            CFG G             |                      PDA M                      |
|------+------------------------------+-------------------------------------------------|
| Rule |       Derivation in G        | State |       String       |       Stack        |
|------+------------------------------+-------+--------------------+--------------------|
|      |              Ψ               |   q   |        ana         |         Ψ          |
|   I  |             aΨA              |   q   |         na         |         ΨA         |
|  II  |             anA              |   q   |         a          |         A          |
|  IV  |             ana              |   q   |         ε          |         ε          |
-----------------------------------------------------------------------------------------

String "sofia" was not accepted by the PDA.

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 6
|         |      CFG      |              PDA             |
|     I.  |    Ψ -> ωΨΩ   |     (q, ω, Ψ) -> (q, ΨΩ)     |
|    II.  |    Ψ -> ω     |     (q, ω, Ψ) -> (q, ε)      |
|   III.  |    Ψ -> ε     |     (q, ε, Ψ) -> (q, ε)      |
|    IV.  |    Ω -> ω     |     (q, ω, Ω) -> (q, ε)      |

=== PDA MENU ===
1. Generate New strings
2. Add strings
3. Validate strings in the PDA
4. Print tree for the strings accepted by the PDA
5. Clear string list
6. Print grammar rules
7. Exit
Choose an option: 7
Exiting...
```

---

