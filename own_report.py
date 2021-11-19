#https://pyfpdf.readthedocs.io/en/latest/index.html
#https://www.youtube.com/watch?v=UmN2_R4KEg8&list=PLFCB5Dp81iNVmuoGIqcT5oF4K-7kTI5vp&index=14
#https://towardsdatascience.com/covid-19-map-animation-with-python-in-5-minutes-2d6246c32e54

from fpdf import FPDF
from datetime import datetime, timedelta

#local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from helper import get_country_names, get_state_names, Mode
from time_series_analysis import plot_countries, plot_states
from create_case_maps import plot_global_case_map, plot_usa_case_map

width = 210
height = 297

#-------------------------------------------------
#PRACTICE
#-------------------------------------------------
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial','B',16)
# pdf.cell(40,10,"Hello World!")

# plot_daily_count_states(["New Hampshire","Massachusetts"], filename="own_report_test.png")
# pdf.image("own_report_test.png", 5, 40, (width-width/2)-5)
# #(5,40,(width-width/2)-5)=(x,y,width of the image)

# plot_daily_count_countries(["US", "India"], filename="own_report_test2.png")
# pdf.image("own_report_test2.png", (width/2)+5,40,(width-width/2)-5)

# states = ["New Hampshire","Massachusetts"]

# plot_daily_count_states(states, filename="own_report_test3.png")
# pdf.image("own_report_test3.png", 5, 30, (width-width/2)-5)
# plot_daily_count_states(states, mode = Mode.DEATHS, filename="own_report_test4.png")
# pdf.image("own_report_test4.png", (width/2)+5,30,(width-width/2)-5)

# plot_states(states, days = 7, filename="own_report_test5.png")
# pdf.image("own_report_test5.png", 5, 110, (width-width/2)-5)
# plot_states(states, days=7, mode=Mode.DEATHS, filename="own_report_test6.png")
# pdf.image("own_report_test6.png", (width/2)+5,110,(width-width/2)-5)

# pdf.output('own_report_tutorial.pdf','F')

# print(get_state_names())
# print(get_country_names())

#-------------------------------------------------
#-------------------------------------------------

def create_title(day, pdf):
    pdf.set_font('Arial','',24)
    pdf.ln(60)
    pdf.write(5, "Covid Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial','',16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_report(day, states, filename="own_report_tutorial.pdf"):
    
    pdf = FPDF()

    #--------------------------------------------------

    '''First Page'''

    pdf.add_page()

    pdf.image("own_report_letterhead.png",0,0,width)
    create_title(day, pdf)

    plot_usa_case_map("own_report_usa_cases.png", day=day)
    pdf.image("own_report_usa_cases.png",5,90,width-20)

    #--------------------------------------------------

    '''Second Page'''

    pdf.add_page()

    plot_daily_count_states(states, filename="own_report_test3.png")
    pdf.image("own_report_test3.png", 5, 30, (width-width/2)-5)
    plot_daily_count_states(states, mode = Mode.DEATHS, filename="own_report_test4.png")
    pdf.image("own_report_test4.png", (width/2)+5,30,(width-width/2)-5)

    plot_states(states, days = 7, filename="own_report_test5.png",end_date=day)
    pdf.image("own_report_test5.png", 5, 110, (width-width/2)-5)
    plot_states(states, days=7, mode=Mode.DEATHS, filename="own_report_test6.png")
    pdf.image("own_report_test6.png", (width/2)+5,110,(width-width/2)-5)

    #--------------------------------------------------

    pdf.output(filename, 'F')

if __name__ == '__main__':
    # day = (datetime.today() - timedelta(days=1)).strftime('%m/%d/%y').replace('/0','/').lstrip("0")
    ##replace because format 5/3/20 and not 10/03/20. lstrip, for 1st 0.
    ##errors out because site doesnt exist any more.
    day = '10/10/20'
    states = ["New Hampshire","Massachusetts"]
    create_report(day, states)