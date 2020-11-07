#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov
# k nearest-neighbot with k = 1

require 'csv'

def calc_dist(a, b)
  Math::sqrt(a[0...-1].zip(b).inject(0) { |sum, e| sum += (e[0] - e[1])**2 })
end

def load_data(file, part, train, test)
  train = []; test = []
  CSV.foreach(file) do |row|
    rf = row.map(&:to_f)
    Random.new.rand(1.0) < part ? train << rf : test << rf
  end
  return train, test
end

abort "Usage: #{$PROGRAM_NAME} <file> <partition>" if ARGV.length != 2
train = []; test = []
until train.length > 0 and test.length > 0 do
  train, test = load_data(ARGV[0], ARGV[1].to_f, train, test)
end
puts "Number of training instances: #{train.length}"
puts "Number of test instances: #{test.length}"
test.each do |r|
  min_dist = calc_dist(r, train[min_index = 0])
  (1...train.length).each do |i|
    dist = calc_dist(r, train[i])
    if dist < min_dist
      min_dist = dist
      min_index = i
    end
  end
  puts "prediction: #{train[min_index][-1]}, actual: #{r[-1]}"
end

# EOF.
