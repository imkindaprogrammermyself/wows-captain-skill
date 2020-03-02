from flask import Flask, send_file, abort, render_template
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

skill_list = [
    ["PT", "PM", "EL", "AS", "DCF", "IEB", "IFA", "LG"],
    ["HA", "JOAT", "EM", "TA", "SSE", "IE", "AR", "LS"],
    ["BOS", "SE", "TAE", "AA", "BFT", "SI", "DE", "VL"],
    ["MFCSA", "FP", "IFHE", "SS", "AFT", "MAAF", "RPF", "CE"]
]


def rounded_rectangle(w, h, r, color):
    rect = Image.new('RGBA', (w, h), color=color)
    corner = Image.new('RGBA', (r, r), color="#00000000")
    draw = ImageDraw.Draw(corner, mode="RGBA")
    draw.pieslice((0, 0, r * 2, r * 2), 180, 270, fill=color)
    rect.paste(corner, (0, 0))
    corner = corner.rotate(90)
    rect.paste(corner, (0, h - r))
    corner = corner.rotate(90)
    rect.paste(corner, (w - r, h - r))
    corner = corner.rotate(90)
    rect.paste(corner, (w - r, 0))
    return rect


def generate_skill_table(skills, border_size, corner_radius, icon_width, icon_height, icon_margin):
    table_width = icon_margin + ((icon_width + icon_margin) * 8)
    table_height = icon_margin + ((icon_height + icon_margin) * 4)
    icon_margin_right, icon_margin_top = icon_margin, icon_margin
    rect = rounded_rectangle(table_width, table_height, int(corner_radius / 2), "#0b344d")
    rect_larger = rounded_rectangle(table_width + border_size, table_height + border_size, corner_radius, "#ffff")
    ow, oh = rect.size
    nw, nh = rect_larger.size
    inner_x, inner_y = int(((nw - ow) / 2)), int(((nh - oh) / 2))
    for skill_tier in skill_list:
        for skill in skill_tier:
            icon = Image.open(format("static/img/%s.png" % skill))
            if skill not in skills:
                icon = icon.point(lambda p: p * 0.3)
            rect.paste(icon, (icon_margin_right, icon_margin_top), mask=icon)
            icon_margin_right += icon_width + icon_margin
        icon_margin_right = icon_margin
        icon_margin_top += icon_height + icon_margin
    rect_larger.paste(rect, (inner_x, inner_y), mask=rect)
    return rect_larger


# See Translator.py on how to generate the numbers
@app.route("/<int:a>,<int:b>,<int:c>,<int:d>")
def users(a, b, c, d):
    if a <= 255 | b <= 255 | c <= 255 | d <= 255:
        skills = [format(a, "08b"), format(b, "08b"), format(c, "08b"), format(d, "08b")]
        skills_used = [skill_list[s][i] for s, bits in enumerate(skills) for i, v in enumerate(bits) if v == "1"]
        output = io.BytesIO()
        rect = generate_skill_table(skills_used, 10, 10, 60, 60, 20)
        rect.save(output, "PNG")
        output.seek(0)
        return send_file(output, mimetype="image/png")
    else:
        abort(400)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    # app.run()
    app.run(host="0.0.0.0", port="80")
