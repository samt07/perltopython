#!/usr/bin/perl
use strict;
use warnings;
use Time::HiRes qw(gettimeofday tv_interval);

my $start_time = [gettimeofday];

my @array = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5);

# Remove duplicates and sort
my @unique_sorted = sort { $a <=> $b } keys %{{ map { $_ => 1 } @array }};

my $elapsed_time = tv_interval($start_time);

print "Sorted unique array: @unique_sorted\n";
printf "Execution time: %.6f seconds\n", $elapsed_time;