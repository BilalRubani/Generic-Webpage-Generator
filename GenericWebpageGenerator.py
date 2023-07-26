def createHTML():
    #Responsible For Creating the HTML File and Begins the HTML Boilerplate
    f = open("index.html", "w")
    f.write('<!DOCTYPE html>\n<html lang="en">\n\n<head>\n')
    f.write('\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    return f

def retrieveTitle(f):
    #Retrieves the Webpage's Title From the User
    title = input("What is the Title of Your Website?\n")
    f.write('\t<title>')
    f.write(title)
    f.write('</title>\n')
    return title

def retrieveIcon(f):
    #Retrieves an Icon for the Webpage from the User
    icon = input("Provide a Link to an Icon for Your Website:\n")
    f.write('\t<link rel="icon" href="')
    f.write(icon)
    f.write('">\n')
    return icon

def createCSS(f):
    #Creates the CSS File for the Webpage
    f.write('\t<link rel="stylesheet" href="style.css">\n</head>\n\n')
    c = open("style.css", "w")
    return c

def createHeader(f, icon, title):
    #Begins the Header Region of the HTML File
    f.write('<body>\n\t<header>\n\t\t<div class="header-region">\n\t\t\t')
    f.write('<div class="left-side">\n\t\t\t\t<p id="title">')
    f.write(title)
    f.write('</p>\n\t\t\t</div>\n\t\t\t<div class ="right-side">\n\t\t\t\t')

def createList(f):
    #Creates the Links Provided by the User
    num = int(input("How Many Links Would You Like to Include?\n"))
    if not num: return 

    f.write('<ul>')
    for i in range(num):
        link_title = input("Provide a Title For Your Link:\n")
        link = input("Provide the URL for the Link:\n")
        f.write('\n\t\t\t\t\t<li><a href="')
        f.write(link)
        f.write('">')
        f.write(link_title)
        f.write('</a></li>')
        if i == num - 1:
            f.write('\n\t\t\t\t</ul>\n\t\t\t')
        else:
            f.write('\t\t\t\t\t')
    f.write('</div>\n\t\t</div>\n\n\t\t')

def secondaryTextHeader(f):
    #Creates the Secondary Text Within the Header Region
    secondary = input("Provide the Secondary Text for Your Header:\n")
    f.write('<p class="secondary">')
    f.write(secondary)
    f.write('</p>\n\t\t\t')
    f.write('</div>\n\t\t\t')

def heroText(f):
    #Creates the Hero Text Within the Header
    hero = input("Provide the Hero Text for Your Header:\n")
    f.write('<h1 class="hero">')
    f.write(hero)
    f.write('</h1>\n\t\t\t\t')
    secondaryTextHeader(f)

def mainHeader(f):
    #Finishes off the Header Portion With the Image
    f.write('<div class="welcome">\n\t\t\t<div class="left-side">\n\t\t\t\t')
    heroText(f)
    f.write('<div class="right-side">\n\t\t\t\t<div class="image">\n\t\t\t\t\t')
    image_link = input("Provide a Link to Your Desired Image for the Main Header:\n")
    f.write('<img src="')
    f.write(image_link)
    f.write('">\n\t\t\t\t')
    f.write('</div>\n\t\t\t</div>\n\t\t</div>\n\t</header>\n\n')

def createCard(f):
    #Creates a Card for the Body Portion of the Webpage
    f.write('<div class="card">\n\t\t\t\t<div class="square">\n\t\t\t\t\t<img src="')
    card_image = input("Provide the Link for Your Card\'s Image:\n")
    f.write(card_image)
    f.write('">\n\t\t\t\t</div>\n\t\t\t\t')
    card_text = input("Provide Text for Your Card:\n")
    f.write('<p>')
    f.write(card_text)
    f.write('</p>')
    f.write('\n\t\t\t</div>')


def mainPage(f):
    #Begins the Body Portion Including the Creation of any Additional Cards
    f.write('\t<main>\n\t\t<h2>')
    body_title = input("Provide a Title for the Main Body of Your Page:\n")
    f.write(body_title)
    f.write('</h2>\n\t\t<div class="card-container">\n\t\t\t')
    createCard(f)
    repeat = int(input("How Many Additional Cards Would You Like?\n"))
    for _ in range(repeat):
        f.write('\n\t\t\t')
        createCard(f)
    f.write('\n\t\t</div>\n\t</main>\n\n\t')

def createQuote(f):
    #Creates the Quote Region of the Webpage
    f.write('<div class="quote">\n\t\t<em>"')
    quote = input("Provide a Quote for Your Webpage:\n")
    f.write(quote)
    f.write('"</em>\n\t\t<p>- ')
    author = input("Provide the Name of the Individual Who said Your Quote:\n")
    f.write(author)
    f.write('</p>\n\t</div>\n\n')

def createBanner(f):
    #Creates the Banner Portion of the Webpage
    f.write('\t<div class="banner">\n\t\t<div class="container">\n\t\t\t<div class="left-side">\n\t\t\t\t')
    f.write('<strong>')
    banner_text = input("Provide Main Text for Banner:\n")
    f.write(banner_text)
    f.write("</strong>\n\t\t\t\t")
    f.write('<p class="secondary">')
    s_text = input("Provide Secondary Text for Banner:\n")
    f.write(s_text)
    f.write('</p>\n\t\t\t</div>\n\t\t\t<div class="right-side">\n\t\t\t\t<div class="image2">\n\t\t\t\t\t')
    image_link = input("Provide a Link to Your Desired Image for the Banner:\n")
    f.write('<img src="')
    f.write(image_link)
    f.write('">\n\t\t\t\t')
    f.write('</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n')


def createFooter(f):
    #Creates the Footer of the Webpage
    f.write('\t<footer>\n\t\tCopyright &copy; ')
    copyright = input("Provide Your Copyright Text:\n")
    f.write(copyright)
    f.write('\n\t</footer>\n</body>\n\n</html>')

def setupHTML():
    #Calls all Functions In Order to Set Up the HTML Document
    index = createHTML()
    title = retrieveTitle(index)
    icon = retrieveIcon(index)
    style = createCSS(index)
    createHeader(index, icon, title)
    createList(index)
    mainHeader(index)
    mainPage(index)
    createQuote(index)
    createBanner(index)
    createFooter(index)

    index.close()

    return style

def generalPageSetup(style):
    #Styles All Elements of Page
    style.write('@import url(\'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap\');\n')
    style.write('* {\n\tmargin: 0;\n\tpadding: 0;\n}\n\n')
    style.write('body {\n\tfont-family: \'Roboto\', sans-serif;\n}\n\n')

def headerBackground(style):
    #Begins Styling Header
    style.write('header {\n\tbackground-color: ')
    header_color = input("Provide a Background Color For the Header in RGB, Hex, or Word Form:\n")
    style.write(header_color)
    style.write(';\n\tpadding: 1em, 13em;\n}\n\n')
    style.write('#title {\n\tfont-size: 24px;\n\tfont-weight: 900;\n\tcolor: ')
    header_title = input("Provide a Color for the Header Title in RGB, Hex, or Word Form:\n")
    style.write(header_title)
    style.write(';\n\tmargin: 20px;\n}\n\n')

def headerRegion(style):
    #Continues Styling Elements Within Header
    style.write('.header-region {\n\tdisplay: flex;\n\tjustify-content: space-between;\n\talign-items: baseline;\n}\n\n')
    style.write('.header-region ul {\n\tlist-style-type: none;\n\tdisplay: flex;\n\tgap: 1.5em;\n}\n\n')
    style.write('.secondary,\na:link {\n\tfont-size: 18px;\n\tcolor:')
    secondary_text_color = input("Provide a Color for the Secondary Text in RGB, Hex, or Word Form:\n")
    style.write(secondary_text_color)
    style.write(';\n\ttext-decoration: none;\n\tmargin-right: 20px;\n}\n\n')

def headerWelcome(style):
    #Styles the Header Welcome Portion
    style.write('.welcome {\n\tdisplay: flex;\n\tpadding: 7em 0;\n\tjustify-content: center;\n\talign-items: center;\n\tgap: 2em;\n}\n\n')
    style.write('.welcome .left-side {\n\tdisplay: flex;\n\tflex-direction: column;\n\tgap: 10px;\n\tmargin: 20px;\n}\n\n')
    style.write('.welcome .right-side {\n\tmargin-right: 20px;\n}\n\n')
    style.write('.hero {\n\tcolor:')
    hero_color = input("Provide a Color for the Hero Text of the Header in RGB, Hex, or Word Form:\n")
    style.write(hero_color)
    style.write(';\n\tfont-weight: 900;\n\tfont-size: 48px;\n}\n\n')

def headerImage(style):
    #Does all Styling For Header Image
    style.write('.image {\n\tdisplay:flex;\n\talign-items: center;\n\tjustify-content: center;\n\theight: 350px;\n\tborder-style: groove;\n\tborder-width: 30px;\n\tborder-color: ')
    border_color = input("Provide a Border Color for the Image of the Header in RGB, Hex, or Word Form:\n")
    style.write(border_color)
    style.write(';\n}\n\n')
    style.write('.image img {\n\theight: 350px;\n}\n\n')

def headerPortion(style):
    #Calls all Functionality To Style the Header Portion
    headerBackground(style)
    headerRegion(style)
    headerWelcome(style)
    headerImage(style)

def mainCard(style):
    #Styles the Cards' Main Container
    style.write('main {\n\tdisplay: flex;\n\tflex-direction: column;\n\talign-items: center;\n\tpadding: 0 13em;\n\tmargin-top: 3em;\n}\n\n')
    style.write('main h2 {\n\tfont-size: 36px;\n\tfont-weight: 900;\n\tcolor: ')
    h2_color = input("Provide a Color for the Header Text of the Information Portion in RGB, Hex, or Word Form:\n")
    style.write(h2_color)
    style.write(';\n}\n\n')
    return h2_color

def cardStyling(style):
    #Styles the Individual Cards
    style.write('.card-container {\n\tdisplay: flex;\n\tjustify-content: center;\n\talign-items: center;\n\tflex-wrap: wrap;\n\tmargin: 3em 0 6em 0;\n\tgap: 5em;\n}\n\n')
    style.write('.card {\n\ttext-align: center;\n\tmax-width: 200px;\n\tdisplay: flex;\n\tflex-direction: column;\n\talign-items: center;\n\tgap: .5em;\n}\n\n')
    style.write('.square {\n\tborder: 5px solid;\n\tborder-color: ')
    card_color = input("Provide a Border Color for the Cards in RGB, Hex, or Word Form:\n")
    style.write(card_color)
    style.write(';\n\tborder-style: ridge;\n\theight: 160px;\n}\n\n')
    style.write('.square img {\n\theight: 160px;\n}\n\n')


def cardPortion(style):
    #Calls All Functionality in Order to Style the Cards
    repeat_color = mainCard(style)
    cardStyling(style)
    return repeat_color

def quoteStyling(style, text_color):
    #Styles the Quote Section of the Webpage
    style.write('.quote {\n\tdisplay: flex;\n\tflex-direction: column;\n\tjustify-content: center;\n\tbackground-color: ')
    quote_background = input("Provide a Color for the Background Region of the Quote in RGB, Hex, or Word Form:\n")
    style.write(quote_background)
    style.write(';\n\tpadding: 7em 13em;\n}\n\n')
    style.write('.quote p {\n\talign-self: flex-end;\n\tfont-weight: bolder;\n\tfont-size: 24px; color: ')
    style.write(text_color)
    style.write(';\n}\n\n.quote em {\n\tfont-size: 36px;\n\tfont-weight: 100;\n\tcolor: ')
    style.write(text_color)
    style.write(';\n}\n\n')

def bannerStyling(style):
    #Styles the Banner Portion of the Webpage
    style.write('.banner {\n\tdisplay: flex;\n\tjustify-content: center;\n\talign-items: center;\n\tpadding: 5em 13em;\n}\n\n')
    style.write('.container {\n\tdisplay: flex;\n\tjustify-content: space-around;\n\talign-items: center;\n\tbackground-color: ')
    banner_background = input("Provide a Background Color for the Banner in RGB, Hex, or Word Form:\n")
    style.write(banner_background)
    style.write(';\n\tpadding: 3em;\n\twidth: 100%;\n\tborder-radius: 10px;\n}\n\n')
    style.write('strong {\n\tfont-size: 24px;\n\tcolor: #FFF;\n}\n\n')
    style.write('.image2 {\ndisplay: flex;\n\talign-items: center;\n\tjustify-content: center;\n\theight: 150px;\n\tborder-style: groove;\n\tborder-width: 20px;\n\tborder-color: ')
    border_color = input("Provide a Border Color for the Banner Image in RGB, Hex, or Word Form:\n")
    style.write(border_color)
    style.write(';\n}\n\n')
    style.write('.image2 img {\n\theight: 150px;\n}\n\n')

def footerStyling(style):
    #Styles the Footer Portion of the Webpage
    style.write('footer {\n\tbackground-color: ')
    footer_background = input("Provide a Background Color for the Footer in RGB, Hex, or Word Form:\n")
    style.write(footer_background)
    style.write(';\n\tcolor: #FFF;\n\tdisplay: flex;\n\tjustify-content: center;\n\talign-items: center;\n\tpadding: 2em 0;\n}\n')

def setupCSS(style):
    #Calls All CSS Styling Functions
    generalPageSetup(style)
    headerPortion(style)
    repeat_color = cardPortion(style)
    quoteStyling(style, repeat_color)
    bannerStyling(style)
    footerStyling(style)

    style.close()

def run():
    print('Welcome to the Generic Webpage Generator!\n')
    style = setupHTML()
    setupCSS(style)
     

run()
