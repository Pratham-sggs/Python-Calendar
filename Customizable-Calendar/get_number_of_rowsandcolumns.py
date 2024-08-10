def get_rows_columns_list(layout) :
    list_of_layout = ["1x12" , "2x6" , "3x4", "4x3", "6x2" , "12x1"]
    list_of_rc = [[1,12] , [2,6], [3,4], [4,3], [6,2] , [12,1]]
    for i in range(0,6) :
        if layout == list_of_layout[i] :
            return list_of_rc[i];