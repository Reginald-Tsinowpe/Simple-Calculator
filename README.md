# Simple-Calculator
## How it works

The window is created with all buttons and entry fields(for text input) shown.  
Anytime a button is clicked, a function named 'entered' is called.  
This function inputs the button's text into the 'Data_Entry' entry field.  
When the '=' button is clicked, or 'Return' key is pressed, the 'Eql_But_Func' function is called.  
This function take the text in the 'Data_Entry' entry field, and passes it as an argument to the 'Calc' function.  
The 'Calc' passes its parameter into the 'eval' function to do the math, clears the existing text in the entry field, and replaces it with the new text.  
The result is then  displayed in the 'Data_Entry' entry field.  

If the entry field is not cleared before further input, the input will follow the already present text in the entry field - Just like an actual calculator.
