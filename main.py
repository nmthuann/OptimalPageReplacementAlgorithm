# import thu viện
from tkinter import *
from tkinter import messagebox, scrolledtext
from time import sleep
import numpy as np

# Nhập số lượng khung: 3
# Nhập số lượng trang: 20
# Nhập trang: 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1

def InserStrar(list):
    string = ""
    for i in range(len(list)):
        if list[i] != -1:
            #list[i] = '*'
            string = string +' * '
        else:
            # List[i] = ' '
            string = string + '   '
    return string
def ChuanHoaChuoi(string):
    temp = ""
    for i in range(len(string)):
        if string[i].isdigit():
            temp = temp + string[i]
    return temp
def TinhChinhChuoi(string):
    temp = ""
    for i in range(len(string)):
        if string[i].isdigit():
            temp = temp + string[i] + " "
    return temp
def TinhChinhDanhSach(List):
    temp = ""
    for i in range(len(List)):
        if List[i] != -1:
            temp = temp + str(List[i]) + " "
    return temp
def ConvertStringToList(string):
    List = []
    string=ChuanHoaChuoi(string)
    for i in range(len(string)):
        List.append(int(string[i]))
    return List

#Nhap List
def Input(List,n):
    for i in range(n):
        x = int(input())
        List.append(x)
    # x = [int(input) for i in range(n)]

#Khoi tao Danh Sach
def CreateList(list,n):
    for i in range(n):
       list.append(-1)
    return list

def CreateList0(list,n):
    for i in range(n):
       list.append(0)
    return list

#tim vi tri lau nhat
# def SearchMaxIndex(List,n):
#     Max = List[0]
#     for i in range(n):
#         if List[i] > Max:
#             Max = List[i]

 # Thuat toán tối ưu phân trang
def OPTAlgorithm(PageList,Pages,FrameList,Frames,faults,MaTran,Array,choose):
    # Tuple1 = ()
    #MaTran = (np.ones((Frames, Pages),dtype=int)) # tạo 1  ma trận
    faults = 0
    Temp = []
    CreateList0(Temp,Frames)
    Max = 0
    Index = 0
    flag1 = flag2 = flag3 = True
    CreateList(FrameList,Pages)
    for i in range(Pages):
        flag1 = flag2 = False

        # TH1
        for j in range(Frames):
            if FrameList[j] == PageList[i]:
                flag1 = flag2 = True
                break

        #TH2
        if flag1 == False:
            for j in range(Frames):
                if FrameList[j] == -1:
                    faults = faults + 1
                    # Array.append(i+1)
                    Array[i] = i+1
                    FrameList[j] = PageList[i]
                    flag2 = True
                    break
        #TH3:
        if flag2 == False:
            flag3 = False

            for j in range(Frames):
                Temp[j] = -1
                k = i + 1
                for k in range(k,Pages,1):
                    if FrameList[j] == PageList[k]:
                        Temp[j] = k
                        break

            for j in range(Frames):
                if Temp[j] == -1:
                    Index = j
                    flag3 = True
                    break

            if flag3 == False:
                Max = Temp[0]
                Index = 0
                for j in range(Frames):
                    if Temp[j] > Max:
                        Temp[j] = Max
                        Index = j
            FrameList[Index] = PageList[i]
            faults = faults + 1

            Array[i] = (i+1)
        for j in range(Frames):
            MaTran[j][i] = FrameList[j]
            # print(FrameList[j],end=' ')
        #Tuple1 += tuple(Array,)
    #     print(i)
    # print("Lỗi: ",faults)
    # print(Tuple1)
    FrameList.clear()
    if choose == 1:
        return MaTran
    if choose == 2:
        return faults
    if choose == 3:
        string = InserStrar(Array)
        return string
    if choose == 4:
        return Array

# Khởi tạo giao diện chuong trinh
program = Tk()  # giao dien
program.title("Thuật Toán Phân Trang OPT")  # tên chương trinh
program.geometry("800x450")

def clicked1():
    if selected.get() == 1:
        messagebox.showerror("ERORR", "Chưa cập nhật")
    if selected.get() == 2:
        #Var
        FrameList = [] #Bo nho dem
        PageList = ConvertStringToList(PageListTXT.get())
        FRAMES = int(FramesTXT.get())
        PAGES = int(PagesTXT.get())
        faults = 0
        MaTrix = (np.ones((FRAMES, PAGES), dtype=int))  # tạo 1  ma trận
        Array = []
        CreateList(Array, PAGES)

        Text1 = Label(program, text = "Kết Quả !",font = ("Arial Bold",14))
        Text1.place(x = 140, y = 180)

        fault = OPTAlgorithm(PageList, PAGES, FrameList, FRAMES,faults,MaTrix,Array,2)
        KQ.configure(text=str(OPTAlgorithm(PageList, PAGES, FrameList, FRAMES,faults,MaTrix,Array,1)))
        FAULTS.configure(text="Tổng số Lỗi Trang: "+str(fault))
        PrintStart.configure(text = (OPTAlgorithm(PageList, PAGES, FrameList, FRAMES,faults,MaTrix,Array,3)))
        String =TinhChinhDanhSach(OPTAlgorithm(PageList, PAGES, FrameList, FRAMES,faults,MaTrix,Array,4))
        PrintIndexErorr.configure(text ="Lỗi Trang ở các vị trí: "+ String)

        messagebox.showinfo('Thông Báo', 'Hoàn Thành !')
    if selected.get() == 3:
        messagebox.showerror("ERORR","Chưa cập nhật")
def clicked2():
    messagebox.askyesnocancel("RESET", " Bạn có muốn reset không ?")

def Frames_clicked():
    fm = FramesTXT.get()# fm = Frames
    Frames.configure(text ="Số lượng Khung:  "+ fm)
def Pages_clicked():
    pg = PagesTXT.get()
    Pages.configure(text = "Số Lượng trang: "+ pg)
def PageList_clicked():
    pglist = PageListTXT.get()
    PageList1.configure(text = "Các trang: "+ TinhChinhChuoi(pglist))
def PageListGUI():
    plist=ConvertStringToList(PageListTXT.get())
    return plist


selected = IntVar()
rad1 = Radiobutton(program, text='FIFO', value=1, variable=selected)
rad2 = Radiobutton(program, text='OPT', value=2, variable=selected)
rad3 = Radiobutton(program, text='LRU', value=3, variable=selected)

#Ke bang thong báo chọn chỉ mục: giao giện phím chọn FIFO - OPT -LRU
But1 = Button(program, text="RUN",fg ="green", command=clicked1)
But2 = Button(program, text="RESET",fg ="red", command= clicked2)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
But1.grid(column=3, row=0)
But2.grid(column=4, row=0)

# Đối tượng khung
Frames = Label(program, text = "Nhập Số Lượng Khung ")#, font = ("Arial Bold",16)
Frames.place(x = 50, y= 50)
FramesTXT = Entry(program,width = 5)
FramesTXT.place(x=200,y=50 )
FramesBT = Button(program, text = "OK", fg ="green",command = Frames_clicked)
FramesBT.place(x=240,y=45)

#Đối tượng trang
Pages = Label(program, text = "Nhập Số Lượng Trang")#, font = ("Arial Bold",16)
Pages.place(x = 50, y = 75)
PagesTXT = Entry(program,width = 5)
PagesTXT.place(x=200,y=75 )
PagesBT = Button(program, text = "OK", fg ="green",command = Pages_clicked)
PagesBT.place(x=240,y=70)

#Nhap cac trang
PageList = Label(program, text = "Nhập Các Trang")
PageList1 = Label(program, text = "")
PageList1.place(x=50 ,y= 125)
PageList.place(x = 50, y=100)
PageListTXT = Entry(program,width = 30)
PageListTXT.place(x=180,y=100)
PagesListBT = Button(program, text = "OK", fg ="green",command = PageList_clicked)
PagesListBT.place(x=370,y= 95)


# #Create bảng Hướng dẫn
GhiChu = Label(program, text="Ghi Chú", font=("Arial Bold",10))
GhiChu.place(x=490,y=15)
Table = scrolledtext.ScrolledText(program,width = 25,height = 5)
Table.place(x = 550, y = 10)
Table.insert(INSERT, "-1 : vị trí ô nhớ đã sử  dụng \n")
Table.insert(INSERT, "* : là lỗi\n")
Table.insert(INSERT, "RUN :để chạy chương trình\n")

# Ghi chú kết quả
KQ = Label(program, text = "Kết Quả sẽ xuất hiện ở đây !",font = ("Arial Bold",16))
KQ.place(x = 180, y = 200)
FAULTS = Label(program, text="", font=("Arial Bold", 10))
FAULTS.place(x=100, y=350)
PrintStart = Label(program, text="", font=("Arial Bold", 20))
PrintStart.place(x=180, y=300)
PrintIndexErorr = Label(program, text="", font=("Arial Bold", 10))
PrintIndexErorr.place(x=180, y=370)

program.mainloop()
#window.destroy()

# KQ=
# [[ 1  1  1  1  1  1  1  1  1  1  1  1  7  7  7]
#  [-1  2  2  2  2  2  2  2  2  2  2  2  2  2  2]
#  [-1 -1  3  3  3  3  3  3  3  3  3  3  3  3  3]
#  [-1 -1 -1  4  4  4  5  6  6  6  6  6  6  6  6]]


# if __name__ == "__main__":
#     PageList=[]
#     FrameList = []
#     faults = 0
#     Array = []
#     frames = int(input("Nhap so luong Khung: "))
#     pages = int(input("nhap so luong Trang: "))
#     MaTran = (np.ones((frames, pages), dtype=int))  # tạo 1  ma trận
#     #CreateList(FrameList, pages)
#     CreateList(Array, pages)
#     print(Array)
#     Input(PageList,pages)
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 1))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 2))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 3))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 1))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 3))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 2))
#     print(OPTAlgorithm(PageList, pages, FrameList, frames, faults, MaTran, Array, 4))