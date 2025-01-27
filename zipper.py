import FreeSimpleGUI as sg

label1 = sg.Text("Select Files to Compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose")

compress_bt = sg.Button("Compress files")

window = sg.Window("File Zipper",layout=[[label1,input1,button1],[label2,input2,button2],[compress_bt]])

window.read()
window.close()
