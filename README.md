# IPFragCalculator
A teaching tool for IP fragmentation

## Usage (for IST 220 students)

Download the file `IPFragCalc.py` to your virtual machine. Open the Terminal, `cd` to the folder where the file downloaded, and then run `python3 IPFragCalc.py`. 

When you run the program, you can choose to assign values for the datagram length, the MTU, the fragment identifier, and the header size. By default, the following values are used:

|            Argument | Default Value |
|--------------------:|:-------------:|
|     Datagram length | 4000          |
|                 MTU | 1500          |
| Fragment idenfifier | x             |
|         Header size | 20            |

To see how to customize these values, run `python3 IPFragCalc.py --help`.