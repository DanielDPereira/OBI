program Hello;

var M, N, Diferenca, Orlando: integer;

begin
    readln(M);
    readln(N);
    
    if (M > N) then
        Diferenca := M - N
        Orlando := Diferenca + M
        writeln(Orlando)
    else
        Diferenca := N - M;
        Orlando := Diferenca + N
    
        writeln(Orlando);
end.

