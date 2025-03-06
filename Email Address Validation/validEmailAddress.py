"""
File: validEmailAddress.py
Name: Alastair
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email
address classifier. You will use a given
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
    # 讀取資料
    maybe_email_list = read_in_data()
    correct_predictions = 0  # 記錄正確分類的數量
    total_emails = len(maybe_email_list)  # 總測試數據數量

    # 遍歷每個 email
    for idx, maybe_email in enumerate(maybe_email_list):
        # 提取特徵向量
        feature_vector = feature_extractor(maybe_email)

        # 計算分數
        score = sum(f * w[0] for f, w in zip(feature_vector, WEIGHT))

        # 判斷是否有效
        is_valid = score > 0  # 分數 > 0 表示有效

        # 比較預測與真實標籤
        if (idx <= 13 and not is_valid) or (idx > 13 and is_valid):
            correct_predictions += 1  # 正確分類則計數 +1

    # 計算準確率
    accuracy = correct_predictions / total_emails
    print(f'Accuracy of this model: {accuracy:.16f}')


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:  # Feature 0: '@' in the str
			feature_vector[i] = 1 if '@' in maybe_email else 0

		elif i == 1:  # Feature 1: No '.' before '@'
			if feature_vector[0]:  # 確保有 '@'
				local_part = maybe_email.split('@')[0]
				feature_vector[i] = 1 if '.' not in local_part else 0

		elif i == 2:  # Feature 2: Some strings before '@'
			if feature_vector[0]:
				local_part = maybe_email.split('@')[0]
				feature_vector[i] = 1 if len(local_part) > 0 else 0

		elif i == 3:  # Feature 3: Some strings after '@'
			if feature_vector[0]:
				domain_part = maybe_email.split('@')[1]
				feature_vector[i] = 1 if len(domain_part) > 0 else 0

		elif i == 4:  # Feature 4: There is '.' after '@'
			if feature_vector[0]:
				domain_part = maybe_email.split('@')[1]
				feature_vector[i] = 1 if '.' in domain_part else 0

		elif i == 5:  # Feature 5: There is no white space
			feature_vector[i] = 1 if ' ' not in maybe_email else 0

		elif i == 6:  # Feature 6: Ends with '.com'
			feature_vector[i] = 1 if maybe_email.endswith('.com') else 0

		elif i == 7:  # Feature 7: Ends with '.edu'
			feature_vector[i] = 1 if maybe_email.endswith('.edu') else 0

		elif i == 8:  # Feature 8: Ends with '.tw'
			feature_vector[i] = 1 if maybe_email.endswith('.tw') else 0

		elif i == 9:  # Feature 9: Length > 10
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	print(feature_vector)
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	email_list = []
	with open(DATA_FILE, 'r') as f:
		for line in f:
			email_list.append(line.strip())
	return email_list


if __name__ == '__main__':
	main()
