from math import sin, cos, degrees, radians

from PIL import Image, ImageDraw, ImageFont
# (0, 0) is upper left corner
#
# Feature - accept pandas dataframes
# Feature - accept dictionary
# Feature - show values. Values should be bigger than labels.
#
# Refactoring - create function get_text_topleft_point(), which takes xy tuple,
# font, font size, and string, and spits out correct point to draw the text for
# it to be centerised on the starting point
#
# Feature - functionize the script
#
# Feature - freeze and package the script

# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
# sample = "Lorem ipsum dolor sit amet, partem periculis an duo, eum lorem paulo an, mazim feugiat lobortis sea ut. In est error eirmod vituperata, prima iudicabit rationibus mel et. Paulo accumsan ad sit, et modus assueverit eum. Quod homero adversarium vel ne, mel noster dolorum te, qui ea senserit argumentum complectitur. Duo at laudem explicari deterruisset, eu quo hinc mnesarchum. Vel autem insolens atomorum at, dolorum suavitate voluptatum duo ex."
# width, height = font.getsize(sample)

labels = ('Exp. Eff.', 'Impact', 'Variance')
values = (38, 17, 28)

SCALE = 6
POINTS = 3
STEPS_IN_GRID = 5
BG_COLOR = 'White'
LABEL_COLOR = (0, 0, 0, 200)

BASE_LENGTH = 100
BASE_SHAPE_LENGTH = 40
BASE_LABEL_SHIFT = 45
DOWNSAMPLING_FACTOR = 2

DEGREES_IN_A_CIRCLE = 360
DEGREES_TO_POINT_UP = 270

# make this a theme later on
SHAPE_COLOR = (135, 206, 250, 180)
LINE_COLOR = (15, 15, 15, 200)
OUTSIDE_COLOR = (0, 0, 0, 0)
LABEL_FONT = ImageFont.truetype("fonts/LemonMilk.otf", 3 * SCALE)
VALUE_FONT = ImageFont.truetype("fonts/LemonMilk.otf", 6 * SCALE)

points_to_shift = {
    3: 10,
    4: 0,
    5: 4,
    6: 0,
    7: 2,
    8: 0,
    9: 1,
    10: 0,
}

if POINTS < 3:
    raise ValueError('You need at least 3 points to make a 2d shape!')


def point_from_angle_distance(point, angle, distance):
    x, y = point
    x_factor = cos(radians(angle))
    y_factor = sin(radians(angle))
    new_point = (x + distance * x_factor, y + distance * y_factor)
    return new_point


# def shapify():

im = Image.new(
    'RGB', (BASE_LENGTH * SCALE, BASE_LENGTH * SCALE), color=BG_COLOR)
draw = ImageDraw.Draw(im, 'RGBA')

vertical_shift = points_to_shift[POINTS]
middle = ((BASE_LENGTH / 2) * SCALE,
          ((BASE_LENGTH / 2) + vertical_shift) * SCALE)
angle_step = DEGREES_IN_A_CIRCLE / POINTS

# draw gridlines
for step in range(1, STEPS_IN_GRID + 1):
    last_point = None
    for i in range(POINTS + 1):
        point = point_from_angle_distance(
            middle, DEGREES_TO_POINT_UP + i * angle_step,
            (BASE_SHAPE_LENGTH / STEPS_IN_GRID) * SCALE * step)
        draw.line((middle, point), fill=LINE_COLOR)
        if last_point and step == STEPS_IN_GRID:
            draw.line(
                (point, last_point), fill=LINE_COLOR, width=int(SCALE / 2))
        elif last_point:
            draw.line((point, last_point), fill=LINE_COLOR)
        last_point = point

# draw shape
points = []
for i, value in enumerate(values):
    points.append(
        point_from_angle_distance(middle, DEGREES_TO_POINT_UP + i * angle_step,
                                  value * SCALE))
    val_point = point_from_angle_distance(middle, 270 + i * angle_step,
                                          45 * SCALE)
    width, height = VALUE_FONT.getsize(str(value))
    val_point = val_point[0] - width / 2, val_point[1] - height / 2
    draw.text(val_point, str(value), font=VALUE_FONT, fill=(0, 0, 0, 200))
draw.polygon(points, outline=LINE_COLOR, fill=SHAPE_COLOR)
draw.line(points + [points[0]], fill=LINE_COLOR, width=int(SCALE / 2))

# draw labels
for i, label in enumerate(labels):
    top_left = point_from_angle_distance(
        middle, DEGREES_TO_POINT_UP + i * angle_step, BASE_LABEL_SHIFT * SCALE)
    shifted = top_left[0] - 12 * SCALE, top_left[1]
    draw.text(shifted, label, font=LABEL_FONT, fill=LABEL_COLOR)

del draw  # this somehow causes the opacity to work properly
# shrink image to implement anti-aliasing
im.thumbnail((SCALE * BASE_LENGTH / DOWNSAMPLING_FACTOR,
              SCALE * BASE_LENGTH / DOWNSAMPLING_FACTOR))  # yapf: disable
im.save('theshapeofyou.png', "PNG")
