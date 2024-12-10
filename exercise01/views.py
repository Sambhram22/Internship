from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    form = StudentForm()
    student_details = ""
    percentage = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Extract student details
            student_data = form.cleaned_data
            total_marks = (
                student_data["marks_english"] +
                student_data["marks_physics"] +
                student_data["marks_chemistry"]
            )
            percentage = (total_marks / 300) * 100

            # Format the student details
            student_details = f"""
                Name: {student_data['name']}
                Date of Birth: {student_data['date_of_birth']}
                Address: {student_data['address']}
                Contact Number: {student_data['contact_number']}
                Email ID: {student_data['email_id']}
                Marks - English: {student_data['marks_english']}, 
                        Physics: {student_data['marks_physics']}, 
                        Chemistry: {student_data['marks_chemistry']}
            """

    return render(request, 'students/student_form.html', {
        'form': form,
        'student_details': student_details,
        'percentage': percentage,
    })
