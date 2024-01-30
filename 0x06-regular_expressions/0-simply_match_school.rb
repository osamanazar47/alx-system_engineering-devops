#!/usr/bin/env ruby
if ARGV.length != 1
    exit 1
end
reg = ARGV[0]
matches = reg.scan(/School/)
puts matches.join
