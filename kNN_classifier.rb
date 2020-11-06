#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

require 'csv'

def load_data
  train = []
  test = []
  CSV.foreach(ARGV[0]) do |row|
    if Random.new.rand(1.0) < 0.8
      train.push(row)
    else
      test.push(row)
    end
  end
  return train, test
end

abort "Usage: #{$PROGRAM_NAME} <data_file>" if ARGV.length != 1
train, test = load_data

# EOF.
