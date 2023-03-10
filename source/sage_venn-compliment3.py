m=1
scale = 1.7
sx=3
sy=2
G = Graphics()
r=lambda x,y: x^2+y^2 < scale^2 and (x-0.75)^2+y^2 > 0.75^2
G+=region_plot(r,(-sx,sx),(-sy,sy),plot_points=200,incol='lightblue',axes=False)
G += circle([0,0], scale)
G += circle([0.75,0], 0.75)
G+=line([[-sx,-sy],[sx,-sy],[sx,sy],[-sx,sy],[-sx,-sy]],rgbcolor=(0,0,0))
G+=text('A',[-1,0],fontsize='x-large')
G+=text('B',[0.75,0],fontsize='x-large')
G