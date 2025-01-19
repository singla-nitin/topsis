

## TOPSIS Implementation

### **Description**
This program implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) decision-making method. It takes input data in the form of a decision matrix, along with the weights and impacts for each criterion, and provides a ranked list of alternatives based on their relative closeness to the ideal solution.

### **Features**
- Accepts input data from a CSV file.
- Computes normalized decision matrix.
- Applies weights and impacts to calculate positive and negative ideal solutions.
- Outputs rankings of the alternatives.

### **Input Requirements**
1. A CSV file with the following structure:
   - The first row should contain the column headers.
   - The first column should contain the names of the alternatives.
   - The subsequent columns should contain numeric values for each criterion.
2. A string specifying weights separated by commas (e.g., `1,2,3,4`).
3. A string specifying impacts separated by commas (e.g., `+,-,+,-`).

### **Output**
The program outputs a CSV file with the following columns:
1. The original decision matrix with weights and impacts applied.
2. The closeness coefficient of each alternative.
3. The rank of each alternative.

### **Usage**
#### **Command Line**
```bash
python topsis.py <input_file> <weights> <impacts> <output_file>
```
Example:
```bash
python topsis.py data.csv "1,2,3,4" "+,-,+,-" result.csv
```

### **Dependencies**
- Python 3.x
- pandas
- numpy

### **Limitations**
- The input file must not contain empty cells.
- Weights and impacts must match the number of criteria columns.



