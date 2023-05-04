
method print_char(byte message){ $OUT 1 message; }

method print_dec(byte message){ $OUT 2 message; }

method sum2(byte1 dest, byte1 a1, byte1 a2)
{
    dest = a1 + a2;
}
// ahoj
method sum(byte1 dest, byte1 a1, byte1 a2)
{
    sum2(dest, a1, a2);
}

method main(byte args)
{
    byte1 num1 = 5; // jj
    byte1 num2 = 4; //d asdasd
    byte1 result;
    byte1 break = '\n'; //dasaf
    byte string = "ahoj jak se dneska mas?\n";
    byte arr = [0, 5, 45, '\n', 'n'];
    sum(result, num1, num2);
    print_dec(result);
    print_char(break);
}