def namecolor_to_rgb(s, complementary = False):
    
    colors_ = s.split('!')
    
    color1_ = to_rgb(colors_[0])
    color2_ = to_rgb(colors_[2])
    proportion = int(colors_[1])

    final_color = [0.0, 0.0, 0.0, 1.0]

    for i_ in range(3):
        final_color[i_] = color1_[i_] * proportion/100 + color2_[i_] * (100 - proportion)/100

    if len(colors_) == 4:
        final_color[3] = int(colors_[3])/100
        
        
    if complementary:
        rc = np.max(final_color[:3]) + np.min(final_color[:3]) - final_color[0]
        gc = np.max(final_color[:3]) + np.min(final_color[:3]) - final_color[1]
        bc = np.max(final_color[:3]) + np.min(final_color[:3]) - final_color[2]
        
        final_color[0] = rc
        final_color[1] = gc
        final_color[2] = bc
            
    return final_color   