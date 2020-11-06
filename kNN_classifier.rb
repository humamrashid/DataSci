#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

require 'csv'

# Calculate Euclidean distance
def calc_dist(a, b)
end

# Load the training and test instances into two arrays
def load_data(file, partition, train, test)
  r = Random.new.rand(1.0)
  CSV.foreach(file) {|row| r < partition ? train << row : test << row}
end

abort "Usage: #{$PROGRAM_NAME} <data_file> <partition>" if ARGV.length != 2
load_data(ARGV[0], partition, train, test)

# EOF.
