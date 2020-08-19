from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import glob

for file in glob.glob("*.*"):
    name = file[:file.find(".")]
    endung = file[file.find(".")+1:]
    if endung == "svg":
        drawing = svg2rlg(file)
        renderPDF.drawToFile(drawing, "{}.pdf".format(name))
