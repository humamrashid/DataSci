#!/usr/bin/ruby

# Humam Rashid
# CISC 7700X, Prof. Sverdlov
# k nearest-neighbor with k = 1

require 'csv'
require 'confusion-matrix'

def calc_dist(a, b)
  Math::sqrt(a[0...-1].zip(b).inject(0) { |sum, e| sum += (e[0] - e[1])**2 })
end

abort "Usage: #{$PROGRAM_NAME} <file> <partition>" if ARGV.length != 2
train = []; test = []
cm = ConfusionMatrix.new
until train.length > 0 and test.length > 0 do
  CSV.foreach(ARGV[0]) do |row|
    rf = row.map(&:to_f)
    Random.new.rand(1.0) < ARGV[1].to_f ? train << rf : test << rf
  end
end
test.each do |r|
  min_dist = calc_dist(r, train[min_index = 0])
  (1...train.length).each do |i|
    dist = calc_dist(r, train[i])
    if dist < min_dist
      min_dist = dist
      min_index = i
    end
  end
  actual = r[-1]
  assigned = train[min_index][-1]
  cm.add_for(actual, assigned)
  puts "prediction: #{assigned}, actual: #{actual}"
end
puts "Accuracy: #{cm.overall_accuracy}"

# EOF.
