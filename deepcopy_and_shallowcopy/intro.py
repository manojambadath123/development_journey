

arun_fvt_colors = ["red","green","blue"]

hari_fvt_colors = arun_fvt_colors

hari_fvt_colors[0] = "purple"

print(arun_fvt_colors is hari_fvt_colors)

print(arun_fvt_colors)

print(hari_fvt_colors)



arun_fvt_colors = ["red","green","blue"]

hari_fvt_colors = arun_fvt_colors.copy()

hari_fvt_colors[0] = "purple"

print(arun_fvt_colors is hari_fvt_colors)



print(arun_fvt_colors)

print(hari_fvt_colors)

