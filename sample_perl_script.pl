#!/usr/bin/perl
use strict;
use warnings;
use Time::HiRes qw(gettimeofday tv_interval);

# Start time
my $start_time = [gettimeofday];

# Sample task: Print messages and loop
print "Hello, World!\n";

for my $i (1..5) {
    print "Counting: $i\n";
}

# End time
my $elapsed = tv_interval($start_time);

# Print execution time
printf("Execution time: %.6f seconds\n", $elapsed);