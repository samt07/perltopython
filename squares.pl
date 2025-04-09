use Time::HiRes qw(time);  # More precise timing

$start_time = time();

@numbers = (1, 2, 3, 4, 5);
@squares = ();

$i = 0;
while ($i < scalar(@numbers)) {
    $num = $numbers[$i];

    $square = 0;
    $k = 0;
    while ($k < $num) {
        $square = $square + $num;
        $k = $k + 1;
    }

    push(@squares, $square);
    $i = $i + 1;
}

$j = 0;
print "Squares:\n";
while ($j < scalar(@squares)) {
    print $squares[$j], "\n";
    $j = $j + 1;
}

$end_time = time();
$duration = $end_time - $start_time;

# Print with 6 decimal places
printf("Execution Time: %.6f seconds\n", $duration);
