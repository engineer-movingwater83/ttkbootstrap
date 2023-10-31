import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

root = ttk.Window(themename='superhero')
colors = root.style.colors

#print(colors)

columns = [
    {'text':'LicenseNumber', 'stretch': False},
    {'text':'CompanyName', 'stretch': False},
    {'text':'UserCount', 'stretch': False},
]

row_data = [
    ('A123', 'IzzyCo', 12),
    ('A126', 'MovingWaterCo', 45),
    ('A158', 'FarCo', 36),
]

table = Tableview(master=root, 
                  coldata=columns, 
                  rowdata = row_data,
                  paginated=True,
                  autofit=False,
                  searchable=True,
                  bootstyle=PRIMARY,
                  stripecolor=(colors.light, 'green')
                  )

table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

table.insert_row('end', ['Marzale LLC', 26])
table.load_table_data()

rows = table.tablerows

print(rows[1].values)

root.mainloop()