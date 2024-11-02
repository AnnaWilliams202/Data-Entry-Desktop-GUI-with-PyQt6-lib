from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QApplication, QPushButton, QLineEdit
import sys


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.layout = QVBoxLayout()

        # Input fields for weight and height
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Enter weight in kg")
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Enter height in cm")

        # Calculate button and result label
        self.calculate_button = QPushButton('Calculate BMI')
        self.result_label = QLabel('')

        # Add widgets to layout
        self.layout.addWidget(QLabel('Weight (kg):'))
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(QLabel('Height (cm):'))
        self.layout.addWidget(self.height_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        # Set layout and connect button
        self.setLayout(self.layout)
        self.calculate_button.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
            self.result_label.setText(f'Your BMI: {bmi:.2f} ({category})')

            self.weight_input.clear()
            self.height_input.clear()
        except ValueError:
            self.result_label.setText("Please enter valid numbers for weight and height.")


app = QApplication(sys.argv)
window = BMICalculator()
window.show()
sys.exit(app.exec())