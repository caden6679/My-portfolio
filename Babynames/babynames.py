"""
File: babynames.py
Name: Caden
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    # 如果名字已經存在，則添加新的年份和比較高的排名
    if name in name_data:
        if year in name_data[name]:
            # 如果年份已存在，比較現有排名和新排名，保留較高的排名
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank
        else:
            # 如果年份不存在，直接添加新的年份和排名
            name_data[name][year] = rank
    else:
        # 如果名字不存在，創建一個新的字典並添加到 name_data 中
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        first_line = True
        for line in f:
            # 如果是第一行，單獨處理年份
            if first_line:
                year = line.strip()
                first_line = False
            else:
                # 分割每一行的內容
                rank, name1, name2 = line.split(',')

                # 進一步處理
                rank = rank.strip()
                name1 = name1.strip()
                name2 = name2.strip()

                # 處理男生名字
                if name1:
                    add_data_for_name(name_data, year, rank, name1)

                # 處理女生名字
                if name2:
                    add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}  # 初始化空的 name_data 字典

    for filename in filenames:
        add_file(name_data, filename)  # 將每個文件的數據添加到 name_data 中

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []

    # 將目標字符串轉換為小寫，以進行不區分大小寫的比較
    target_lower = target.lower()

    # 遍歷 name_data 字典中的每個名字
    for name in name_data:
        # 將名字轉換為小寫，以進行不區分大小寫的比較
        name_lower = name.lower()

        # 如果目標字符串在名字中，將這個名字添加到匹配列表中
        if target_lower in name_lower:
            matching_names.append(name)

    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
