data = {
   'students' : [
       {
           'name' : 'Salvador Vizcaino',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
       {
           'name' : 'Edgar Torres',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
       {
           'name' : 'Galileo Guzman',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
       {
           'name' : 'Liz Rueda',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
       {
           'name' : 'Met Velazquez',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
       {
           'name' : 'Salvador Vizcaino',
           'class': 2015,
           'scores' : [10,8,8,6.9,8.9,8.9]
       },
        {
           'name' : 'Mario Rueda',
           'class': 2015,
           'scores' : []
       }
   ]
}

print('Data pura_________________________')
print(len(data['students']))
print(data['students'])
print('-------------------')

def student_with_scores(student):
    scores = student.get('scores', [])
    if len(scores) >= 1:
        return True
    return False

print('Data estudiantes con calificaciones_________________________')
qualified_students = list(filter(student_with_scores, data['students']))
print(len(qualified_students))
print(qualified_students)

def final_score(student):
    scores = student.get('scores', [])
    scores_sum = 0
    for s in scores:
        scores_sum = scores_sum + s
        result = scores_sum / len(scores)
    return round(result, 2)

print('Data final scores con arreglo for_________________________')
students_final_scores = list(map(final_score, qualified_students))
print('--------------------')
print(students_final_scores)


def apply_final_score(student):
    scores = student['scores']
    results = sum(scores) / len(scores)
    student['final_score'] = round(results,2)
    return student

print('Data con arreglo en función_________________________')
students_with_final_score = list(map(apply_final_score, qualified_students))
print('----------------------')
print(students_with_final_score)


