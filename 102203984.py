import sys
import pandas as pd
import numpy as np

def validate_inputs(args):
    if len(args) != 5:
        raise ValueError("Error: Incorrect number of parameters. Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")

    input_file, weights, impacts, output_file = args[1], args[2], args[3], args[4]

  
    try:
        pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file '{input_file}' not found.")

    
    weights = list(map(float, weights.split(',')))
    if any(w <= 0 for w in weights):
        raise ValueError("Error: Weights must be positive numbers.")

    
    impacts = impacts.split(',')
    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Error: Impacts must be '+' or '-'.")

    return input_file, weights, impacts, output_file

def topsis(input_file, weights, impacts):
    
    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise ValueError("Error: Input file must contain at least three columns.")

    
    data = df.iloc[:, 1:]

    if not np.issubdtype(data.dtypes.to_numpy(), np.number):
        raise ValueError("Error: All criteria columns must contain numeric values.")

  
    norm_data = data / np.sqrt((data**2).sum())

    
    weighted_data = norm_data * weights

    
    ideal_best = [weighted_data[col].max() if imp == '+' else weighted_data[col].min() for col, imp in zip(weighted_data.columns, impacts)]
    ideal_worst = [weighted_data[col].min() if imp == '+' else weighted_data[col].max() for col, imp in zip(weighted_data.columns, impacts)]

    
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    
    scores = dist_worst / (dist_best + dist_worst)

    
    df['Topsis Score'] = scores
    df['Rank'] = scores.rank(ascending=False).astype(int)

    return df

def main():
    try:
  
        input_file, weights, impacts, output_file = validate_inputs(sys.argv)

       
        result_df = topsis(input_file, weights, impacts)

        result_df.to_csv(output_file, index=False)
        print(f"Success: Results saved to '{output_file}'")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
