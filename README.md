Simple Calculator
GOAL DEADLINE:  

Your final project is a chance to make any interesting application you would like. Design a final project that you can complete in two weeks. Follow these steps:

Step 1: Think of an idea
A simple calculator application that performs basic arithmetic operations (addition, subtraction, multiplication, and division). The calculator will have a graphical user interface (GUI) with buttons for digits and operations, and a display area to show the result.
Step 2: Reflect
Fantastic! That sounds like a well scoped project. We have some questions to help you think about your project idea. Take some time to think about them and write your answers below.

Feel free to write as much or as little as you want, or to say if you're not sure about anything. The more accurate your answers are, the better we can help you come up with a plan.

Your calculator app sounds great! What kind of design are you thinking about for the GUI? Do you have a specific layout or color scheme in mind?

I chose this project because it is manageable within the given time frame, and it allows me to apply what I've learned about Python, loops, and GUI development. A calculator is a useful tool, and building one will reinforce my understanding of event handling and basic arithmetic operations.
For the GUI design of the simple calculator app, I want it to be clean, intuitive, and easy to use. 
A light grey or white background for the entire application to keep it simple and clean.
White background with black text for clear readability.
Sounds good! Have you thought about how users will interact with the calculator? For example, will they click buttons with their mouse or type on their keyboard?

Mouse Interaction the users will primarily interact with the calculator by clicking on the buttons with their mouse. Each button (digits, operators, clear, and equals) will be clickable, triggering the corresponding action and for the keyboard Interaction Users will also have the option to type numbers and operators directly using their keyboard. This will allow for faster input compared to clicking buttons.
That's a solid plan. Have you considered how you will handle invalid inputs or errors, like division by zero or entering multiple operators in a row?

Yea, 
Division by Zero----> Using a try-except block around the evaluation function to catch division by zero and other evaluation errors, displaying an "Error" message.
Multiple Operators---> Validating input before updating the display to prevent consecutive operators. For example, checking if the last character is an operator before adding another.
Great! How do you plan to structure your code to handle different parts of the calculator, like updating the display, performing calculations, and handling user input?

Updating the Display:
button_click(item): Adds the clicked button's value to the display.
button_clear(): Clears the display.
Performing Calculations:
button_equal(): Evaluates the expression in the display, handles errors, and updates the display with the result or an error message.
Handling User Input:
key_press(event): Processes keyboard inputs and calls the appropriate functions based on the input.
Anything else we should know when building milestones?

Step 3: Plan Milestones
There are many ways to approach your project, but here's one. If you need some help getting started, here's a guide to help you through the process. You can mark each step as completed as you go.

Of course, feel free to take your own path. It's the journey that matters, not the destination.

Set Up Your Graphics Window
Start by creating a simple window for your calculator GUI. Use the graphics library to draw a window with a defined size and title, and set the background color to light grey or white as you planned.

Here are some resources that might help you with this step:
Lesson: Graphics
Reading: Graphics Shapes
Worked Example: Programming is Awesome
Here are some terms you might need to know for this step:
GUI: Graphical User Interface, which allows users to interact with electronic devices using graphical icons and visual indicators.
Create Buttons for Digits and Operations
Add buttons for the digits (0-9) and basic arithmetic operations (+, -, *, /). Make sure each button is clickable and arranged in a grid layout. Assign each button a unique identifier that will help you recognize it when clicked.

Here are some resources that might help you with this step:
Lesson: Graphics
Worked Example: Centered Square
Here are some terms you might need to know for this step:
Grid Layout: A layout where the interface elements are arranged in a grid of rows and columns.
Implement User Input Handling
Write functions to handle button clicks and keyboard inputs. Define a function to capture mouse clicks on buttons and another function to handle keyboard presses. Update the display based on the input received.

Here are some resources that might help you with this step:
Lesson: Animation
Worked Example: Mouse Tracker
Here are some terms you might need to know for this step:
Event Handling: The process of responding to user actions, such as mouse clicks or key presses, within a software application.
Update the Display
Create functions to update the calculator's display area when buttons are pressed or keys are typed. Ensure the display shows the current input and results clearly.

Here are some resources that might help you with this step:
Reading: Graphics Shapes
Perform Calculations
Implement the functionality to evaluate the arithmetic expressions input by the user. Use functions to perform addition, subtraction, multiplication, and division. Include error handling for invalid inputs and division by zero.

Here are some resources that might help you with this step:
Worked Example: Print Divisors
Here are some terms you might need to know for this step:
Evaluate: To calculate the value of an expression.
Error Handling: The process of gracefully managing errors that occur during the execution of a program.
Test and Refine Your Calculator
Thoroughly test your calculator to ensure all buttons and functions work as expected. Handle edge cases such as multiple consecutive operators and invalid inputs. Refine the GUI for a clean and intuitive user experience.

Here are some terms you might need to know for this step:
Edge Case: A problem or situation that occurs only at an extreme (maximum or minimum) operating parameter.
Enhance Your Calculator (Optional)
If you have extra time, consider adding additional features such as a more advanced GUI layout, additional mathematical functions (e.g., square root, exponentiation), or a history of calculations.
