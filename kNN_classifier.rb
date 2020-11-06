#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

require 'csv'

# Calculate Euclidean distance
def calc_dist(a, b)
  Math::sqrt(a[0...-1].zip(b).inject(0) { |sum, e| sum += (e[0] - e[1])**2 })
end

# Load the training and test instances into two arrays
def load_data(file, part, train, test)
  CSV.foreach(file) { |r| Random.new.rand(1.0) < part ? train << r : test << r }
end

def main
  abort "Usage: #{$PROGRAM_NAME} <file> <partition>" if ARGV.length != 2
  train = []; test = []
  load_data(ARGV[0], ARGV[1].to_f, train, test)
  puts calc_dist([1,2,3], [4,5,6])
end

main

# EOF.
