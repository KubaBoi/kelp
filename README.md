# Kelp

Kelp is language specially for LilyGo TWatch 2020 environment. Programs run via virtual machine.

Virtual machine documentation is ./VM_README.md .

## Methods

Methods are define as `method name(args) {code}`. To return use the `return` keyword without any arguments (this is not necessary at the end of method).

Example:

```c
method example_method(byte1 argument)
{
    byte1 a = 0;
}
```

Methods can have an overload, but every definition need to has different count of arguments.

```c
method create(byte arg)
{
    arg = "ahoj";
}

method create(byte arg0, byte arg1)
{
    arg0 = "ahoj";
    arg1 = [52];
}
```

## Data types

There are not static data types. Every variable is just "array" of bytes and the size of this array is defined in data type specification:

```c
byte1 char = 10; // 1 byte will be allocated and set value to 10
byte2 short = 258; // 2 bytes will be allocated and set values to 2 1
byte3 something = 23; // 3 bytes will be allocated and set values to 23 0 0
byte4 int = 5; // 4 bytes will be allocated and set values to 5 0 0 0
.
.
.
```

But there is also option to not specify size:

```c
byte string1; // variable string1 will be defined but no allocations are done
// allocation for 17 bytes will be done
// and also set instruction will be done
// 17 bytes because "Hello world! :)\n" is 16 chars long plus ending 0
string1 = "Hello world! :)\n"; 

byte string2 = "Hello :)\n"; // allocation and set of 10 bytes

// arrays are defined as []
// there will be allocation and set for 3 bytes done
byte array = [12, 5, 'a'];

// this approach is not the best practice, better use simple `byte` annotation
// and let the compiler do the job
byte12 string3 = "Hello :)\n"; // allocation of 12 bytes and set of 10 bytes

// errors because allocation byte counts are less than set byte counts
byte2 array_err = [23, 7, 1];
byte2 string_err = "HeeHee\n";
```

## Start of the program

Every program need to have its own `main` method which is than considered as starting point. This `main` method should have exactly 1 argument (this argument will always be `byte` no matter what user define).

The one argument is program input and always will be at address 0.

```c
// arg will be type `byte` even if user defined it as `byte1`
method main(byte1 arg)
{
    // code
}
```

## Raw instructions

Sometimes it would be necessary to use raw instructions. Those structures are something like assembly code. 

Raw instructions are defined with `$` at the start of command and and with `;` at the end.

```c
// print
byte message = "Hello world!\n";
$OUT 0 message;

// sum
byte1 num1 = 5;
byte1 num2 = 4;
byte1 dest;
$SUM dest num1 num2;
```

List of instructions and its usages are in Virtual machine documentation.

Most of default library methods would contains raw instructions. For example simple decimal print:

```c
method print_dec(byte message)
{ 
    $OUT 2 message; 
}
```

## Copying

Every variable is considered to be pointer. So after this procedure:

```c
// case 1
byte1 num1 = 5;
byte num2 = num1;

// case 2
byte1 num1 = 5;
byte1 num2;
$FRE num2;
num2 = num1;
```

will `num1` and `num2` be pointing to same memory address.

To copy value use this syntax:

```c
byte1 num1 = 5;
byte1 num2 = *num1;
```

`num1` and `num2` will have same value but different memory address. In case that `num1` and `num2` do not have same sizes, compilator will print a warning about precision and copied would be the lower count of bytes. 

### Warning!!

If copying address remember to use `byte` data type or `FRE` instruction as in first example. Otherwise `num2` would allocate some memory, but after `CPT` instruction, this allocated memory will be unreachable.

In the second example there is no need to `FRE` instruction because allocated memory will be filled with values;
