#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

require 'csv'

# Calculate Euclidean distance
def calc_dist(a, b)
end

# Load the training and test instances into two arrays
def load_data(partition)
  test = []
  train = []
  CSV.foreach(ARGV[0]) do |row|
    Random.new.rand(1.0) < partition ? train.push(row) : test.push(row)
  end
  return train, test
end

abort "Usage: #{$PROGRAM_NAME} <data_file> <partition>" if ARGV.length != 2
train, test = load_data(partition)

# EOF.
