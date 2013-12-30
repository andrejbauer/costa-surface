#!/usr/bin/env python

# Convert a CSV file produced by Costa.nb to a PovRay mesh2 object.

import csv
import argparse

parser = argparse.ArgumentParser('csv-to-mesh2.py')
parser.add_argument('input', action='store', type=argparse.FileType(mode='rb'), help='input file (.csv)')
parser.add_argument('output', action='store', type=argparse.FileType(mode='w'), help='output file (.inc)')
args = parser.parse_args()

f = args.input
g = args.output

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

