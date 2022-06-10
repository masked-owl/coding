function Add-Numbers
{
    param([int]$n1, [int]$n2)
    $answer=$n1+$n2
    return $answer
}

$x = Add-Numbers 3 4
$x += Add-Numbers 1 2
$x