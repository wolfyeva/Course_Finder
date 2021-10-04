import pandas as pd
import tkinter as tk  # for making GUI
import tkinter.messagebox


def surf(url):
    df = pd.read_html(url)
    max = int(df[0].loc[10]['姓名'])
    name = df[0].loc[2]['姓名']
    one = df[1]['志願序'].value_counts()[1]
    two = df[1]['志願序'].value_counts()[2]
    three = df[1]['志願序'].value_counts()[3]
    one_p = round(max / (one + 1) * 100)
    if one_p <= 100:
        two_p = 0
        three_p = 0
    else:
        one_p = 100
        two_p = round(max / (one + two + 1) * 100)
        if two_p <= 100:
            three_p = 0
        else:
            two_p = 100
            three_p = round(max / (one + two + three + 1) * 100)
            if three_p > 100:
                three_p = 100
    global line
    line = ""
    line = line + name + '\n'
    line = line + '人數限制：' + str(max) + '\n'
    line = line + '第一志願：' + str(one_p) + '%\n'
    line = line + '第二志願：' + str(two_p) + '%\n'
    line = line + '第三志願：' + str(three_p) + '%\n'
    return line


def surfs(*aug):
    line = ""
    for many in aug:
        line = line + surf(many) + '\n'
    return line


def gui():  # a function to use GUI
    window = tk.Tk()  # create a window
    window.title('選課超快樂')  # set title of window
    window.geometry('610x250')  # set how big the window is
    window.configure(background='orange')  # set background to orange!

    def execute():  # function to close window and get inputs
        global url  # set global variables
        url = url_text.get(1.0, "end-1c")  # get entry of the user
        url = url.replace(' ', '')
        url = url.split("\n")
        line = surfs(*url)
        tkinter.messagebox.showinfo("搜尋結果", message=line, default='ok')

    o_frame = tk.Frame(window, width=20)  # create a frame
    o_frame.pack(side=tk.LEFT)  # pack to window
    t_frame = tk.Frame(window, width=20)  # create a frame
    t_frame.pack(side=tk.RIGHT)  # pack to window
    url_label = tk.Label(text='請輸入網址：\n (可換行分段)')  # set what to display
    url_label.pack(side=tk.TOP)  # start from left
    url_frame = tk.Frame(window)  # create a frame
    url_frame.pack(side=tk.TOP)  # pack to window

    text_scr = tk.Scrollbar(url_frame)
    url_text = tk.Text(url_frame, height=5, yscrollcommand=text_scr.set)  # where user input
    text_scr.pack(side=tk.RIGHT, fill=tk.Y)
    url_text.insert(0.0,
                    'https://cis.ncu.edu.tw/Course/main/query/byKeywords?courselist=07006\n'
                    'https://cis.ncu.edu.tw/Course/main/query/byKeywords?courselist=07007')
    # set default value
    url_text.pack(side=tk.LEFT)  # start from left
    text_scr.config(command=url_text.yview)
    exe_btn = tk.Button(window, text='Go!', command=execute)  # a button to execute
    exe_btn.pack()  # pack the button
    window.mainloop()  # loop to continue showing the window


if __name__ == '__main__':
    gui()
