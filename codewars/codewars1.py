def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    years = 0
    if human_years == 1:
        cat = 15
        dog = 15
        years = 1
    elif human_years == 2:
        cat = 24
        dog = 24
        years = 2
    else:
        years = human_years
        y = human_years - 2
        cat = 15 + 9 + (y*4)
        dog = 15 + 9 + (y*5)
    return [years,cat,dog]