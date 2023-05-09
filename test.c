typedef void method;
typedef int byte;
typedef int byte1;
typedef int byte2;


/*method print_str(byte message){ $OUT 0 message; }
method print_char(byte message){ $OUT 1 message; }
method print_dec(byte message){ $OUT 2 message; }
method free(byte var) { $FRE var; }
*/
method sum(byte1 dest, byte1 a1, byte1 a2)
{
    $SUM dest a1 a2;
}
// ahoj
/*method sumis(byte1 dest, byte1 a1, byte1 a2)
{
    sum(dest, a1, a2);
}*/

method main(byte args)
{
    byte1 brk = '\n';
    byte1 spc = ' ';
    byte1 one = 1;
    byte1 five = 5;
    
    // for cyklus
    for (byte1 i = 0; i <= five; $SUM i i one;)
    {
        $OUT 2 i;
        $OUT 1 brk;
        if (i == one) 
        {
            $OUT 1 spc;
        }
    }
    $OUT 1 brk;
}