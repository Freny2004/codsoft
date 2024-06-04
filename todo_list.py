  
import tkinter as tk                   
from tkinter import ttk                
from tkinter import messagebox         
import sqlite3 as sql              
    
# function to create tasks 
def create_task():  
    
    task_str = task_field.get()   
    if len(task_str) == 0:   
        messagebox.showinfo('Please check your field...')  
    else:  
        tasks.append(task_str)  
        
       # the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        
        list_update()  
       
        task_field.delete(0, 'end')  
  
  
  
#  function to update the list  
def list_update():  
    clear_list()  
    for task in tasks:  

        task_listbox.insert('end', task)  
  
#  function to delete a task from the list  
def delete_task():  
    try:  
      
        the_value = task_listbox.get(task_listbox.curselection())  
        
        if the_value in tasks:  
           
            tasks.remove(the_value)  
          
            list_update()  
          
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
    
        messagebox.showinfo('You Cannot Delete Becaue No Item Selected.')        
  

# function to clear the list  
def clear_list():  

    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():   
    print(tasks)  
 
    guiWindow.destroy()  
  
def view_task():
    print("\nTasks:")
    for i, task in tasks(tasks, start=1):
        print(f"{i}. {task}")
  
# main function  
if __name__ == "__main__":  
  
    guiWindow = tk.Tk()  
   
    guiWindow.title("To-Do List")  

    guiWindow.geometry("500x450+750+250")  
    
    guiWindow.resizable(0, 0)  
  
    guiWindow.configure(bg = "lightblue")  
  
   
    the_connection = sql.connect('listOfTasks.db')  
    
    the_cursor = the_connection.cursor()  
 
    the_cursor.execute('create table if not exists tasks (title text)')  
 
    tasks = []  
 
    header_frame = tk.Frame(guiWindow, bg = "#D7FAEB")  
    functions_frame = tk.Frame(guiWindow, bg = "#D7FAEB")  
    listbox_frame = tk.Frame(guiWindow, bg = "#D7FAEB")  
   
  
    
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
       
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Times", "30"),  
        background = "#D7FAEB",  
        foreground = "#000000"  
    )  

    header_label.pack(padx = 20, pady = 20)  
  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task Description:",  
        font = ("Consolas", "11", "bold"),  
        background = "#D7FAEB",  
        foreground = "#000000"  
    )  

    task_label.place(x = 30, y = 40)  
      

    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
 
    task_field.place(x = 30, y = 80)  
  
    create_button = ttk.Button(  
        functions_frame,  
        text = "Create Task",  
        width = 24,  
        command = create_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    view_button = ttk.Button(  
        functions_frame,  
        text = "View Task",  
        width = 24,  
        command = view_task  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
  
    create_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    view_button.place(x = 30, y = 200)
    exit_button.place(x = 30, y = 240)  
  

    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
 
    task_listbox.place(x = 10, y = 20)  
  
    list_update()  

    guiWindow.mainloop()  
 
    the_connection.commit()  
