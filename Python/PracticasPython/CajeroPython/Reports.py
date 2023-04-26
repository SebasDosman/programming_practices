from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Reports(object):
    def __init__(self, path_reports : str):
        self.path_reports = path_reports
    
    def generate_report(self, return_list1 : list, return_list2 : list, return_list3 : list):
        c = canvas.Canvas(self.path_reports, pagesize = letter)  
        
        c.setFont("Times-Roman", 12)
        c.setLineWidth(.3)
        
        c.drawString(70, 730, "----------------------------------------")
        c.drawString(70, 710, "Report from first document")
        c.drawString(70, 690, "----------------------------------------")
        c.drawString(70, 670, "Total: " + str(return_list1[0]))
        c.drawString(70, 650, "Total withdrawn: " + str(return_list1[1]))
        c.drawString(70, 630, "Total consignment: " + str(return_list1[2]))
        c.drawString(70, 610, "Total invalid withdrawal: " + str(return_list1[3]))
        c.drawString(70, 590, "----------------------------------------")
        
        c.drawString(70, 550, "----------------------------------------")
        c.drawString(70, 530, "Report from second document")
        c.drawString(70, 510, "----------------------------------------")
        c.drawString(70, 490, "Total: " + str(return_list2[0]))
        c.drawString(70, 470, "Total withdrawn: " + str(return_list2[1]))
        c.drawString(70, 450, "Total consignment: " + str(return_list2[2]))
        c.drawString(70, 430, "Total invalid withdrawal: " + str(return_list2[3]))
        c.drawString(70, 410, "----------------------------------------")
        
        c.drawString(70, 370, "----------------------------------------")
        c.drawString(70, 350, "Report from third document")
        c.drawString(70, 330, "----------------------------------------")
        c.drawString(70, 310, "Total: " + str(return_list3[0]))
        c.drawString(70, 290, "Total withdrawn: " + str(return_list3[1]))
        c.drawString(70, 270, "Total consignment: " + str(return_list3[2]))
        c.drawString(70, 250, "Total invalid withdrawal: " + str(return_list3[3]))
        c.drawString(70, 230, "----------------------------------------")

        c.save()