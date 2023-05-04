
method print_str(byte message){ $OUT 0 message; }
method print_char(byte message){ $OUT 1 message; }
method print_dec(byte message){ $OUT 2 message; }

method sum(byte1 dest, byte1 a1, byte1 a2)
{
    $SUM dest a1 a2;
}
// ahoj
method sumis(byte1 dest, byte1 a1, byte1 a2)
{
    sum(dest, a1, a2);
}

method main(byte args)
{
    byte string = "Hello fakin world!!!!!!!!\n";
    print_str(string);

    byte1 num1 = 5; // jj
    byte1 num2 = 4; //d asdasd
    byte1 result;
    byte1 break = '\n'; //dasaf
    byte plus = " + ";
    byte eq = " = ";
    byte arr = [0, 5, 45, '\n', 'n'];
    sumis(result, num1, num2);
    print_dec(num1);
    print_str(plus);
    print_dec(num2);
    print_str(eq);
    print_dec(result);
    print_char(break);
}