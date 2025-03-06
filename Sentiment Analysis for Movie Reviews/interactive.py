"""
File: interactive.py
Name: 
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

import sys
import json
from util import interactivePrompt
from submission import extractWordFeatures


def loadWeights(weights_path):
    """
    Load weights from a file.
    @param weights_path: str, the path to the weights file.
    @return: dict[str, float], a dictionary of weights.
    """
    weights = {}
    with open(weights_path, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split('\t')
            weights[key] = float(value)
    return weights


def main():
    weights_path = 'weights'  # Ensure the weights file exists in the current directory
    try:
        weights = loadWeights(weights_path)
        print("Weights loaded successfully. You can now input reviews for prediction.")
    except FileNotFoundError:
        print(f"Error: Weights file '{weights_path}' not found. Make sure to generate the weights using grader.py.")
        sys.exit(1)

    # Call interactivePrompt to allow user inputs and predictions
    interactivePrompt(extractWordFeatures, weights)


if __name__ == '__main__':
    main()
