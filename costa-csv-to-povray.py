#!/usr/bin/python

# Convert a CSV file produced by Costa.nb to a PovRay mesh2 object.

import csv

with open("costa.csv", "rb") as f:
    with open("costa-object.inc", "w") as g:
        c = csv.reader(f, delimiter=",", quotechar='"')
        c.next ()
        n_vert = int(c.next()[0])
        g.write("  vertex_vectors {\n    %d,\n" % n_vert)
        for i in range(n_vert):
          v = c.next()
          g.write("    <%s,%s,%s>%s\n" % (v[0], v[1], v[2], ("," if i < n_vert-1 else "")))
        g.write("  }\n\n")
        n_norm = int(c.next()[0])
        g.write("  normal_vectors {\n    %d,\n" % n_norm)
        for i in range(n_norm):
          v = c.next()
          g.write("    <%s,%s,%s>%s\n" % (v[0], v[1], v[2], ("," if i < n_vert-1 else "")))
        g.write("  }\n\n")
        n_face = int(c.next()[0])
        g.write("  face_indices {\n    %d,\n" % n_face)
        for i in range(n_face):
          v = c.next()
          g.write("    <%s,%s,%s>%s\n" % (v[0], v[1], v[2], ("," if i < n_vert-1 else "")))
        g.write("  }\n\n")

