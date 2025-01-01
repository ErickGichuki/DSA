# initialize a variable to store the the max pothole indicator(max_indicator)
# set a variable to keep track of the legth of the current group of consecutive potholes(current_length)
# init a var to track the max depth within the current group of potholes(current_max_depth)
# iterate thru the arr R
# if the element is greater than 0(implies a pothole);
#  increment current_length by 1, 
# update current_max_depth to be max of current_max_depth adn the current element's depth
# if 0;
# calculate the pothole indicator for the current group(if current_length>0)
# update max_indicator if the current group indicator is larger.
# Reset current_length and current_max_depth for the next group
# Return max_indicator

def solution(R):
    max_indicator = 0
    current_length = 0
    current_max_depth = 0

    for depth in R:
        if depth > 0:
            current_length += 1
            current_max_depth = max(current_max_depth, depth)
        else:
            if current_length >0:
                current_indicator = current_length * current_max_depth
                max_indicator = max(max_indicator, current_indicator)
                current_length = 0
                current_max_depth = 0
        
    if current_length > 0:
        current_indicator = current_length * current_max_depth
        max_indicator = max(max_indicator, current_indicator)

    return max_indicator

R = [9,8,7,0,0,0,2,3,6,4]
print(solution(R))