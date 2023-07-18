# Finance Calculator Application

## Description
The Finance Calculator application allows users to perform investment and bond calculations based on user input. It provides a user-friendly interface built using PyQt5 library.

## Dependencies
The application relies on the following external libraries:
- PyQt5: A set of Python bindings for the Qt application framework.

## Class Documentation

### CalculationTypeDialog
- Description: Represents a dialog window for selecting the calculation type.
- Inherits: QDialog
- Methods:
  - `__init__()`: Initializes the dialog window with investment and bond radio buttons and an Ok/Cancel button box.
  - `get_calculation_type()`: Opens the dialog window and returns the selected calculation type (investment or bond).

### InvestmentDialog
- Description: Represents a dialog window for inputting investment calculation parameters.
- Inherits: QDialog
- Methods:
  - `__init__()`: Initializes the dialog window with input fields for amount, interest rate, investment duration, calculation type (simple or compound), and an Ok/Cancel button box.
  - `get_inputs()`: Opens the dialog window and returns the inputted investment parameters (amount, interest rate, investment duration, calculation type).

### BondDialog
- Description: Represents a dialog window for inputting bond calculation parameters.
- Inherits: QDialog
- Methods:
  - `__init__()`: Initializes the dialog window with input fields for present value, interest rate, loan duration, and an Ok/Cancel button box.
  - `get_inputs()`: Opens the dialog window and returns the inputted bond parameters (present value, interest rate, loan duration).

### MainWindow
- Description: Represents the main window of the Finance Calculator application.
- Inherits: QMainWindow
- Methods:
  - `__init__()`: Initializes the main window with a result label, a "Start Calculation" button, a "Go Back" button, and a layout.
  - `calculate()`: Performs the calculation based on the selected calculation type and inputted parameters.
  - `select_calculation_type()`: Opens the CalculationTypeDialog and sets the selected calculation type.
  
## Usage
To use the Finance Calculator application:
1. Ensure that the required dependencies are installed (PyQt5)
    pip install pip.
    pip install PyQt5.
2. Run the script.
3. The main window will appear with the option to select a calculation type (investment or bond).
4. Select the desired calculation type.
5. Input the required parameters in the dialog window that appears.
6. Click the "Start Calculation" button to perform the calculation.
7. The result will be displayed in the result label.
8. To perform another calculation, click the "Go Back" button to return to the calculation type selection.

Note: Invalid input will be handled with error messages displayed in message boxes.

## Conclusion
The Finance Calculator application provides a convenient way for users to perform investment and bond calculations. It features an intuitive user interface and input validation to ensure accurate results. Users can easily switch between calculation types and perform multiple calculations within the same session.
