# COP_curve_Plotter
### The Problem statement :
The effect of evaporator temperature on the coefficient of performance of a heat pump is to be visualized. 

Consider an ideal cycle with R-22 as the working fluid and a condenser temperature of 40  ͦC.

 Plot a curve for the coefficient of performance versus the evaporator temperature for the temperatures from -15  ͦC to -25 ͦC


### Description
The python script main_assemble.py is used to achieve the visual plots for the above given problem statement by using matplotlib and extracting data from the available dataset in excel file. 

The excel file contains the refrigerant R22's property values like specific heat, enthalpy, entropy.

The output is displayed with the help of an interactive GUI interface using wx module.

### Quick Start
Clone and run the [COP_curve_Plotter](https://github.com/soulbliss/COP_curve_Plotter) repository to see the script in action.

```sh
git clone https://github.com/soulbliss/COP_curve_Plotter
cd COP_curve_Plotter
python main_assemble.py
```



## Outputs
![The user enters the input](https://github.com/soulbliss/COP_curve_Plotter/blob/master/Images/1.jpg?raw=true)

![Clicking on the left button, reveals out this graph](https://github.com/soulbliss/COP_curve_Plotter/blob/master/Images/2.jpg?raw=true)

![Clicking on the right button, plots this graph accordingly](https://github.com/soulbliss/COP_curve_Plotter/blob/master/Images/3.jpg?raw=true)


## Conclusion
As the temperature increases the COP also increases and hence as shown in the figures above the ideal values are accurate.
