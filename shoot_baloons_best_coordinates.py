"""


"""

def sphere_line_intersection(l1, l2, sp, r):

    def square(f):
        return f * f
    from math import sqrt

    # l1[0],l1[1],l1[2]  P1 coordinates (point of line)
    # l2[0],l2[1],l2[2]  P2 coordinates (point of line)
    # sp[0],sp[1],sp[2], r  P3 coordinates and radius (sphere)
    # x,y,z   intersection coordinates
    #
    # This function returns a pointer array which first index indicates
    # the number of intersection point, followed by coordinate pairs.

    p1 = p2 = None

    a = square(l2[0] - l1[0]) + square(l2[1] - l1[1]) + square(l2[2] - l1[2])
    b = 2.0 * ((l2[0] - l1[0]) * (l1[0] - sp[0]) +
               (l2[1] - l1[1]) * (l1[1] - sp[1]) +
               (l2[2] - l1[2]) * (l1[2] - sp[2]))

    c = (square(sp[0]) + square(sp[1]) + square(sp[2]) + square(l1[0]) +
            square(l1[1]) + square(l1[2]) -
            2.0 * (sp[0] * l1[0] + sp[1] * l1[1] + sp[2] * l1[2]) - square(r))

    i = b * b - 4.0 * a * c

    if i < 0.0:
        pass  # no intersections
    elif i == 0.0:
        # one intersection
        p[0] = 1.0

        mu = -b / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

    elif i > 0.0:
        # first intersection
        mu = (-b + sqrt(i)) / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

        # second intersection
        mu = (-b - sqrt(i)) / (2.0 * a)
        p2 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

    return [p1, p2]

    radius = 2 #radius for all baloons is the same
    baloons = [[10,14,15],[15,18,19],[14,19,10]]
    l1 = [0, 0, 0] # always set first point to shooter's position

    nob = len(baloons) #get number of baloons

    for i in range (0, nob):

        for x2 in range (baloons[i][0]-radius, baloons[i][0]+radius+1):
            for y2 in range (baloons[i][1]-radius, baloons[i][1]+radius+1):
                for z2 in range (baloons[i][2]-radius, baloons[i][2]+radius+1):

                    points = sphere_line_intersection(l1, [x2, y2, z2] , baloons[i], radius)
                    if points[0] != None or points[1] != None # If there is at least one intersection with primary balloon
                        m = 0
                        while m < nob:
                            if m != i:
                                 

