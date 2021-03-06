import pygal

wm = pygal.maps.world.World()

wm.title = 'North, Central, and Suth America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('Oceania', ['nz'])

wm.render_to_file('americas.svg')