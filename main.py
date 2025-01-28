import FreeSimpleGUI as sg
import zip_creator

sg.theme("LightBlue")
label1 = sg.Text("Select Files to Compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose",key='files')

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose",key='folder')

compress_bt = sg.Button("Compress files")
output_label = sg.Text(key="output")
icon_path = "favicon.ico"

window = sg.Window("File Zipper",layout=[[label1,input1,button1],[label2,input2,button2],[compress_bt,output_label]],
                   font=('Helvetica',12),
                   icon=icon_path)

while True:
    event,values = window.read()
    print(event,values)
    filepath = values['files'].split(";")
    folder = values['folder']
    zip_creator.make_archive(filepath,folder)
    window["output"].update(value="Compression Complete")



window.close()
