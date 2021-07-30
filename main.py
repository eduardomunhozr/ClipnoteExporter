from get_configs import *
from make_vid import *
import tkinter as tk

selected = 0
list = os.listdir(Dir(''))
newList = []
thumb = []

clip = list[selected]

def listIterate():
    for item in range(len(list)):
        newItem = list[item].replace(',', '/', 2)
        newItem = newItem.replace(',', ':')
        newItem = newItem.replace(':', '    ', 1)
        newList.append(newItem)

listIterate()
print (list)

def saveGif():
    exportGif('{}'.format(clip), clip)

def listboxClick(event):
    global selected, clip
    selected = event.widget.curselection()[0]
    clip = list[selected]
    thumbView.config(image = thumb[selected])
    print(clip)

root = tk.Tk()

for item in range(len(list)):
    thumb.append(None)
    thumb[item] = (tk.PhotoImage(file = get_thumb(Dir(list[item]))))

print(get_thumb(Dir(clip)))
print(Dir(clip))

#labels
listbox = tk.Listbox(root, width = 40, height = 20)
scrollbar = tk.Scrollbar(root)
thumbView = tk.Label(root, image = thumb[0])
exportBtn = tk.Button(root, font = 'verdana 25', text = 'export', command = saveGif)


for i in range(len(newList)):
    listbox.insert(i, newList[i])

listbox.bind("<<ListboxSelect>>", listboxClick)

listbox.pack(side = 'left')
scrollbar.pack(side = 'left', fill = 'both')
thumbView.pack(side = 'top')
exportBtn.pack(side = 'bottom')


listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

filepath = os.path.dirname(__file__)

root.title('ClipNote Exporter')
root.iconbitmap('{}\\ClipnoteExporter.ico'.format(filepath))
root.mainloop()
