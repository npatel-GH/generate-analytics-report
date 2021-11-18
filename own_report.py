#https://pyfpdf.readthedocs.io/en/latest/index.html


from fpdf import FPDF

#local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries

width = 210
height = 297

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(40,10,"Hello World!")

plot_daily_count_states(["New Hampshire","Massachusetts"], filename="own_report_test.png")
pdf.image("own_report_test.png", 5, 40, (width-width/2)-5)
#(5,40,(width-width/2)-5)=(x,y,width of the image)

plot_daily_count_countries(["US", "India"], filename="own_report_test2.png")
pdf.image("own_report_test2.png", (width/2)+5,40,(width-width/2)-5)

pdf.output('own_report_tutorial.pdf','F')

#Start at 19 mins