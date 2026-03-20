n = int(input()) #input for how many students
student_marks = {} #empty dictionary to store students and marks
for _ in range(n): #loop for run n times
    name, *line = input().split() #split input into name and marks(Krish 67 68 69)
    scores = list(map(float, line)) #convert int to float
    student_marks[name] = scores #add entry to dictionary
query_name = input() #take student name input
scores=student_marks[query_name] #take scores of that particular selected student
average=sum(scores)/len(scores) #find average
print(f"{average:.2f}") #print average with 2 decimals at last

