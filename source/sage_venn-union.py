m=2
scale = 1.7
sx=3
sy=2
centers = [(cos(n*2*pi/m), sin(n*2*pi/m)) for n in range(m)]
clr = ['blue', 'blue', 'green']
G = Graphics()
r=lambda x,y:(x-centers[0][0])^2+(y-centers[0][1])^2 < scale^2 or (x-centers[1][0])^2+(y-centers[1][1])^2 < scale^2
G+=region_plot(r,(-sx,sx),(-sy,sy),plot_points=200,incol='lightblue',axes=False)
for i in range(m):
    G += circle(centers[i], scale)
for i in range(m):
    G += circle(centers[i], scale)
G+=line([[-sx,-sy],[sx,-sy],[sx,sy],[-sx,sy],[-sx,-sy]],rgbcolor=(0,0,0))
G+=text('B',centers[0],fontsize='x-large')
G+=text('A',centers[1],fontsize='x-large')
G