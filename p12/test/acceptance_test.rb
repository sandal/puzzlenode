require_relative "helper"

CURRENT_DIR = File.expand_path(File.dirname(__FILE__))

describe "The seekrit executable" do
  it "must be able to crack the sample code" do
    results = `ruby #{CURRENT_DIR}/../bin/decoder data/input.txt` 
    results.must_equal(File.read("#{CURRENT_DIR}/../data/sample_output.txt").strip)
  end
end
