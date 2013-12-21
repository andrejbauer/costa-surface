#include "colors.inc"

camera {
    location <10, 12, 7>
    sky <0, 0, 1>
    look_at  <0, 0, 2>
}

light_source { 
  <20, 17, 15>
  color rgb <1,1,1>
}

plane {
  <0, 0, 1>, -8
  pigment { color rgb <0.5,0.5,0.5> }
}

mesh2 {
  #include "costa-object.inc"

  pigment{
    marble scale 2 turbulence 0.9
    color_map { 
      [0.0 color rgb <1,1,1>]
      [1.0 color rgb <0.3,0.3,1>]
    }
  }

  finish {
    specular 0.9
  }
}