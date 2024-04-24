from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_problem_pdf(problem_name , problem_statement , input_format , output_format , testcases , explanation):
    
    print(problem_name)
    print(problem_statement)
    print(input_format)
    print(output_format)
    print(testcases)
    
    c = canvas.Canvas("media\\problem_pdfs\\problem.pdf", pagesize=letter)
    # max_page_height = 800
    font_name = "mooli"
    pdfmetrics.registerFont(TTFont(font_name, "G:\\SEM-7\\ADF\\FINAL PROJECT\\Mooli-Regular.ttf"))

    page_margin = 50
    section_margin = 30
    font_size = 12
    font_size_heading = font_size + 3
    # font_name = "Helvetica"
    font_name_bold = font_name
    line_height = font_size + 12
    width, height = letter
    y = height - page_margin  # Starting y-coordinate
    
    def drawPageBorder() :
        gap = 20
        top_left = (gap , height - gap)
        top_right = (width - gap , height - gap)
        bottom_left = (gap , gap)
        bottom_right = (width - gap , gap)
        
        c.line(top_left[0] , top_left[1] , bottom_left[0] , bottom_left[1])
        c.line(top_right[0] , top_right[1] , bottom_right[0] , bottom_right[1])
        c.line(top_left[0] , top_left[1] , top_right[0] , top_right[1])
        c.line(bottom_left[0] , bottom_left[1] , bottom_right[0] , bottom_right[1])
        
    drawPageBorder()
    
    def centerPrint(content , position) :
        line = content
        c.setFont(font_name_bold , font_size_heading)
        while c.stringWidth(line , fontName=font_name_bold , fontSize=font_size_heading) < width - 2 * page_margin :
            line = " " + line + " "
        c.drawString(page_margin , position , line)
        return position
            
    y = centerPrint(problem_name , y)
    
    y -= line_height
    y -= section_margin
    
    
    def printHeading(heading , position) :
        c.setFont(font_name_bold , font_size_heading)
        c.drawString(page_margin , position , heading)
        return position
        
    def printContent(content , position) :
        y = position
        sub = 0
        c.setFont(font_name , font_size)
        pdf_content = []
    
        line = ""
        temp = content.split('\n')
        for each in temp : 
            tokens = each.split(" ")
            for token in tokens :
                if c.stringWidth(line + token , fontName=font_name , fontSize=font_size) >= width - 2 * page_margin :
                    # spaces = ""
                    prevIndex = 0
                    while c.stringWidth(line , fontName=font_name , fontSize=font_size) < width - 2 * page_margin :
                        found = False
                        for index in range(prevIndex + 1 , len(line)) :
                            if line[index] == " " and line[index - 1] != " " :
                                line = line[:index + 1] + " " + line[index + 1:]
                                prevIndex = index + 1
                                found = True
                                break
                        
                        if found == False :
                            for index in range(0 , len(line)) :
                                if line[index] == " " and line[index - 1] != " " :
                                    line = line[:index + 1] + " " + line[index + 1:]
                                    prevIndex = index + 1
                                    found = True
                                    break
                        
                        if found == False : 
                            break
                    pdf_content.append(line)
                    line = token + " "
                else :
                    line += token + " "
        
        pdf_content.append(line)
        
        for line in pdf_content : 
            c.drawString(page_margin , y , line)
            y -= line_height
            if y < page_margin + 10 :
                c.showPage()
                drawPageBorder()
                y = height - page_margin
                
            sub += line_height
        
        return y
        
    def printSection(heading , content , position) :
        sub_position = 0
        position = printHeading(heading , position)
        
        position -= 10
        c.line(page_margin , position , page_margin + width - 2 * page_margin , position)
        position -= line_height
        
        if len(content) == 0 :
            return position
        
        position = printContent(content , position)
        
        return position
    
    y = printSection("Problem Statement" , problem_statement , y)
    y -= section_margin
    y = printSection("Input Format" , input_format , y)
    y -= section_margin
    y = printSection("Output Format" , output_format , y)
    y -= section_margin
    y = printSection("Testcases" , "" , y)
    
    def printTestCase(input , output , y) :
        sub_margin = 10
        
        c.setFont(font_name , font_size)
        
        if y - max(len(input.split('\n')) , len(output.split('\n'))) * line_height * 2 - line_height * 2 - sub_margin < 0 :
            c.showPage()
            drawPageBorder()
            y = height - page_margin
            y = printTestCase(input , output , y)
            return y
        
        top_left = (page_margin , y)
        top_right = (width - page_margin , y)
        top_middle = ((top_left[0] + top_right[0]) // 2 , y)
        
        c.line(top_left[0] , top_left[1] , top_right[0] , top_right[1])
        
        y -= line_height
        
        input_left = top_left[0] + sub_margin
        output_left = top_middle[0] + sub_margin
        
        c.drawString(input_left , y , "Input")
        c.drawString(output_left , y , "Output")
        
        y -= sub_margin
        c.line(top_left[0] , y , top_right[0] , y)
        
        y -= line_height
        
        input_y = y
        output_y = y
        
        
        
        for input_line in input.split('\n') :
            c.drawString(input_left , input_y , input_line)
            input_y -= line_height
            
        for output_line in output.split('\n') :
            c.drawString(output_left , output_y , output_line)
            output_y -= line_height
        
        y = min(input_y , output_y)
        c.line(top_middle[0] , top_middle[1] , top_middle[0] , y)
        c.line(top_right[0] , top_right[1] , top_right[0] , y)
        c.line(top_left[0] , top_left[1] , top_left[0] , y)
        c.line(top_left[0] , y , top_right[0] , y)
        
        
        return y
    
    for testcase in testcases :
        input , output = map(str , testcase)    
        y = printTestCase(input , output , y)
        y -= 10
    
    y -= section_margin
    
    y = printSection("Explnation" , explanation , y)
    
    c.save()
    
problem_name = "Problem Name"
problem_statement = """You are given a and b. Find the summation of a and b.""" * 2

input_format = """
Single line consisting of two numbers a and b.
"""

output_format = """
print a + b.
"""

testcases = [
    (12323 , "fdgfdgd"),
    (323232 , "fdfd")
]
