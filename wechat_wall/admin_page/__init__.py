WHETHER_REVIEW = 1 
# 1: need to be reviewed
# 0: don't need


def get_whether_review():
    return WHETHER_REVIEW


def set_whether_review(whether_review):
    print whether_review
    global WHETHER_REVIEW
    WHETHER_REVIEW = whether_review
    print WHETHER_REVIEW
