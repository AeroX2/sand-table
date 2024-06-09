import cadquery as cq
from cq_gears import SpurGear

# Create a gear object with the SpurGear class
spur_gear = SpurGear(module=1.0, teeth_number=19, width=5.0, bore_d=5.0)

# Build this gear using the gear function from cq.Workplane
wp = cq.Workplane('XY').gear(spur_gear)

show(wp)
