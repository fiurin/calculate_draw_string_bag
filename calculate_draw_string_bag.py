#!/usr/bin/env python3

# This script shall help to calculate the pattern sizes for
# variants of "Triangle Gusset Drawstring Bag", an awesome sewing
# tutorial by #巾着袋#三角マチ#GiftIDEA on YouTube
# https://www.youtube.com/watch?v=coTLsExBB8I

seam_allowance = 1 # cm

welcome = (
    f"CALCULATE SIZES FOR TRIANGEL GUSSET DRAWSTRING BAG \n"
    f"Tutorial: https://www.youtube.com/watch?v=coTLsExBB8I \n"
    f"The author assumes that measurements are given in cm. "
    f"{seam_allowance} cm seam allowance is included.\n"
    f"------------------------------------------------------"
    f"---------------------------------"
)
print(welcome)
 
# get the sizes of the final bag
width_bag = float(input("How wide should the final bag become? "))
height_bag = float(input("How high should the final bag become? "))
depth_bag = float(input("How deep should the final bag become? "))
height_drawstring = float(input("How big should the drawstring become? "))

# calculate width for each part
# width of final bag + seam allowance
width = width_bag + (2 * seam_allowance)

# calculate the side-panels
# high of final bag minus the size of the drawstring + seam allowance
side_length = height_bag - height_drawstring + (2 * seam_allowance)

# calculate the bottom
# depth of the bag + seam allowance
bottom_length = depth_bag + (2 * seam_allowance)

# calculate the inner fabric
# 2 sides + the draw string on each side + the bottom + seam allowance
inner_fabric_length = (2 * height_bag) + bottom_length

# output
output_sizes = (
    f"2 pieces for sides (outer fabric): {side_length} cm x {width} cm \n"
    f"1 piece for bottom (same as inner fabric) : {bottom_length} cm x {width} cm \n"
    f"1 piece for inner fabric: {inner_fabric_length} cm x {width} cm \n"
    f"IMPORTANT: The calculated sizes contain a seam allowance of {seam_allowance} cm. \n"
)

print(output_sizes)