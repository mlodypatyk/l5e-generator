from os import confstr_names
import pickle
from PIL import Image, ImageDraw
colors = {
    'r': (255, 0, 0),
    'g': (0, 255, 0),
    'b': (0, 0, 255),
    'y': (255, 255, 0)
}

def drawTriangle(draw, topX, topY, color, multiplier):
    draw.polygon([(topX, topY), (topX-20, topY+35*(multiplier)), (topX+20, topY+(35*multiplier))], fill = colors[color])
    draw.line((topX, topY, topX-20, topY+35*(multiplier)), fill=(0, 0, 0))
    draw.line((topX, topY, topX+20, topY+35*(multiplier)), fill=(0, 0, 0))
    draw.line((topX+20, topY+35*(multiplier), topX-20, topY+35*(multiplier)), fill=(0, 0, 0))
def generateImage(cubestate, filename):
    # triangle height = 35
    # triangle base = 40
    im = Image.new('RGB', (360, 208))
    draw = ImageDraw.Draw(im)
    draw.polygon([(0,0), (0,208), (360, 208), (360, 0)], fill = (255, 255, 255))
    # f
    drawTriangle(draw, 180, 0, 'g', 1)

    drawTriangle(draw, 160, 35, cubestate[0], 1)
    drawTriangle(draw, 180, 70, cubestate[1], -1)
    drawTriangle(draw, 200, 35, cubestate[2], 1)

    drawTriangle(draw, 140, 70, 'g', 1)
    drawTriangle(draw, 160, 105, cubestate[3], -1)
    drawTriangle(draw, 180, 70, cubestate[4], 1)
    drawTriangle(draw, 200, 105, cubestate[5], -1)
    drawTriangle(draw, 220, 70, 'g', 1)
    # r
    drawTriangle(draw, 180+120, 0, 'b', 1)

    drawTriangle(draw, 160+120, 35, cubestate[6], 1)
    drawTriangle(draw, 180+120, 70, cubestate[7], -1)
    drawTriangle(draw, 200+120, 35, cubestate[8], 1)

    drawTriangle(draw, 140+120, 70, 'b', 1)
    drawTriangle(draw, 160+120, 105, cubestate[9], -1)
    drawTriangle(draw, 180+120, 70, cubestate[10], 1)
    drawTriangle(draw, 200+120, 105, cubestate[11], -1)
    drawTriangle(draw, 220+120, 70, 'b', 1)
    # l
    drawTriangle(draw, 180-120, 0, 'r', 1)

    drawTriangle(draw, 160-120, 35, cubestate[12], 1)
    drawTriangle(draw, 180-120, 70, cubestate[13], -1)
    drawTriangle(draw, 200-120, 35, cubestate[14], 1)

    drawTriangle(draw, 140-120, 70, 'r', 1)
    drawTriangle(draw, 160-120, 105, cubestate[15], -1)
    drawTriangle(draw, 180-120, 70, cubestate[16], 1)
    drawTriangle(draw, 200-120, 105, cubestate[17], -1)
    drawTriangle(draw, 220-120, 70, 'r', 1)
    # d
    drawTriangle(draw, 140, 140, 'y', -1)
    drawTriangle(draw, 160, 105, cubestate[18], 1)
    drawTriangle(draw, 180, 140, cubestate[19], -1)
    drawTriangle(draw, 200, 105, cubestate[20], 1)
    drawTriangle(draw, 220, 140, 'y', -1)
    
    drawTriangle(draw, 160, 175, cubestate[21], -1)
    drawTriangle(draw, 180, 140, cubestate[22], 1)
    drawTriangle(draw, 200, 175, cubestate[23], -1)

    drawTriangle(draw, 180, 210, 'y', -1)
    #drawTriangle()

    im.save(filename)

#generateImage('ggggygrbbbybrrbrgryryyyb', 'test.png')

cycles = pickle.load(open("5cycle.pickle", "rb"))
print(len(cycles.keys()))

solved_top = {}
double_flip = {}
nutella = {}
minty = {}
minutella_l = {}
minutella_r = {}
flip_l = {}
flip_r = {}
soloflip_l = {}
soloflip_r = {}
wo_l = {}
wo_r = {}
oka_l = {}
oka_r = {}
bell_l = {}
bell_r = {}
bottom = {}

for num, case in enumerate(cycles.keys()):
    generateImage(case, 'images/' + str(num) + '.png')
    permutation, orientation, rlub_solutions, rlu_solutions = cycles[case]
    cycles[case].append(num)
    if permutation[0] == 0 and permutation[1] == 1 and orientation[0] == 0 and orientation[1] == 0:
        solved_top[case] = cycles[case]
    elif permutation[0] == 0 and permutation[1] == 1 and orientation[0] == 1 and orientation[1] == 1:
        double_flip[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 1 and orientation[1] == 1:
        nutella[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 0 and orientation[1] == 0:
        minty[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 1 and orientation[1] == 0:
        minutella_l[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 0 and orientation[1] == 1:
        minutella_r[case] = cycles[case]
    elif permutation[0] == 0 and permutation[1] == 1 and orientation[0] == 1 and orientation[1] == 0:
        flip_l[case] = cycles[case]
    elif permutation[0] == 0 and permutation[1] == 1 and orientation[0] == 0 and orientation[1] == 1:
        flip_r[case] = cycles[case]
    elif permutation[0] == 0 and permutation[1] != 1 and orientation[0] == 1:
        soloflip_l[case] = cycles[case]
    elif permutation[0] != 0 and permutation[1] == 1 and orientation[1] == 1:
        soloflip_r[case] = cycles[case]
    elif permutation[0] == 0 and permutation[1] != 1 and orientation[0] == 0:
        wo_l[case] = cycles[case]
    elif permutation[0] != 0 and permutation[1] == 1 and orientation[1] == 0:
        wo_r[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] != 0 and orientation[0] == 0:
        oka_l[case] = cycles[case]
    elif permutation[1] == 0 and permutation[0] != 1 and orientation[1] == 0:
        oka_r[case] = cycles[case]
    elif permutation[0] == 1 and permutation[1] != 0 and orientation[0] == 1:
        bell_l[case] = cycles[case]
    elif permutation[1] == 0 and permutation[0] != 1 and orientation[1] == 1:
        bell_r[case] = cycles[case]
    elif permutation[0] not in [0, 1] and permutation[1] not in [0, 1]:
        bottom[case] = cycles[case]
method_names = ['top', '2flip', 'nutella', 'minty', 'minutella_L', 'minutella_R', 'flip_L', 'flip_R', 'soloflip_L', 'soloflip_R', 'wo_L', 'wo_R', 'oka_L', 'oka_R', 'bell_L', 'bell_R', 'bottom']
methods = [solved_top, double_flip, nutella, minty, minutella_l, minutella_r, flip_l, flip_r, soloflip_l, soloflip_r, wo_l, wo_r, oka_l, oka_r, bell_l, bell_r, bottom]
sum_of_algs = 0
for pos, method in enumerate(methods):
    print(len(method.keys()))
    sum_of_algs += len(method.keys())
f = open('wszystko.csv', 'w')
for alg in cycles:
    _, _, RLUB, RLU, pos = cycles[alg]
    f.write(str(pos)+'\n')
    f.write('RLU\n')
    for alg in RLU:
        f.write(' '.join(alg) + '\n')
    f.write('RLUB\n')
    for alg in RLUB:
        f.write(' '.join(alg) + '\n')
f.close()
print(sum_of_algs)
