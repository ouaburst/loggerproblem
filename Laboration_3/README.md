# Laboration 3

## Environment & Tools
[replace this with relevant information]

## Purpose
This lab explores the distinctions between iterative and recursive methods, the intricacies of function decoration, 
efficient file handling, and the practical use of custom loggers. Centered on various Fibonacci sequencing techniques, 
the lab's aim is to accurately measure execution times and present pertinent data through the console and log files. 
The overarching objective is to design and craft a system that consistently measures, logs, and showcases this data to 
the user. The concrete goals for determining success of this study are:

- Initialize and configure **``ass_3_logger``** with its dual handlers. Ensure the console outputs at the **``INFO``** 
level and file outputs at the **``DEBUG``** level, adhering to the defined formatting standards like timestamp, logger 
name, log level, and message content.
- Implement the **``fibonacci_memory(nth_nmb)``** function as per the requirements. This function should offer a 
performance edge over the standard recursive method by utilizing memory, leading to reduced execution time.
- Implement the **``@measurements_decorator``** to monitor the execution times of each Fibonacci function. This 
decorator needs to align with the provided pseudo code, log appropriate information, capture Fibonacci sequences, 
compute durations, and return the correct data to the caller.
- Implement the **``print_statistics(fib_details: dict, nth_nmb: int)``** function, adhering to the stipulated 
guidelines. This function needs to display sequencing statistics in the console, using the designated formatting and 
the supplied helper function for time formatting nuances.
- Implement the **``write_to_file(fib_details: dict)``** function as per the requirements. This function needs to 
generate files with exact Fibonacci details, conform to the specified naming conventions, and store them in the 
**``_Resources``** directory, all while ensuring content format consistency.

## Procedures
[replace this with relevant information]

## Discussion
### Purpose Fulfillment
[replace this with relevant information]

### Alternative Approaches
[replace this with relevant information]

## Personal Reflections
[replace this with relevant information]