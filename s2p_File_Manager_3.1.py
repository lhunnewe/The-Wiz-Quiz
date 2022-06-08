import os, csv,datetime, subprocess
import tkinter as tk
def main():
    listf = listfiles()
    listp = listprojects(listf) #Function to list all the projects once
    pcompile = ''
    pcomp = projectsSelect(listp, pcompile) #Select your project file 
    listpf = projectsFiles(pcomp,listf,listp) #return project files - Compiles all the project s2p files for conversion
    clearTerminal()
    convert_csv_q(listpf) #Question: Convert listpf to csv
    list_hdrs = convert_csv_hdrs(listpf)
    convert_csv_hdrs_post(list_hdrs,pcomp)
    convert_csv_data(pcomp,listpf)
    complete_q(pcomp)
def listfiles():#Compiling list of files
    listf = []
    os_chdir_data()
    fd = os.getcwd()
    for file in os.listdir(fd):
        listf.append(file)
    return listf
def listprojects(listf):#projects
    listf = listf
    listp = []
    os_chdir_data()
    fd = os.getcwd()
    for file in os.listdir(fd):
        listf.append(file)

    for file in listf:
        if file.endswith('s2p'):
            index = file.find('_')
            if index > 0:
                result = file[0:index] #Getting the project name in the listf 
                if result not in listp:
                    listp.append(result)
        elif file.startswith('FD'):
            index = file.find('_')
            if index > 0:
                result = file[0:index]
                if result not in listp:
                    listp.append(result)
    
    listbox.delete(0,tk.END) #Clears the list so if it's pressed a second time it's not duplicated.
    for i, p in enumerate(listp):
        listbox.insert(i,p)
    return listp
def projectsSelect(listp,pcompile):#Select the project you want to convert to csv
    listp = listp
    clearTerminal()
    if pcompile =='':
        c = 0
        for i in listp: #Count and list each project file for selection
            print(c,i)
            c+=1
        pmsg = 'Which project would you like to compile (input number): '
        pchoice = input(pmsg)
        pcompile = listp[int(pchoice)]
        #print(pcompile)
        return pcompile
def projectsFiles(pcomp,listf,listp): #List all project files, confirm csv creation
    listf = listf
    listp = listp
    pcomp = pcomp
    listpf = []
    #print('Project: ', pcomp)

    for file in listf:
        if file.endswith('s2p'): #.s2p file?
            index = file.find('_') #Gets index number of first underscore

            if index > 0: #is a s2p file and found an underscore in file name. if index = -1 then no underscore found
                result = file[0:index] #Getting the project name in the listf 
                if result == pcomp and file not in listpf:
                    listpf.append(file)
            elif file.startswith('FD'):
                index = file.find('_')
                if index > 0:
                    result = file[0:index]
                    if result not in listp:
                        listp.append(result)
    return listpf
def convert_csv_q(listpf):
    listpf = listpf
    c = 0
    for file in listpf:
        c += 1
        print (file)
    msg = 'Would you like to convert the above ' + str(c) + ' projects to a csv file? (y/n) '
    pchoice = input(msg)
    if pchoice == 'y':
        pass
    elif pchoice !='y':
        main()
def convert_csv_hdrs(listpf):
    os_chdir_data()
    listpf = listpf
    listhdrs = []

    d_frequency = False #boalean for if statement
    d_num = False #boalean for if statement
    for file in listpf:
        #print('File Open: ', file)
        txtfile = open(file,'r')
        lines = txtfile.readlines()
        for line in lines:
            if d_frequency == False:
                if line.startswith('!Frequency'):
                    list11 = list(line.split("   "))
                    list11 = list(line.split("  "))
                    d_frequency = True
        for line in lines:
            if d_num == False:
                if line.startswith('#'):
                    list21 = list(line.split("   "))
                    list21 = list(line.split("  "))
                    list21 = list(line.split(" "))
                    d_num = True
    txtfile.close

    listhdrs = []
    for i, item in enumerate (list11): #Clean list11, move to listhdrs
        if item !='':
            item = item.strip()
            listhdrs.append(item)

    for i, item in enumerate(list21): #strips \n off of the last index value
        item = item.strip('\n')
        list21[i] = item

    for i, item in enumerate(listhdrs): #Rename headers in listhdrs
        if i == 0: #Frequency
            listhdrs[i] = 'Fo (' + list21[1] + ')'
        elif i == 1:
            listhdrs[i] = list21[2] + '_' + item
        elif i == 2:
            listhdrs[i] = list21[2] + '_' + item
        elif i == 3:
            listhdrs[i] = list21[3] + '_' + item
        elif i == 4:
            listhdrs[i] = list21[3] + '_' + item
        elif i == 5:
            listhdrs[i] = list21[4] + '_' + item
        elif i == 6:
            listhdrs[i] = list21[4] + '_' + item
        elif i == 7:
            listhdrs[i] = list21[5] + '_' + item
        elif i == 8:
            listhdrs[i] = list21[5] + '_' + item
        
    listhdrs.append('file_name')
    listhdrs.append('config')
    listhdrs.append('date_ran')
    return listhdrs

    os_chdir_root()

    fd = os.getcwd()
    fd = fd+'/s2pFiles/'
    os.chdir(fd)
    #print (fd)
def convert_csv_hdrs_post(listhdrs, pcomp):
    listhdr = []
    listhdr = listhdrs
    csv_new = pcomp + ".csv"    

    os_chdir_csv()

    with open(csv_new, 'w') as csvfile: # Create a csv file in the spreadsheet folder
        csvwriter = csv.writer(csvfile,lineterminator = '\n')
        #csvwriter.writerow(['H1','H2','H3','H4','H5','H6','H7','H8','H9'])
        csvwriter.writerow(listhdr)
    csvfile.close()
def os_chdir_root(): #changes cwd to the root directory
    fd = os.getcwd()
    fdbool = fd.endswith('s2pFileManipulator')
    if fdbool == False:
        while fdbool is False:
            os.chdir('../')
            fd = os.getcwd()
            fdbool = fd.endswith('s2pFileManipulator')
def os_chdir_csv():
    os_chdir_root()

    fd = os.getcwd()
    fd = fd+'/spreadsheets/LeRoy/'
    os.chdir(fd)
    #print (fd)
def os_chdir_data():
    os_chdir_root()

    fd = os.getcwd()
    fd = fd+'/s2pFiles/'
    os.chdir(fd)
    #print (fd)
def convert_csv_data(pcomp,listpf):
    listpf = listpf
    csv_export = pcomp + '.csv'
    for file in listpf:
        os_chdir_data()
        data = False
        txtfile = open(file,'r')
        lines = txtfile.readlines()
        for i, line in enumerate(lines):
            if data == True:
                print (i, line)
                lnsplit = line.split()
                lnsplit.append(file)
                lnsplit.append(config)
                ts = datetime.datetime.now()
                lnsplit.append(ts)
                os_chdir_csv()
                with open(csv_export,'a') as csvfile:
                    csvwriter = csv.writer(csvfile,lineterminator = '\n')
                    csvwriter.writerow(lnsplit)
            elif line.startswith('!Frequency'):
                data = True
                #print(i,data)
            elif line.startswith('#'):
                config = line.strip()
                #print(i,config)
def complete_q(pcomp):
    msg = 'File Conversion complete!'
    print(msg)
def clearTerminal(): #Clears windows terminal from prior print screens
    for x in range(10):
        print(' ')
def CurSelet(event):
    widget = event.widget
    selection=widget.curselection()
    global picked
    picked = widget.get(selection[0])
    print(picked)

    listf = listfiles()
    listp = listprojects(listf) #Function to list all the projects once
    pcomp = picked
    listpf = projectsFiles(pcomp,listf,listp) #return project files - Compiles all the project s2p files for conversion
    #for f in listpf:
    pf_listbox.delete(0,tk.END) #Clears the list so if it's pressed a second time it's not duplicated.
    for i, p in enumerate(listpf):
        pf_listbox.insert(i,p)
    return listpf, picked
def ButtonSubmit():    
    print('Converting file(s) to csv')
    listf = listfiles()
    listp = listprojects(listf) #Function to list all the projects once
    pcomp = picked #NEED TO FIGURE OUT HOW TO DERIVE THIS FROM THE CURSET
    listpf = projectsFiles(pcomp,listf,listp) #return project files - Compiles all the project s2p files for conversion
    
    listhdrs = convert_csv_hdrs(listpf)
    convert_csv_hdrs_post(listhdrs, pcomp)
    convert_csv_data(pcomp,listpf)
    complete_q(pcomp)
#https://realpython.com/python-gui-tkinter/#adding-a-widget
#https://www.youtube.com/watch?v=D8-snVfekto


root = tk.Tk() #root app that the canvas and frames are in
root.title('s2P File Manager') #Titles the root app
height = 500 #Height of the canvas
width = 600 #Width of the canvas

canvas = tk.Canvas(root,height=height,width=width) #Declaring the height/width of canvas
canvas.pack() #Packing the canvas

bg_image = tk.PhotoImage(file='bg01.png') #Declaring variable as image location
bg_label = tk.Label(root,image=bg_image) #Assigning image to a label that is mapped to the root
bg_label.place(relwid=1,relheight=1) #Placing the label to 100% of the canvas

frame_hdr = tk.Frame(root,bg='gray',bd=5) #Creating a Frame for the header
frame_hdr.place(relx=0.0,rely=0.01,relwidth=1.0,relheight=0.1) #Placement of Frame, xy are defaulted to NW of the grid

label_hdr=tk.Label(frame_hdr,text='S2P File Manager',font=('courier',18))#Label that goes inside the header with Text
label_hdr.place(relx=0.00,rely=0,relwidth=1.0,relheight=0.95)#xy and relative width and height to the frame

#frame_p
frame_p=tk.Frame(root,bg='gray',bd=5)
frame_p.place(relx=0.05,rely=0.15,relwidth=0.40,relheight=.75)

#frame_pf
frame_pf=tk.Frame(root,bg='gray',bd=5)
frame_pf.place(relx=0.50,rely=0.15,relwidth=0.45,relheight=.75)


listf = []
button_proj=tk.Button(frame_p,font=('courier',10),text='Press to Scan Projects',relief= 'groove', command=lambda: listprojects(listf))
button_proj.place(relx=0.0,rely=0,relwidth=1.0,relheight=0.10)

#https://coderslegacy.com/python/list-of-tkinter-widgets/
#global listbox
listbox = tk.Listbox(frame_p) #Creating a listbox in the project frame
listbox.bind('<<ListboxSelect>>',CurSelet)#Upon clicking, stores selected value RESEARCH THIS!
listbox.place(relx=0,rely=0.15,relwidth=1.0,relheight=0.70)#xy placement of listbox

pf_hdr=tk.Label(frame_pf,text='Project Conversion Files',font=('courier',12))#Label header for conversion files
pf_hdr.place(relx=0.00,rely=0.00,relwidth=1.0,relheight=0.1)

#global pf_listbox
pf_listbox = tk.Listbox(frame_pf) #Listbox for showing the list of project files
pf_listbox.place(relx=0,rely=0.15,relwidth=1.0,relheight=.70)

button_submit=tk.Button(frame_pf,font=('courier',10),text='Convert Files',relief= 'groove',command=lambda: ButtonSubmit())
button_submit.place(relx=0.0,rely=0.90,relwidth=1.0,relheight=0.10)

root.mainloop()#Continous loop for the app


#main()