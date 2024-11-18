def is_layout_correct(layout) :
    
    list_of_layout = ["1x12" , "2x6" , "3x4", "4x3", "6x2" , "12x1"]
    for i in range(0,6) :
        if layout == list_of_layout[i] :
            return True;
    return False;