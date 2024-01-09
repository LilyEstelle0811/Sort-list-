def sort_list(inlist):
    if len(inlist) <= 1:
        return(inlist)
    elif len(inlist) == 2:
        if inlist[0] <= inlist[1]:
            return inlist
        else:
            return [inlist[1],inlist[0]]
    else:
        first_item = inlist[0]
        inlist.remove(first_item)
        higher_list = []
        lower_list = []
        
        for i in inlist:
            if i > first_item:
                higher_list.append(i)
            else:
                lower_list.append(i)
                
        sort_lower = sort_list(lower_list)
        sort_higher = sort_list(higher_list)
        
        #print(sort_higher)
        
        return (sort_lower+[first_item]+sort_higher)
