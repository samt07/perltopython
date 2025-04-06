#!/usr/bin/perl
use strict;
use warnings;
use Time::HiRes qw(gettimeofday tv_interval);

# Start the timer
my $start_time = [gettimeofday];

# Hard-coded data
my @numbers = (14, 7, 21, 9, 3, 12, 5, 18);

# Calculate sum and average
my $sum = 0;
foreach my $num (@numbers) {
    $sum += $num;
}
my $average = $sum / scalar(@numbers);

# Find min and max
my $min = $numbers[0];
my $max = $numbers[0];
foreach my $num (@numbers) {
    $min = $num if $num < $min;
    $max = $num if $num > $max;
}

# Sort the array
my @sorted = sort { $a <=> $b } @numbers;

print "Numbers: " . join(", ", @numbers) . "\n";
print "Sum: $sum\n";
printf "Average: %.2f\n", $average;
print "Min: $min\n";
print "Max: $max\n";
print "Sorted: " . join(", ", @sorted) . "\n";

# Calculate and display execution time
my $end_time = [gettimeofday];
my $execution_time = tv_interval($start_time, $end_time);
printf "Execution time: %.6f seconds\n", $execution_time;