# Data Types in Programming

In programming, data types are an essential concept as they define the type of data a variable can hold. Here's a brief overview of some common data types:

1. `int`
2. `char`
3. `float`
4. `double`
5. `void`

## 1. Int (Integer - signed int)

An `int` typically occupies 4 bytes of memory, equivalent to 32 bits. This allocation limits the range of values it can store within the 32-bit boundary.

- **Highest positive number**: $2^{31} - 1$ (2,147,483,647)
- **Lowest negative number**: $-2^{31}$ (-2,147,483,648)

### Unsigned Int

An **unsigned int** differs from a signed int by excluding negative numbers, thus extending its positive range. It uses the bit normally reserved for indicating the sign to store data, effectively doubling the maximum positive value it can represent.

- **Range**: From $0$ to $2^{32} - 1$ (0 to 4,294,967,295), covering approximately 4.29 billion distinct values.

## 2. Char (Character)

A `char` occupies 1 byte of memory, or 8 bits, limiting it to 8 bits of information. This size is sufficient to represent characters using the ASCII encoding, which maps characters (e.g., A, B, C) to numeric values within this range.

- **Character range**: From -128 to 127, covering the full spectrum of ASCII characters and control codes.

## 3. Float (Floating Point)

A `float` uses 4 bytes of memory (32 bits) and is designed to represent fractional numbers. However, it's important to note that floating-point numbers have precision limitations, meaning they may not always represent decimal numbers exactly due to the way they are stored in binary.

## 4. Double (Double Precision Float)

A `double` occupies 8 bytes of memory (64 bits), offering double the precision of a float. This increased size allows for a more accurate representation of decimal numbers, making it suitable for calculations requiring high precision.

## 5. Void

`Void` is unique as it is not a data type in the traditional sense but rather a keyword indicating the absence of data. In function declarations, `void` specifies that the function does not return a value.

## Not Built-In Types:

1. `bool` - Represents boolean values, true or false.
2. `string` - Represents sequences of characters, used for storing text.

Understanding these data types and their limitations is crucial for effective programming, as it influences how data is stored, manipulated, and interpreted within your code.