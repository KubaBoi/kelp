
method print_char(bit message){ $OUT 1 message; }

method print_dec(bit message){ $OUT 2 message; }

method sum2(bit8 dest, bit8 a1, bit8 a2)
{
    dest = a1 + a2;
}
// ahoj
method sum(bit8 dest, bit8 a1, bit8 a2)
{
    sum2(dest, a1, a2);
}

method main(bit args)
{
    bit8 num1 = 5; // jj
    bit8 num2 = 4; //d asdasd
    bit8 result;
    bit8 break = '\n'; //dasaf
    sum(result, num1, num2);
    print_dec(result);
    print_char(break);
}