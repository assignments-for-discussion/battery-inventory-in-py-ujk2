
def count_batteries_by_usage(cycles):
  lowCount = 0
  mediumCount = 0
  highCount = 0
 
  for i in cycles:
    if i<=0:
      continue
    if i < 410:
      lowCount = lowCount+1
        elif i >= 410 and i <= 949:
          mediumCount = mediumCount+1
        elif i >= 950:
          highCount = highCount+1
  return {
    "lowCount": lowCount,
    "mediumCount": mediumCount,
    "highCount": highCount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
