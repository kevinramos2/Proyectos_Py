import pdfkit
import jinja2
from datetime import datetime

my_name = "Kevin Ramos"
item1 = "Tv"
item2 = "Mesa L"
item3 = "Air Fryer"
today_date = datetime.today().strftime("%d %b, %y")

context = {
  'my_name': my_name,
  'item1': item1,
  'item2': item2,
  'item3': item3,
  'today_date': today_date
}
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template ='plantilla.html'
template  = template_env.get_template(html_template)

template.render(context) 

pdfkit.configuration(wkhtmltopdf=)