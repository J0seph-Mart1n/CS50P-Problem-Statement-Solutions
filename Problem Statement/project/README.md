 # TRANSACTION MANAGEMENT SYSTEM
    #### Video Demo:  https://youtu.be/O22gQ8GAAM0
    #### Description: I created an command-line Transaction Management System that can track the expenses used by the user.
                      It also prints the balance amount.
    TODO

    The provided Python code implements a basic transaction management system, creating a simple interactive interface for users to add credited or deducted transactions, display transaction history, and check the account balance. Let's break down the code and provide a detailed description.

   Overview:
   The program begins by prompting the user to enter the maximum limit for the account. It then initializes a transaction details file, "transaction_details.txt," with column headers. The main loop of the program allows users to perform various actions until they choose to exit.

   Main Functionality:
   1. Adding Credited Transactions (Choice 1):
      - Users can input a credited transaction amount.
      - The gain_transaction function is called to handle the transaction.
      - If the transaction is successful (i.e., within the maximum limit), the transaction details are written to the file, and the amount is updated.
      - If there is an issue (e.g., storage full), an appropriate message is printed.

   2. Adding Deducted Transactions (Choice 2):
      - Similar to credited transactions, users input a deducted transaction amount.
      - The loss_transaction function is called to process the transaction.
      - If the transaction is successful (i.e., sufficient balance), the details are written to the file, and the amount is updated.
      - If there is an issue (e.g., low balance), an appropriate message is printed.

   3. Displaying Transactions (Choice 3):
      - The display_transaction function reads the transaction details from the file and prints them line by line.
      - The current account balance is also displayed.

   4. Exiting the Program (Choice 4):
      - The program displays the current account balance and exits the loop, ending the execution.

   Functions:
   - gain_transaction(n, max_amount) and loss_transaction(n) Functions:
   - These functions handle credited and deducted transactions, respectively.
   - They check if the transaction is valid based on the provided conditions (storage full or low balance).
   - If successful, transaction details are appended to the file, and the account balance is updated.

   - display_transaction() Function:
   - Reads the transaction details from the file and prints them.
   - Also displays the current account balance.

   Improvements:
   - Error Handling:
   - The code incorporates basic error handling for invalid user inputs, ensuring that the program doesn't crash if users provide non-integer choices or amounts.

   - Consistency in Variable Usage:
   - The code uses global variables (amount) for managing the account balance consistently.

   Test Function:
   - I tested the function in the test_project.py file that checked whether the amount is been added or subtracted from the balance variable.

   Conclusion:
   In summary, this Python program serves as a straightforward transaction management system. It allows users to interactively add credited and deducted transactions, view transaction history, and check the account balance. While the code is functional, it could be extended by incorporating more advanced features such as data validation, user authentication, or graphical interfaces for enhanced usability. The current implementation, however, provides a solid foundation for understanding basic transaction handling in Python.
