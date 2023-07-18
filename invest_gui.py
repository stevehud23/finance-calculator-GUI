from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QRadioButton, QWidget, QMessageBox, QInputDialog
import math

class CalculationTypeDialog(QDialog):
    """Dialog for selecting the calculation type: investment or bond."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculation Type")
        self.layout = QVBoxLayout(self)
        self.investment_radio = QRadioButton("Investment")
        self.bond_radio = QRadioButton("Bond")
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.investment_radio)
        self.layout.addWidget(self.bond_radio)
        self.layout.addWidget(self.button_box)

    def get_calculation_type(self):
        """Returns the selected calculation type: 'investment' or 'bond'."""
        if self.exec_() == QDialog.Accepted:
            if self.investment_radio.isChecked():
                return "investment"
            if self.bond_radio.isChecked():
                return "bond"
        return None

class InvestmentDialog(QDialog):
    """Dialog for investment calculation."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Investment Calculation")
        self.layout = QVBoxLayout(self)
        self.amount_label = QLabel("Amount:")
        self.amount_edit = QLineEdit()
        self.rate_label = QLabel("Interest Rate:")
        self.rate_edit = QLineEdit()
        self.time_label = QLabel("Investment Duration (in years):")
        self.time_edit = QLineEdit()
        self.calculation_type_label = QLabel("Calculation Type:")
        self.simple_radio = QRadioButton("Simple")
        self.compound_radio = QRadioButton("Compound")
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.cancel_dialog)  # Connect rejected signal to custom slot
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_edit)
        self.layout.addWidget(self.rate_label)
        self.layout.addWidget(self.rate_edit)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.time_edit)
        self.layout.addWidget(self.calculation_type_label)
        self.layout.addWidget(self.simple_radio)
        self.layout.addWidget(self.compound_radio)
        self.layout.addWidget(self.button_box)

    def cancel_dialog(self):
        # Clear input fields and selected calculation type
        self.amount_edit.clear()
        self.rate_edit.clear()
        self.time_edit.clear()
        self.simple_radio.setChecked(False)
        self.compound_radio.setChecked(False)
        
    def closeEvent(self, event):
        event.accept()  # Accept the close event to close the window

    def get_inputs(self):
        """Returns the input values for investment calculation."""
        while True:
            try:
                p = float(self.amount_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid amount. Please enter a valid number.")
                self.amount_edit.setText("")
                self.amount_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        while True:
            try:
                r = float(self.rate_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid interest rate. Please enter a valid number.")
                self.rate_edit.setText("")
                self.rate_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        while True:
            try:
                t = float(self.time_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid investment duration. Please enter a valid number.")
                self.time_edit.setText("")
                self.time_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        calculation_type = ""
        if self.simple_radio.isChecked():
            calculation_type = "simple"
        elif self.compound_radio.isChecked():
            calculation_type = "compound"
        else:
            QMessageBox.warning(self, "Calculation Type", "Please select a calculation type.")
            if self.exec_() == QDialog.Rejected:
                return None, None, None, None

        return p, r, t, calculation_type

class BondDialog(QDialog):
    """Dialog for bond calculation."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bond Calculation")
        self.layout = QVBoxLayout(self)
        self.present_value_label = QLabel("Present Value:")
        self.present_value_edit = QLineEdit()
        self.interest_rate_label = QLabel("Interest Rate:")
        self.interest_rate_edit = QLineEdit()
        self.duration_label = QLabel("Loan Duration (in months):")
        self.duration_edit = QLineEdit()
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.cancel_dialog)  # Connect rejected signal to custom slot
        self.layout.addWidget(self.present_value_label)
        self.layout.addWidget(self.present_value_edit)
        self.layout.addWidget(self.interest_rate_label)
        self.layout.addWidget(self.interest_rate_edit)
        self.layout.addWidget(self.duration_label)
        self.layout.addWidget(self.duration_edit)
        self.layout.addWidget(self.button_box)
        
    def cancel_dialog(self):
        # Clear input fields
        self.present_value_edit.clear()
        self.interest_rate_edit.clear()
        self.duration_edit.clear()
        
    def closeEvent(self, event):
        event.accept()  # Accept the close event to close the window

    def get_inputs(self):
        """Returns the input values for bond calculation."""
        while True:
            try:
                P = float(self.present_value_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid present value. Please enter a valid number.")
                self.present_value_edit.setText("")
                self.present_value_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        while True:
            try:
                i = float(self.interest_rate_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid interest rate. Please enter a valid number.")
                self.interest_rate_edit.setText("")
                self.interest_rate_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        while True:
            try:
                n = float(self.duration_edit.text())
                break
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Invalid loan duration. Please enter a valid number.")
                self.duration_edit.setText("")
                self.duration_edit.setFocus()
                if self.exec_() == QDialog.Rejected:
                    return None, None, None

        return P, i, n


class MainWindow(QMainWindow):
    """Main window for the finance calculator."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Calculator")

        self.result_label = QLabel("Calculation Result:")
        self.result_label.setWordWrap(True)

        self.calculate_button = QPushButton("Start Calculation")
        self.calculate_button.clicked.connect(self.calculate)

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(self.select_calculation_type)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.back_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.calculation_type = None
        self.dialog = None

    def calculate(self):
        """Performs the selected calculation based on the calculation type."""
        if self.calculation_type is None:
            QMessageBox.warning(self, "Calculation Type", "Please select a calculation type.")
            return

        if self.dialog is None:
            if self.calculation_type == "investment":
                self.dialog = InvestmentDialog()
            elif self.calculation_type == "bond":
                self.dialog = BondDialog()
            else:
                return

        dialog_result = self.dialog.exec_()
        if dialog_result == QDialog.Accepted:
            if self.calculation_type == "investment":
                p, r, t, calculation_type = self.dialog.get_inputs()
                if calculation_type == "simple":
                    interest = r / 100 * p * t
                    total_amount = p + interest
                    result = f"\nInterest Rate: {r}%\nTotal Investment: £{total_amount}\nTotal Duration: {t} years\nTotal Interest: £{interest}"
                elif calculation_type == "compound":
                    total_amount = p * math.pow((1 + r / 100), t)
                    interest = total_amount - p
                    result = f"\nInterest Rate: {r}%\nTotal Investment: £{total_amount}\nTotal Duration: {t} years\nTotal Interest: £{interest}"
                else:
                    return
            elif self.calculation_type == "bond":
                P, i, n = self.dialog.get_inputs()
                m = i / 100 / 12
                repayment = int(round(m * P) / (1 - (1 + m) ** (-n)))
                interest_total = repayment * n - P
                total_loan = repayment * n
                result = f"\nMonthly Repayment: £{repayment}\nInterest Rate: {i}%\nLoan Duration: {n} months\nTotal Interest Payable: £{interest_total}\nTotal Repayable: {total_loan}"
            else:
                return

            self.result_label.setText(result)
            self.dialog = None
        elif dialog_result == QDialog.Rejected:
            if self.dialog.get_inputs() is None:
                QMessageBox.warning(self, "Notification", "Please select an option.")
                self.select_calculation_type()

    def select_calculation_type(self):
        """Displays the dialog to select the calculation type."""
        self.result_label.setText("Calculation Result:")
        self.calculation_type = None
        self.dialog = None
        dialog = CalculationTypeDialog()
        result = dialog.get_calculation_type()
        if result is not None:
            self.calculation_type = result
        else:
            reply = QMessageBox.warning(
                self, "Warning", "Cancel: to go back to the main menu\nClose: to quit the application.",
                QMessageBox.Cancel | QMessageBox.Close, defaultButton=QMessageBox.Cancel
            )
            if reply == QMessageBox.Close:
                QApplication.quit()  # Quit the application immediately
            elif reply == QMessageBox.Cancel:
                self.select_calculation_type()  # Recursive call to return to the investments selection menu

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.select_calculation_type()
    window.show()
    app.exec_()









