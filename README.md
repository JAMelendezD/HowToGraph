# HowToGraph

## Matplotlib

Basic scripts using matplot to create high quality plots, animations, 3d plots and much more.

## Pymol

I have written a short script to create 3 dimensional functions and vizualise them using pymol. This can be very useful since all the advantages from pymol can be used on the graphs such as different representations, color and ray tracing.

For this to work you will need to install pymol:

`sudo apt-get install pymol`
 
 Now you can run the program with your version of python for my case it is:
 
`python3 functiontopymol.py new -1 1 100 80 X**2-Y**2`

<p align="center">
  <img width="800" src="./media/example3.png">
</p>

For information about the parameters you can type `python3 functiontopymol.py -h`. The program will create a function and open it using pymol if you need a tutorial on how to use pymol you can check this link [Pymol tutorial](https://jamelendezd.github.io/MolecularDynamicsPymol/). The program also creates a colormap of the function and can be open by typing in the terminal:

`pymol colormap.pml`

Finally here are some sample images created with this repository.

<p align="center">
  <img width="800" src="./media/example1.png">
</p>

<p align="center">
  <img width="800" src="./media/example2.png">
</p>

<p align="center">
  <img width="800" src="./media/example4.png">
</p>

<p align="center">
  <img width="800" src="./media/map2.png">
</p>

<p align="center">
  <img width="800" src="./media/map3.png">
</p>
