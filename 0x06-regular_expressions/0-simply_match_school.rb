#!/usr/bin/env ruby
if ARGV.length != 2
    exit 1
end
reg = ARGV[1]
matches = reg.scan(/School/)
puts "{matches}"
