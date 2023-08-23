import textwrap
from PIL import Image, ImageFont, ImageDraw

base=Image.open("base_image.png")

def write_aligment(string):
    alig_fnt = ImageFont.truetype('AligFnt.ttf', 40)
    pos = [1090,312]
    # Measure the text area
    wi = alig_fnt. getmask(string).getbbox()[2]
    hi = 40
    # Copy the relevant area from the source image
    img = base.crop ((pos[0], pos[1], pos[0] + hi, pos[1] + wi))

    # Rotate it backwards
    img = img.rotate (270, expand = 1)

    # Print into the rotated area
    d = ImageDraw.Draw (img)
    d.text ((0, 0), string, font = alig_fnt, fill = (0, 0, 0))

    # Rotate it forward again
    img = img.rotate (90, expand = 1)

    # Insert it back into the source image
    # Note that we don't need a mask
    base.paste (img, pos)

write_aligment("Chaotic Good")

base_obj = ImageDraw.Draw(base)


def write_text(string, pos, max_height, max_legnth, fnt_name, underline=False):
    text_height = max_height
    while True:
        fnt = ImageFont.truetype(fnt_name, text_height)
        text_width = fnt.getmask(string).getbbox()[2]
        if text_width >= max_legnth:
            text_height = text_height-3
        else:
            break
    pos[0] = int(pos[0]+(max_legnth-text_width)/2)
    base_obj.text((pos[0],pos[1]), string, (255,255,255), font=fnt)
    if underline:
        base_obj.line((pos[0], pos[1]+text_height, pos[0]+text_width, pos[1]+text_height))


def write_name(name):
    write_text(name, [27,32], 60, 506, 'Lato-Regular.ttf', True)

def write_quote(quote):
    quote = quote.replace("\"","")
    write_text(f"\"{quote}\"",[45, 658], 41,1026, 'QuoteFnt.ttf' )

def write_academics(majors,minors):
    total = len(majors)+len(minors)
    if total == 1:
        pos = [602, 108]
        write_text(f"[{majors[0]}]", pos, 136,317, 'Lato-Italic.ttf')
    else:
        count  = 0
        diff = int(136/total)
        for major in majors:
            pos = [597-((diff/3)*count), 35+(diff*count)]
            write_text(f"[{major}]", pos, diff,307,'Lato-Italic.ttf')
            count += 1
        for minor in minors:
            pos = [597-((diff/3)*count), 35+(diff*count)]
            write_text(f"({minor})", pos, diff,307,'Lato-Italic.ttf')
            count += 1
    
def write_place(place):
    words = textwrap.wrap(place, width=10)
    # words = place.split(" ")
    total = len(words)
    count  = 0
    diff = int(136/total)
    for word in words:
        pos = [930-((diff/3)*count), 25+(diff*count)]
        write_text(word, pos, diff,230,'QuoteFnt.ttf')
        count += 1
            
write_name("Beatriz Rodriguez")
write_academics(["mathematics"],["computer science"])
write_place("oscuros del el balced")
write_quote("\"There is an abundance of soup and so of soup and soup\"")

base.show()
base.save("test.png")