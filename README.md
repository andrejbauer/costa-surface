## Costa's minimal surface with PovRay

[Costa's minimal surface](http://mathworld.wolfram.com/CostaMinimalSurface.html) is one of those amazing mathematical objects that look good when rendered with [PovRay](http://www.povray.org/). While it is not too hard to find triangulations of Costa's surface suitable for the PovRay [`triangle` element](http://www.povray.org/documentation/view/3.6.1/295/), triangulations with surface normals are not that easy to come by. But these are needed for the [`smooth_triangle`](http://www.povray.org/documentation/view/3.6.1/295/) element which makes Phong shading possible.

In the service of humanity, and especially my students who wanted to render the surface, I provide here the code to triangulate and compute the normals to Costa's minimal surface. The code is written in Mathematica, which is not freely accessible. Therefore, for convenience the repository also contains certain files generated by Mathematica:

* a CSV file `costa.csv` with ready-made triangulations and surface normals, with
  a Python script `cvs-to-mesh2.py` for converting the CSV file to a partial PovRay   
  [`mesh2`](http://www.povray.org/documentation/view/3.6.1/293/) element,

* a PDF file `Costa.pdf`, the PDF export of `Costa.nb`, so you can see how I did it.

### How to use the files

To generate a picture using PovRay, proceed as follows:

1. Run `Costa.nb` with Mathematica and use the `CostaCSV` function to generate a CSV
   file which contains the triangulation and normals, say `costa.csv`.

2. Use `csv-to-mesh2.py` to convert the CSV file to a *partial* PovRay `mesh2` object.

3. Include the partial `mesh2` object into your PovRay file, as demonstrated in `costa.pov`.

4. Generate `costa.png` with something like

        povray costa.pov +A +J +W1024 +H1024

### The format produced by Mathematica `CostaCSV` function

The Mathematica function `CostaCSV` outputs a CSV file in a format that is suitable for
generating a PovRay `mesh2` object:

1. The first line lists the parameters that were used with in the call to `CostaCSV`:

        r1,r2,k,l,m,n

  Their meaning is as follows:

    * `r1` and `r2` are the radii which determine the upper and middle radius of the surface
    * `k`, `l`, `m`, `n` specify the number of vertices used in the triangulation, specifically:
      `k` for the inner points, `l` for the edges, `m` for one rim and `n` for the other rim.
      In general, larger numbers mean a finer mesh.

2. The triangulation points, where `N` is the number of points, followed by one point per line:

        N
        x1,y1,z1
        x2,y2,z2
        ...
        xN,yN,zN

3. The normalized normals to the surface at respective triangulation points, where `N` is the
   number of points (and equal to the `N` above):


        N
        u1,v1,w1
        u2,v2,w2
        ...
        uN,vN,wN  

4. The triangles that form the surface triangulation, where `M` is their numbers and the indices
   refer to the points above.

        M
        i1,j1,k1
        i2,j2,k2
        ...
        iM,jM,kM

### The result

The file `costa.pov` generates the following picture:

<img src="https://raw.github.com/andrejbauer/costa-surface/master/costa.png" width=80% align="center"/>
