#-----------------------------------------------------------------------
# Application 1: Identifying Cholera Hotspots from Water Contamination Levels
# Name: Najiyah Williamson
# Due Date: 3/27/26
#-----------------------------------------------------------------------

bacterial_levels = [250, 720, 480, 510, 300, 680, 590]

# copying the list object bacterial_levels
OGbacterial_levels = bacterial_levels[:]
unsafe_count = 0 #need this before the loop so I can count

# using enumerate() for loop
for i, contamination in enumerate(bacterial_levels, start = 1):
    safety = "Unsafe" if contamination >= 500 else "Safe"
    print(f"Source {i}: {contamination} ({safety})")
    bacterial_levels[i-1] = [contamination, i, safety] #adapted from Mod 3 notes: -1 lets it start from 0 in list

# counting unsafe sources
unsafe_count = sum(level >= 500 for level in OGbacterial_levels)
print(f"Total Unsafe Sources: {unsafe_count}")

# top 3 most contaminated
top3 = sorted(OGbacterial_levels, reverse=True)[:3]
print("Top 3 Most Contaminated Bacterial Levels:", top3[0], ",", top3[1], ",", top3[2])

# average contamination
avg_contamination = sum(OGbacterial_levels) / len(OGbacterial_levels)
print("Average bacterial contamination across the Water Sources:", round(avg_contamination, 2))

# sorting modified bacterial levels list from highest to lowest bacterial levels
print("\n""Contamination Levels (High to Low):")
print("\n".join(map(lambda x: f"{x[0]} (Source {x[1]} - {x[2]})", sorted(bacterial_levels, reverse=True))))

# Original bacterial levels list
print("\n" + str(OGbacterial_levels)) # this format creates a line space before

# Modified bacterial levels nested list
print("\n" + str(bacterial_levels))

# function for threshold
def count_unsafe_sources(bact_levels, thres):
    unsafe_count = 0
    for level in bact_levels:
        if level >= thres:
            unsafe_count += 1
    return unsafe_count

# calling the function
no_unsafe_sources = count_unsafe_sources(bact_levels=OGbacterial_levels, thres=600)
print("\n" + str(no_unsafe_sources))
