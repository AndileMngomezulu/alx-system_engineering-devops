#!/usr/bin/env ruby
# repetition

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
