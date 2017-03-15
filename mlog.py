#Graphical User Interface
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#Mine Log 
# import MineLog as ml
from MineLog import Equipment,ShiftFile,mload,oeeEquipmentPlot,oeeEquipmentPlot1,param_plot,param_multiple_plot,Moving_AveragePlot 

import os

cwd=os.getcwd()
filepath= os.path.join(cwd,'Equipment')

def get_Equipment_list():
    eq_filenames=[i for i in os.listdir(filepath) if i.endswith(".mlog")]

    eq_list=[]
    for i in eq_filenames:
        eq=mload(os.path.join(filepath,i))
        # NOTE:eq.update()
        eq_list.append(eq)
    return eq_list
def plot_Equipment(widget,builder):
    moving_bool=moving_ave_btn.get_active()
    interval=roll_mean_interval.get_value_as_int()
    params=[]
    if check_availability.get_active(): params.append("Availability")
    if check_utilization.get_active(): params.append("Utilization")
    if check_efficiency.get_active(): params.append("Efficiency")
    if check_oee.get_active(): params.append("OEE")
    x=eq_listbox.get_selected_rows()
    if x and params and not moving_bool and len(x)==1:
        oeeEquipmentPlot1(x[0].data,params)
    if moving_bool and x and params and interval>0:
        Moving_AveragePlot([t.data for t in x],params,interval=interval,marker='o')
def toggle_select_mode(widget,builder):
    mode={0:1,1:3}
    eq_listbox.set_selection_mode(mode[kind_plot.get_active()])
    print("this")
def delete_Equipment(widget,builder):
    x=eq_listbox.get_selected_row()
    if x:
        os.remove(os.path.join(filepath,x.data.Name+".mlog"))
        eq_listbox.remove(x)
        eq_listbox.show()
# Create New Equipment
def create_Neweq(w,builder):
    name=eq_title.get_text()
    if name != "":
        cwd=os.getcwd()
        filepath= os.path.join(cwd,'Equipment')
        new_eq=Equipment(name)
        new_eq.save(filepath)
        eq_listbox.add(ListBoxRowWithData(new_eq))
        eq_listbox.show_all()
        neweq_dialog.hide()
#Cancel New Equipment
def cancel_Neweq(w,builder):
    neweq_dialog.hide()
#Cancel Adding Shift
def cancel_Addshift(w,builder):
    addshift_dialog.hide()
def add_shift2Equipment(w,builder):
    file2add=shift_file_filechooserbutton1.get_filename()
    selected_equipment_4addshift = eq_listbox.get_selected_rows()
    try:
        if selected_equipment_4addshift[0].data.AddFile(file2add): print("File Added")
        selected_equipment_4addshift[0].data.update()
        selected_equipment_4addshift[0].data.save(filepath)
        # print(ShiftFile(file2add))
        # print(selected_equipment_4addshift[0].data.Data)
    except:
        # TODO: Error Message Dialog box for this
        print("ShiftFile not Added")

    addshift_dialog.hide()
# Open Add Shift Dialog
def add_shift2Equipment_open_dialog(w,builder):
    selected_equipment_4addshift = eq_listbox.get_selected_rows()
    shift_file_filechooserbutton1.unselect_all()
    temp= len(selected_equipment_4addshift)
    if temp!=1:
        messagedialog1.run()
        messagedialog1.hide()
    else:
        temp_sel_eq= builder.get_object("label4")
        temp_sel_eq.set_text("{0} is selected".format(selected_equipment_4addshift[0].data.Name))
        addshift_dialog.run()
        addshift_dialog.hide()
# Open New Equipment Dialog
def create_newEquipment(widget,builder):
    eq_title.set_text("")

    neweq_dialog.run()
    neweq_dialog.hide()

class Handler:
    def on_mainWindow_destroy(self, *args):
        Gtk.main_quit()

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data.Name))

builder = Gtk.Builder()
builder.add_from_file("mlog.glade")
builder.connect_signals(Handler())

window = builder.get_object("applicationwindow1")
window.connect('destroy',Gtk.main_quit)


#Equipment List Viewer
eq_listbox = builder.get_object("equipment_listbox")

#List of Equipment
eq_list=get_Equipment_list()

#Initialize list of Equipment to List Viewer
for i in eq_list:
    eq_listbox.add(ListBoxRowWithData(i))

#New Equipment button
new_equipment_btn = builder.get_object("new_equipment")
new_equipment_btn.connect("clicked",create_newEquipment,builder)


#New Equipment Dialog
neweq_dialog = builder.get_object("neweq_dialog")
eq_title=builder.get_object("equip_title_entry")

create_eq_btn=builder.get_object("create_eq_btn")
create_eq_btn.connect("clicked",create_Neweq,builder)

cancel_eq_btn=builder.get_object("cancel_create_btn")
cancel_eq_btn.connect("clicked",cancel_Neweq,builder)

# Add Shift button
add_shift_btn = builder.get_object("add_shift_btn")
add_shift_btn.connect("clicked",add_shift2Equipment_open_dialog,builder)

# Add Shift Dialog
messagedialog1 = builder.get_object("messagedialog1")
addshift_dialog = builder.get_object("addshift_dialog")
cancel_addshift_btn = builder.get_object("cancel_addshift_btn")
cancel_addshift_btn.connect("clicked",cancel_Addshift,builder)
add_shiftdialog_btn = builder.get_object("add_shiftdialog_btn")
add_shiftdialog_btn.connect("clicked",add_shift2Equipment,builder)
shift_file_filechooserbutton1 = builder.get_object("shift_file_filechooserbutton1")

#Delete Equipment Button
delete_equipment_btn = builder.get_object("delete_equipment")
delete_equipment_btn.connect("clicked",delete_Equipment,builder)


# Plotting
plot_btn= builder.get_object("plot_btn")
plot_btn.connect("clicked",plot_Equipment,builder)
moving_ave_btn=builder.get_object("moving_ave_btn")
check_availability=builder.get_object("check_availability")
check_utilization=builder.get_object("check_utilization")
check_efficiency=builder.get_object("check_efficiency")
roll_mean_interval=builder.get_object("roll_mean_interval")
check_oee=builder.get_object("check_oee")
kind_plot=builder.get_object("kind_plot")
kind_plot.connect("changed",toggle_select_mode,builder)


window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
