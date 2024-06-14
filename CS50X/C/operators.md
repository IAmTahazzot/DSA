# C Operators

Operators in C are symbols that tell the compiler to perform specific mathematical or logical manipulations. They are used in the program to manipulate data and variables. C operators can be classified into several types:

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

- **Addition (`+`)**: Adds two operands. 
  - **Example**: `a + b`
- **Subtraction (`-`)**: Subtracts the second operand from the first. 
  - **Example**: `a - b`
- **Multiplication (`*`)**: Multiplies both operands. 
  - **Example**: `a * b`
- **Division (`/`)**: Divides the numerator by the denominator. 
  - **Example**: `a / b`
  - **Note**: If both operands are integers, the result is an integer (the fractional part is discarded).
- **Modulus (`%`)**: Returns the remainder of division. 
  - **Example**: `a % b`
  - **Note**: Only works with integers.

## 2. Relational Operators

Relational operators compare two values and determine the relationship between them.

- **Equal to (`==`)**: Checks if the values of two operands are equal. 
  - **Example**: `a == b`
- **Not equal to (`!=`)**: Checks if the values of two operands are not equal. 
  - **Example**: `a != b`
- **Greater than (`>`)**: Checks if the value of the left operand is greater than the value of the right operand. 
  - **Example**: `a > b`
- **Less than (`<`)**: Checks if the value of the left operand is less than the value of the right operand. 
  - **Example**: `a < b`
- **Greater than or equal to (`>=`)**: Checks if the left operand is greater than or equal to the right operand. 
  - **Example**: `a >= b`
- **Less than or equal to (`<=`)**: Checks if the left operand is less than or equal to the right operand. 
  - **Example**: `a <= b`

## 3. Logical Operators

Logical operators are used to combine two or more conditions.

- **Logical AND (`&&`)**: Returns true if both statements are true. 
  - **Example**: `a > b && c > d`
- **Logical OR (`||`)**: Returns true if at least one statement is true. 
  - **Example**: `a > b || c > d`
- **Logical NOT (`!`)**: Reverses the logical state of its operand. If a condition is true, then Logical NOT operator will make it false. 
  - **Example**: `!a`

## 4. Bitwise Operators

Bitwise operators perform bit-level operations on the operands.

- **AND (`&`)**: Performs a bitwise AND operation between two operands.
  - **Example**: `a & b`
- **OR (`|`)**: Performs a bitwise OR operation between two operands.
  - **Example**: `a | b`
- **XOR (`^`)**: Performs a bitwise XOR operation between two operands.
  - **Example**: `a ^ b`
- **NOT (`~`)**: Performs a bitwise NOT operation, inverting each bit of its operand.
  - **Example**: `~a`
- **Left Shift (`<<`)**: Shifts the bits of the first operand to the left by the number of positions specified by the second operand.
  - **Example**: `a << 2`
- **Right Shift (`>>`)**: Shifts the bits of the first operand to the right by the number of positions specified by the second operand.
  - **Example**: `a >> 2`

## 5. Assignment Operators

Assignment operators are used to assign values to variables.

- **Simple assignment (`=`)**: Assigns the value of the right operand to the left operand.
  - **Example**: `a = b`
- **Add and assign (`+=`)**: Adds the right operand to the left operand and assigns the result to the left operand.
  - **Example**: `a += b` (equivalent to `a = a + b`)
- **Subtract and assign (`-=`)**: Subtracts the right operand from the left operand and assigns the result to the left operand.
  - **Example**: `a -= b` (equivalent to `a = a - b`)
- **Multiply and assign (`*=`)**: Multiplies the right operand with the left operand and assigns the result to the left operand.
  - **Example**: `a *= b` (equivalent to `a = a * b`)
- **Divide and assign (`/=`)**: Divides the left operand by the right operand and assigns the result to the left operand.
  - **Example**: `a /= b` (equivalent to `a = a / b`)
- **Modulus and assign (`%=`)**: Takes modulus using two operands and assigns the result to the left operand.
  - **Example**: `a %= b` (equivalent to `a = a % b`)

Understanding these operators and their precedence (which determines the order they are applied in expressions) is crucial for writing effective C programs.