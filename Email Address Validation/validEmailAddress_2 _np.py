"""
File: validEmailAd.py
Name:
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  TODO:
feature2:  TODO:
feature3:  TODO:
feature4:  TODO:
feature5:  TODO:
feature6:  TODO:
feature7:  TODO:
feature8:  TODO:
feature9:  TODO:
feature10: TODO:

Accuracy of your model: TODO:
"""

import numpy as np

WEIGHT = np.array([
    [-1],  # Feature 0: Contains '@'
    [-2.65],  # Feature 1:  '.' before '@'
    [-2.6],  # Feature 2: Non-empty local part before '@'
    [0.76],  # Feature 3: Non-empty domain part after '@'
    [1],  # Feature 4: Contains '.' in the domain part
    [-6],   # Feature 5: Contains invalid characters
    [0.74],  # Feature 6: Ends with '.com'
    [0.7],  # Feature 7: Ends with '.edu'
    [0.75],  # Feature 8: Ends with '.tw'
    [-6]   # Feature 9: Contains '..'
])

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
    maybe_email_list = read_in_data()
    correct_predictions = 0
    total_emails = len(maybe_email_list)

    for idx, maybe_email in enumerate(maybe_email_list):
        print(maybe_email)
        # 提取特徵
        feature_vector = feature_extractor(maybe_email)

        # 計算分數
        score = np.dot(feature_vector, WEIGHT).sum()
        print(score)

        # 判斷是否有效
        is_valid = score > 0  # 分數 > 0 表示有效

        # 比較預測與真實標籤
        if (idx <= 13 and not is_valid) or (idx > 13 and is_valid):
            correct_predictions += 1  # 正確分類則計數 +1

    # 計算準確率
    accuracy = correct_predictions / total_emails
    print(f'Accuracy of this model: {accuracy:.16f}')


def feature_extractor(maybe_email):
    feature_vector = np.zeros(len(WEIGHT))
    invalid_characters = "()\\,;<>[]#^%$\""

    for i in range(len(feature_vector)):
        if i == 0:  # Feature 0: Contains '@'
            feature_vector[i] = 1 if '@' not in maybe_email else 0

        elif i == 1:  # Feature 1: No '.' before '@'
            if '@' in maybe_email:
                local_part = maybe_email.split('@')[0]
                feature_vector[i] = 1 if '.' in local_part else 0

        elif i == 2:  # Feature 2: Non-empty local part
            if '@' in maybe_email:
                local_part = maybe_email.split('@')[0]
                feature_vector[i] = 1 if len(local_part) == 0 else 0

        elif i == 3:  # Feature 3: Non-empty domain part
            if '@' in maybe_email:
                domain_part = maybe_email.split('@')[1]
                feature_vector[i] = 1 if len(domain_part) > 0 else 0

        elif i == 4:  # Feature 4: Contains '.' in domain part
            if '@' in maybe_email:
                domain_part = maybe_email.split('@')[1]
                feature_vector[i] = 1 if '.' in domain_part and domain_part.rsplit('.', 1)[-1].isalpha() else 0

        elif i == 5:  # Feature 5: Contains invalid characters
            feature_vector[i] = 1 if any(c in invalid_characters for c in maybe_email) else 0

        elif i == 6:  # Feature 6: Ends with '.com'
            feature_vector[i] = 1 if maybe_email.endswith('.com') else 0

        elif i == 7:  # Feature 7: Ends with '.edu'
            feature_vector[i] = 1 if maybe_email.endswith('.edu') else 0

        elif i == 8:  # Feature 8: Ends with '.tw'
            feature_vector[i] = 1 if maybe_email.endswith('.tw') else 0

        elif i == 9:  # Feature 9: Contains '..'
            feature_vector[i] = 1 if '..' in maybe_email else 0

    print(f"Feature vector: {feature_vector}")
    return feature_vector


def read_in_data():
    """
    :return: list, containing strings that may be valid email addresses
    """
    email_list = []
    with open(DATA_FILE, 'r') as f:
        for line in f:
            email_list.append(line.strip())
    return email_list


if __name__ == '__main__':
    main()

