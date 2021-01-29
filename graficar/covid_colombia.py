"""
Este Script como reto del curso 
se graficara datos sobre el contagio del covid en colombia 
"""
import sqlite3 as sqlite 
from bokeh.io import output_file,show
from bokeh.models import tools
from bokeh.models.tools import Toolbar
from bokeh.plotting import figure


if __name__ == '__main__':
    #realizamos la conexion a la base de datos 
    con = sqlite.connect('colombia.sqlite')
    cur = con.cursor()

    #consulta para graficar 
    _sql = '''
        SELECT department.id, department.name, COUNT(*) cantidad
        FROM covid_colombia 
        INNER JOIN department on department.id = covid_colombia.id_department
        WHERE covid_colombia.id_recovered_status = 2 
        GROUP BY 1,2
        order by cantidad desc
        LIMIT 10;
    '''
    cur.execute(_sql)

    #variables para graficar 
    departments = list()
    deads = list()

    for  result in cur:
        print(result[0],result[1],result[2])

        departments.append(result[1])
        deads.append(result[2])

    
    #realizamos las operaciones para graficar 

    output_file('covid_colombia.html')
    fig = figure(x_range=departments, plot_height=550, plot_width =350,title='Top 10 Departamentos con + muertos por Covid',
                 toolbar_location=None, tools="")

    fig.vbar(x=departments,top=deads,width=0.8)

    fig.xgrid.grid_line_color = None
    fig.xaxis.major_label_orientation = 1
    fig.y_range.start = 0

    show(fig)