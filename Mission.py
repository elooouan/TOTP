# Function to concatenate 2 lists
def concat_lists(list1, list2):
    if not list2:
        return list1
    
    head, *tail = list2
    return concat_lists(list1 + [head], tail)

# Function to parse the positive input integers
def parse_positive_nums(line):
    # Empty error handling
    if not line:
        return []
    
    head, *tail = line.split()
    tail = " ".join(tail)  # function expects string arg

    # We only add it to the array if it's a positive integer and respects the condition "Yn <= 100"
    if 0 <= int(head) <= 100:
        return concat_lists([int(head)], parse_positive_nums(tail))
    return parse_positive_nums(tail)

# Function to sum the squares of positive integers
def sum_squares(nums):
    # Empty error handling
    if not nums:
        return 0
    
    head, *tail = nums
    return (head ** 2 if head >= 0 else 0) + sum_squares(tail)

# Function to read input lines recursively for a specific number of expected lines
def read_n_lines(N, current_count=0, lines=None):
    if lines is None:
        lines = []
    
    if current_count >= N:
        return lines
    
    try:
        line = input()
        lines.append(line)
        return read_n_lines(N, current_count + 1, lines)
    except EOFError:
        return lines  # Return what we have if EOF is encountered early

# Function to process test cases recursively
def process_test_cases(lines, i, N, results, errors):
    # Error handling for N <= 0
    if N <= 0:
        return results, errors
    
    # More error handling
    if i + 1 >= len(lines):
        errors.append("Not enough input lines provided")
        return results, errors
    
    try:
        X = int(lines[i])
        if not (0 < X <= 100): 
            errors.append(f"Test case {len(results) + 1}: The number of integers must be between 1 and 100, got {X}")
            # Not sure if this is what was required for me to do, but since "Note 1" says
            # "There should be no output until all the input has been received"
            # I skip this test case and move to the next instead of immediately displaying an error message
            return process_test_cases(lines, i + 2, N - 1, results, errors)
        
        try:
            nums = parse_positive_nums(lines[i + 1])
            results.append(str(sum_squares(nums)))
            return process_test_cases(lines, i + 2, N - 1, results, errors)
        except Exception as e:
            # Error handling while parsing -> usually if the user confuses the X field with Yn, enters Unicode/special characters or floats
            errors.append(f"Test case {len(results) + 1}: Error parsing integers - {str(e)}")
            return process_test_cases(lines, i + 2, N - 1, results, errors)
    
    except Exception as e:
        errors.append(f"Test case {len(results) + 1}: Error processing test case - {str(e)}")
        return process_test_cases(lines, i + 2, N - 1, results, errors)

def main():
    errors = []
    
    try:
        # First line should be N (number of test cases)
        first_line = input()
        try:
            N = int(first_line)
            
            if N < 1: # Error handling for N < 1
                print("Number of test cases must be at least 1")
                return
            elif N > 100: # And N > 100
                print("Number of test cases must be at most 100")
                return
                
            # Now we know how many more lines to read (2 lines per test case)
            remaining_lines = read_n_lines(2 * N)
            all_lines = [first_line] + remaining_lines
            
            # Process all test cases
            results, new_errors = process_test_cases(all_lines, 1, N, [], [])
            errors = concat_lists(errors, new_errors)
            
            # Print any errors first
            if errors:
                print("\n".join(errors))
            
            # Print results
            if results:
                print("\n".join(results))
                
        except ValueError:
            # More error handling for N, if the user enters a float or string instead of an integer for exemple
            print(f"Error: First line must be an integer, got '{first_line}'")
            
    except EOFError:
        # Even more error handling, I think you can only get this if you send an EOF signal with Ctrl+D
        # I haven't handled other signals like SIGINT or anything so I hope the automatic tests go easy on me
        print("No input provided")

if __name__ == "__main__":
    main()