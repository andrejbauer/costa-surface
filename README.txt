1. Run Cota.nb with Mathematica and use the CostaCSV function to generate a CSV
   file which contains the triangulation and normals, say "costa.csv".

2. Use costa-csv-to-povray.py to convert the CSV file to a partial PovRay mesh2 object
   and save it to "costa-object.inc".

3. Include the partial mesh2 object into your PovRay file, as shown in "costa.pov".

4. Generate "costa.png" with something like

   povray costa.pov +A +J +W1024 +H1024

