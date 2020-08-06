"""
__filename__ = "enhancedwebpage.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""
from datetime import datetime
from flask import Flask, request
from pytz import timezone

APP = Flask(__name__)

# Index
@APP.route('/enhancedwebpage', methods=['GET', 'POST'])
def index():
    """
    Webpage Index
    """
    content = webhead()
    content += webh1('The Best Breath Mints Of All Time')
    content += mainimg()
    content += webh2('Altoids')
    content += paragraph1()
    content += unordlist()
    content += webh3('Tic Tacs')
    content += paragraph2()
    content += ordlist()
    content += currenttime()
    content += webh4('Other Quality Breathmints')
    content += table()
    content += webh5('Quick Survey!')
    content += form()

    # Writing Form data to a file
    with open('Week7Deliverables/form-data.txt', mode='a') as formdata:
        formdata.write('\nQuick Survey Results:\n')
        formdata.write('How many breathmints do you consume per day?: ' +
                       request.form['answer1'] + '\n')
        formdata.write('Do you carry breathmints around with you regularly?: ' +
                       request.form['answer2'] + '\n')
        formdata.write('In which situations do you like to use breathmints? How '
                       'often do they occur? Do the breathmints help?: ' +
                       request.form['answer3'] + '\n')
        formdata.write('Select your favorite mint: ' + request.form['fave'] + '\n')

    content += webend()
    return content

# Head
def webhead():
    """
    Webpage Head
    """
    head_data = '<!--Head and Title-->'
    head_data += '<!DOCTYPE html> '
    head_data += '<html>'
    head_data += '<head> '
    head_data += '<title>The Best Breath Mints</title>'
    head_data += '</head>'
    head_data += '<body>'
    return head_data

# Heading 1
def webh1(string):
    """
    Webpage Heading 1
    """
    heading_string = '<H1 style="font-family: Verdana, sans-serif;">' + string + '</H1>'
    return heading_string

# Main Images
def mainimg():
    """
    Top Webpage Images
    """
    img_data = '<!--Images under Header-->'
    img_data += '<div>'
    img_data += '<img src="/static/altoids-pic-2.jpg">'
    img_data += '<img src="/static/tic-tacs-pic-2.jpg">'
    img_data += '</div>'
    return img_data

# Heading 2
def webh2(string):
    """
    Webpage Heading 2
    """
    heading_string = '<H2 style="font-family: Lucida Console, monospace;">' + string + '</H2>'
    return heading_string

# Paragraph + Image under Heading 2
def paragraph1():
    """
    Webpage Paragraph and Image under Heading 2
    """
    para_data = '<!--Content for Altoids Heading-->'
    para_data += '<div><img src="/static/altoids-pic-1.jpg"></div>'
    para_data += '<p>'
    para_data += 'Altoids - the Curiously Strong Mints! They were first made in '
    para_data += '1780 and have stayed in the same distinctive tin cases for '
    para_data += 'centuries. Their sharp taste of peppermint wipes bad breath out'
    para_data += ' in an instant. Places you can buy it:'
    para_data += '</p>'
    return para_data

# Unordered List under Heading 2
def unordlist():
    """
    Webpage Unordered List under Heading 2
    """
    ul_data = '<ul>'
    ul_data += '<li>Target</li>'
    ul_data += '<li>7-eleven</li>'
    ul_data += '<li>Costco</li>'
    ul_data += '<li><a href="https://productcentral.mars.com/altoids">'
    ul_data += 'Altoids Official Website</a></li>'
    ul_data += '</ul>'
    return ul_data

# Heading 3
def webh3(string):
    """
    Webpage Heading 3
    """
    heading_string = '<H3 style="font-family: Lucida Console, monospace;">' + string + '</H3>'
    return heading_string

# Paragraph + Image under Heading 3
def paragraph2():
    """
    Webpage Paragraph and Image under Heading 3
    """
    para_data = '<!--Contents for Tic Tac Heading-->'
    para_data += '<div><img src="/static/tic-tacs-pic-1.jpg"></div>'
    para_data += '<p>'
    para_data += 'Tic Tacs! These smaller, smoother candies come in dozens of '
    para_data += 'different flavors, including Peppermint, Orange, Spearmint, and '
    para_data += 'Wintergreen. They were first created in 1968 and have spread to '
    para_data += 'over 100 countries. They knock out bad breath in minutes. '
    para_data += 'Places you can buy it:'
    para_data += '</p>'
    return para_data

# Ordered List under Heading 3
def ordlist():
    """
    Webpage Ordered List under Heading 3
    """
    ol_data = '<ol>'
    ol_data += '<li>Walmart</li>'
    ol_data += '<li>Shoppers</li>'
    ol_data += '<li><a href="https://www.amazon.com/s?k=tic+tacs&i=grocery&ref=nb_sb_noss_2>">'
    ol_data += 'Amazon</a></li>'
    ol_data += '<li><a href="https://www.tictac.com/us/en/">'
    ol_data += 'Tic Tacs Official Website</a></li>'
    ol_data += '</ol>'
    return ol_data

# Current Time
def currenttime():
    """
    Webpage Current Time EST
    """
    eastern = timezone('US/Eastern')
    rightnow = datetime.now(eastern)
    current_time = rightnow.strftime('%H:%M:%S')
    para_data = '<!--Getting Current Time (EST)-->'
    para_data += '<p>'
    para_data += 'The current time (EST) is: ' + current_time
    para_data += '</p>'
    return para_data

# Heading 4
def webh4(string):
    """
    Webpage Heading 4
    """
    heading_string = '<H4 style="font-family: Lucida Console, monospace;">' + string + '</H4>'
    return heading_string

# Table
def table():
    """
    Webpage Table
    """
    table_data = '<!--Creating Table-->'
    table_data += '<table border="1">'
    table_data += '<tr><th>Eclipse</th>'
    table_data += '<th>Trident</th>'
    table_data += '<th>Ice Breakers</th></tr>'
    table_data += '<tr><th>Orbit</th>'
    table_data += '<th>Breath Savers</th>'
    table_data += '<th>Spry</th></tr>'
    table_data += '<tr><th>Mentos</th>'
    table_data += '<th>4ever</th>'
    table_data += '<th>Starbucks Mints</th></tr>'
    table_data += '<tr><th>Life Savers</th>'
    table_data += '<th>VerMints</th>'
    table_data += '<th>PUR</th></tr>'
    table_data += '</table>'
    return table_data

# Heading 5
def webh5(string):
    """
    Webpage Heading 5
    """
    heading_string = '<H5 style="font-family: Lucida Console, monospace;">' + string + '</H5>'
    return heading_string

# Form
def form():
    """
    Webpage Form
    """
    form_data = '<!--Creating Form-->'
    form_data += '<form method="POST">'
    form_data += '<div><label for="answer1">How many breathmints do you consume per day?'
    form_data += '</label> <input type="text" name="answer1"></div>'
    form_data += '<div><label for="answer2">Do you carry breathmints around with you regularly?'
    form_data += '</label> <input type="text" name="answer2"></div>'
    form_data += '<div><label for="answer3">In which situations do you like to use breathmints?'
    form_data += ' How often do they occur? Do the breathmints help?</label></div>'
    form_data += '<div><textarea name="answer3" rows="6" cols="40"></textarea></div>'
    form_data += '<div><label for="answer4">Select your favorite mint: </label>'
    form_data += '<select name="fave"><option value="Altoids">Altoids</option>'
    form_data += '<option value="Tic Tacs">Tic Tacs</option>'
    form_data += '<option value="Eclipse">Eclipse</option>'
    form_data += '<option value="Trident">Trident</option>'
    form_data += '<option value="Ice Breakers">Ice Breakers</option>'
    form_data += '<option value="Orbit">Orbit</option>'
    form_data += '<option value="Breath Savers">Breath Savers</option>'
    form_data += '<option value="Spry">Spry</option>'
    form_data += '<option value="Mentos">Mentos</option>'
    form_data += '<option value="4ever">4ever</option>'
    form_data += '<option value="Starbucks Mints">Starbucks Mints</option>'
    form_data += '<option value="Life Savers">Life Savers</option>'
    form_data += '<option value="VerMint">VerMint</option>'
    form_data += '<option value="PUR">PUR</option>'
    form_data += '<option value="Other">Other...</option></select></div>'
    form_data += '<div><input type="reset" value="Clear Form"></div>'
    form_data += '<div><input type="submit" value="Submit Answers"></div></form>'
    return form_data

# End
def webend():
    """
    Webpage End
    """
    end_data = '</body>'
    end_data += '</html>'
    return end_data

APP.run(host='0.0.0.0', port=8080)
