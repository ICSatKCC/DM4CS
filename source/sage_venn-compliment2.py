scale = 1.7
sx=3
sy=2
G = Graphics()
r=lambda x,y: x^2+y^2 &gt; scale^2
G+=region_plot(r,(-sx,sx),(-sy,sy),plot_points=200,incol='lightblue',axes=False)
G += circle([0,0], scale)
G+=line([[-sx,-sy],[sx,-sy],[sx,sy],[-sx,sy],[-sx,-sy]],rgbcolor=(0,0,0))
G+=text('A',[0,0],fontsize='x-large')
G