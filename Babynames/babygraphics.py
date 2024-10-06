"""
File: babygraphics.py
Name: Caden
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 計算總年數和每年之間的間隔
    num_years = len(YEARS)
    interval = (width - 2 * GRAPH_MARGIN_SIZE) / num_years
    # 計算並返回當前年份的垂直線的x坐標
    return GRAPH_MARGIN_SIZE + interval * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for year in YEARS:
        x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW,
                           font=("Helvetica", 12))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # 確定顏色索引
    color_index = 0

    # 遍歷查找的每個名字
    for name in lookup_names:
        # 檢查名字是否存在於name_data中
        if name in name_data:
            # 獲取當前名字的數據
            data = name_data[name]

            # 為每一年繪製線條和文字
            for i in range(len(YEARS) - 1):
                x1 = get_x_coordinate(CANVAS_WIDTH, i)
                x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)

                # 計算兩個相鄰年份的y坐標
                y1_raw = data.get(str(YEARS[i]), MAX_RANK)
                y2_raw = data.get(str(YEARS[i + 1]), MAX_RANK)

                # 處理可能的 '*'
                y1 = GRAPH_MARGIN_SIZE + (int(y1_raw) / MAX_RANK * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                                          if y1_raw != MAX_RANK else CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)
                y2 = GRAPH_MARGIN_SIZE + (int(y2_raw) / MAX_RANK * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                                          if y2_raw != MAX_RANK else CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)

                # 繪製線條
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])

                # 在點旁邊繪製文字
                if y1_raw == MAX_RANK:
                    y1_raw = '*'
                text_content = f"{name} {y1_raw}"
                canvas.create_text(x1 + TEXT_DX, y1, text=text_content, anchor=tkinter.SW,
                                   font=("Helvetica", 8), fill=COLORS[color_index])

            # 為最後一年繪製文字
            x_last = get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1)
            y_last_rang = data.get(str(YEARS[-1]),  MAX_RANK)
            y_last = GRAPH_MARGIN_SIZE + (int(y_last_rang) / MAX_RANK * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                                          if y_last_rang != MAX_RANK else CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)
            if y_last_rang == MAX_RANK:
                y_last_rang = '*'
            text_content_last = f"{name} {y_last_rang}"
            print(y_last_rang, y_last)
            canvas.create_text(x_last + TEXT_DX, y_last, text=text_content_last, anchor=tkinter.SW,
                               font=("Helvetica", 8), fill=COLORS[color_index])

            # 增加顏色索引以供下一個名字使用
            color_index = (color_index + 1) % len(COLORS)

    # 更新畫布
    canvas.update()


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
