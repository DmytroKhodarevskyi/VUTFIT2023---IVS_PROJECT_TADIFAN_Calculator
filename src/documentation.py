


def __init__():
    """
    @brief Initializes the documentation class.
    @return None
    """


def print_key_event(self, event):
    """
    Simulates a button click on the calculator UI based on the user's keyboard input.

    Parameters:
    -----------
    event : str
        A string representing the keyboard input event triggered by the user.

    Returns:
    --------
    None

    Description:
    ------------
    This method maps the user's keyboard input to the corresponding button on the calculator's UI and simulates a
    button click event. If the input is a number or operator key, the corresponding button is clicked and the
    calculator's display is updated. If the input is a non-number key (e.g., Enter, Delete), the corresponding
    calculator button is clicked, triggering the appropriate action.

    Examples:
    ---------
    >>> calc = Calculator()
    >>> calc.print_key_event('1')
    # Clicks the Button_1 on the calculator's UI and updates the display to show '1'
    >>> calc.print_key_event('+')
    # Clicks the Button_Plus on the calculator's UI and updates the display accordingly
    """


def register_keyboard_event(self):
    """
    Register a function to be called when a key on the keyboard is pressed.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method uses the `on_press` method of the `keyboard` library to register a lambda function that takes a `keyboard`
    event as input and passes it to the `print_key_event` method of the current instance of the class.
    """


def add_number(self, Button_text: str):
    """
    Add a number to the UI entry widget.

    Parameters:
    -----------
    Button_text : str
        A string representing the number to be added to the UI entry widget.

    Returns:
    --------
    None

    Description:
    ------------
    This method adds a number to the current text in the UI entry widget. If the current text in the UI entry widget is "0",
    the method replaces it with the `Button_text`. Otherwise, the method appends the `Button_text` to the current text in
    the UI entry widget. After modifying the text in the UI entry widget, the method calls the `adjust_entry_font_size`
    method to adjust the font size of the text if necessary.
    """


def add_point(self):
    """
    Add a decimal point to the UI entry widget.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method adds a decimal point (" , ") to the current text in the UI entry widget if one is not already present. If a
    decimal point is already present, the method does nothing. After modifying the text in the UI entry widget, the method
    calls the `adjust_entry_font_size` method to adjust the font size of the text if necessary.
    """


def change_sign(self):
    """
    Change the sign of the number in the UI entry widget.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method changes the sign of the number currently displayed in the UI entry widget by adding or removing a minus
    sign ("-"). If the number is currently positive, the method adds a minus sign to make it negative. If the number is
    currently negative, the method removes the minus sign to make it positive. If the number is currently zero, the method
    does nothing.

    After changing the sign of the number, the method updates the text in the UI entry widget to reflect the new value,
    and calls the `adjust_entry_font_size` method to adjust the font size of the text if necessary.
    """


def clear_all(self):
    """
    Clear the UI entry widget and history, and reset other UI elements.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method clears the current value from the UI entry widget and sets it to zero. It also clears any existing
    entries from the history list widget, and calls the `adjust_entry_font_size` method to adjust the font size of the
    entry widget text if necessary.
    """


def clear_entry(self):
    """
    Clear the UI entry widget.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method clears the current value from the UI entry widget and sets it to zero. It also calls the
    `adjust_entry_font_size` method to adjust the font size of the entry widget text if necessary.
    """


def backspace(self):
    """
    Delete the last character from the UI entry widget.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method removes the last character from the text in the UI entry widget, if it is not already empty. If the entry
    widget contains only a negative sign and no other digits, this method sets the widget value to zero.

    Additionally, this method calls the `adjust_entry_font_size` method to adjust the font size of the entry widget text
    """


def clear_history_if_equality(self):
    """
    Clears the history if the last operation performed was an equality operation.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Description:
    ------------
    This method checks if the last operation performed was an equality operation by calling the `get_history_sign`
    method. If the result of the method is `=`, then it clears the history widget.

    """


def remove_trailing_zeroes(number: str):

  """
  Remove trailing zeroes from a given number string.

  Parameters:
  -----------
  number : str
    A string representing the number to remove trailing zeroes from.

  Returns:
  --------
  str
    A string representing the number with trailing zeroes removed.

  Description:
  ------------
    This function takes a number string as input, converts it to a float, and then back to a string with trailing zeroes
    removed. If the input string represents an error (i.e. "error"), the function returns the input string.
   """


def get_entry_number(self):
    """
    @brief Gets the number from entry from the calculator display.
    @return The number from the calculator display.
    """


def get_history_number(self):
    """
    @brief Gets the number from history from the calculator display.
    @return The number from the calculator display.
    """


def get_history_sign(self):
    """
    @brief Gets the math sign from history from the calculator display.
    @return The math sign from the calculator display.
    """


def get_entry_text_width(self):
    """
    @brief Gets the width of the entry text.
    @return The width of the entry text.
    """


def get_history_text_width(self):
    """
    @brief Gets the width of the history text.
    @return The width of the history text.
    """


def binary_calculate(self, math_sign: str):
    """
    @brief Calculates the result of the binary operation and displays it on the calculator UI.
    @This function retrieves the first operand and the operator from the calculator history and
    the second operand from the calculator entry.
    It then calculates the result of the binary operation and displays it on the calculator entry
    while also updating the calculator history.
    @return The calculated result as a string, or None if an error occurred during the calculation.
    """


def unary_calculate(self, math_sign):
    """
    @brief Calculates the result of the unary operation and displays it on the calculator UI.
    @This function retrieves the operand and the operator from the calculator entry.
    It then calculates the result of the unary operation and displays it on the calculator entry.
    @return The calculated result as a string, or None if an error occurred during the calculation.
    """


def show_error(self):
    """
    @brief Displays an error message on the calculator UI.
    @return None
    """


def remove_error(self):
    """
    @brief Removes the error message from the calculator UI.
    @return None
    """


def disable_buttons(self):
    """
    @brief Disables or enables all buttons in the calculator.
    @param disable A boolean value indicating whether to disable (True) or enable (False) the buttons.
    This function disables or enables all buttons in the calculator based on the value of the
    'disable' parameter. If 'disable' is True, all buttons are disabled and their color is changed.
    If 'disable' is False, all buttons are enabled and their color is changed back to the original color.
    @return None
    """


def change_buttons_color(self, css_color: str):
    """
    @brief Changes the color of all buttons in the calculator.
    @param css_color The color to change the buttons to.
    This function changes the color of all buttons in the calculator to the color specified by the
    'css_color' parameter.
    @return None
    """


def return_button_color(self, button):
    """
    @brief Returns the color of a button.
    @param button The button to get the color of.
    @return The color of the button.
    """


def adjust_entry_font_size(self):
    """
    @brief Adjusts the font size of the entry text.
    @return None
    """


def resizeEvent(self, event):
    """
    @brief Handles the resize event for the calculator.
    @param event The resize event to handle.
    @return None
    """


def math_operation(self, math_sign: str):
    """
    @brief Performs a math operation.
    @param math_sign The math sign to perform.
    @return None
    """


def add_history(self, math_sign: str):
 """
    Adds the current entry and the math sign to the history widget.

    Parameters:
    -----------
    math_sign : str
        The math symbol to add to the history.

    Returns:
    --------
     None

     Description:
     ------------
    This method adds the current entry and the math sign to the history widget, clearing the entry afterwards.
    If the history widget is empty or the last operation performed was an equality operation, it creates a new
    history string using the current entry and the math symbol. It replaces the dot with a comma for localization.
    Finally, it sets the text of the history widget to the new string and sets the entry text to "0".
 """
