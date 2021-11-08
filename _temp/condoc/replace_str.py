import re

# content = """
# > In algorithms there is a starting state *S* and a sequence of legal
# > steps (moves, transformations). One looks for answers to the following
# > questions:
# >
# > 1\. Can a given end state be reached?
# >
# > 2\. Find all reachable end states.
# >
# > 3\. Is there convergence to an end state?
# >
# > 4\. Find all periods with or without tails, if any.
# >
# > Since the Invariance Principle is a *heuristic principle*, it is best
# > learned by experience, which we will gain by solving the key examples
# > **E1** to **E10**.
# >
# > 2 1. The Invariance Principle

# *sequence of points* (*xn, yn*) *according to the rule***E1.** *Starting
# with a point S* � (*a, b*) *of the plane with* 0 *\< b \< a, we generate
# a*

# > *x*0 � *a,* *y*0 � *b,* *xn*+1 �*xn* ~~+~~ *yn,* *yn*+1 �2*xnyn* *.* 2
# > *xn* + *yn*
# >
# > Here it is easy to ﬁnd an *invariant*. From *xn*+1*yn*+1 � *xnyn*, for
# > all *n* we deduce *xnyn* � *ab* for all *n*. This is the *invariant*
# > we are looking for. Initially, we have *y*0 *\< x*0. This relation
# > also remains invariant. Indeed, suppose *yn \< xn* for some *n*. Then
# > *xn*+1 is the midpoint of the segment with endpoints *yn, xn*.
# > Moreover, *yn*+1 *\< xn*+1 since the harmonic mean is strictly less
# > than the arithmetic mean.
# >
# > Thus,\
# > 0 *\< xn*+1 − *yn*+1 �*xn* ~~−~~ *ynxn* + *yn*·*xn* − *yn\< xn* −
# > *yn*2\
# > for all *n*. So we have lim *xn* � lim *yn* � *x* with *x*2� *ab* or
# > *x* �√\
# > *ab*. Here the invariant helped us very much, but its recognition was
# > not yet the solution, although the completion of the solution was
# > trivial.
# """

def _replace_basic(content, rpls):
    for key, val in rpls.items():
        content = content.replace(key, val)
    return content

def _replace_regex(content, rpls):
    for key, val in rpls.items():
        content = re.sub(key, val, content)
    return content


if __name__ == '__main__':
    ## NOTE: Problem-Solving_Strategies_Engel.md
    rpls_basic =  {
        '\.': '.',
        '�': '=',
        'ﬁ': 'fi',
        '√': '_sqrt_',
        " .\n. ": ' . . ',
        ",\n. ": ', . ',
        '. . .': '···',
        " ·\n· ": ' · · ',
        ",\n· ": ', · ',
        '· · ·': '...'
    }
#  .\n. 
# \>
# \<
# =→
    rpls_regex = {
        r'\n> *': r'\n',
        r'\\\n': r'\\ ',
        r'([a-zA-Z0-9,*≥=+−→←()) ])\n([a-zA-Z0-9,*≥=+−→←()) ])': r'\1 \2'
        # r'([a-zA-Z])\n([a-zA-Z])': '\1 \2'
    }

    content = open('source/Problem-Solving_Strategies_Engel.md', 'r', encoding='utf-8').read()

    content = _replace_basic(content, rpls_basic)
    content = _replace_regex(content, rpls_regex)

    open('modified/Problem-Solving_Strategies_Engel.md', 'w', encoding='utf-8').write(content)
    # print(content)
