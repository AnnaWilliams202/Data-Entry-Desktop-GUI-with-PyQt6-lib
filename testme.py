import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

# Create the application instance
app = QApplication(sys.argv)

# Create the main window (widget)
window = QWidget()
window.setWindowTitle('Data Entry Tool')
window.setGeometry(100, 100, 300, 150)

# Create layout
layout = QVBoxLayout()

# Create input fields
firstNameField = QLineEdit()
firstNameField.setPlaceholderText('Enter first name here...')
layout.addWidget(firstNameField)

lastNameField = QLineEdit()
lastNameField.setPlaceholderText('Enter last name here...')
layout.addWidget(lastNameField)

# Create submit button
submitButton = QPushButton('Submit')
layout.addWidget(submitButton)

# Set layout on the window
window.setLayout(layout)

# Connect Enter key to submit button click for both fields
firstNameField.returnPressed.connect(submitButton.click)
lastNameField.returnPressed.connect(submitButton.click)


# Function to handle data submission
def submitData():
    first_name = firstNameField.text()
    last_name = lastNameField.text()

    if not first_name or not last_name:
        QMessageBox.warning(window, 'Warning', 'Both input fields must be filled!')
        return

    csv_file = 'data2.csv'
    file_exists = os.path.isfile(csv_file)

    if file_exists:
        # Append to the existing CSV file
        with open(csv_file, mode='a', newline='') as file:
            file.write(f"{first_name},{last_name}\n")
    else:
        # Create a new CSV file and write the header and data
        with open(csv_file, mode='w', newline='') as file:
            file.write("First Name,Last Name\n")
            file.write(f"{first_name},{last_name}\n")

    firstNameField.clear()  # Clear first name field
    lastNameField.clear()  # Clear last name field
    QMessageBox.information(window, 'Success', 'Data has been added to the CSV file!')


# Connect submit button click to submitData function
submitButton.clicked.connect(submitData)

# Show the window
window.show()

# Execute the application's event loop
sys.exit(app.exec())