from wifi import Cell, Scheme


cell = Cell.all('en0')

# cell = Cell.all('en0')[0]
# scheme = Scheme.for_cell('en0', 'home', cell, passkey)
# scheme.save()
# scheme.activate()
#
# scheme = Scheme.find('en0', 'home')
# scheme.activate()