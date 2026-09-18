from django.shortcuts import render, get_object_or_404

from .models import Question, Choice, Submission


def submit(request):
    questions = Question.objects.all()

    if request.method == "POST":
        score = 0
        results = []

        for question in questions:
            answer_key = f"question_{question.id}"
            selected_id = request.POST.get(answer_key)

            if selected_id:
                selected_choice = get_object_or_404(
                    Choice,
                    id=selected_id
                )

                if selected_choice.is_correct:
                    score += 1
                    result = "Correct"
                else:
                    result = "Incorrect"

                Submission.objects.create(
                    question=question,
                    selected_choice=selected_choice
                )

                results.append({
                    "question": question.text,
                    "selected": selected_choice.text,
                    "result": result
                })

        return render(
            request,
            "exam_result.html",
            {
                "score": score,
                "total": questions.count(),
                "results": results
            }
        )

    return render(
        request,
        "exam.html",
        {
            "questions": questions
        }
    )


def show_exam_result(request):
    submissions = Submission.objects.all()

    score = 0
    results = []

    for submission in submissions:
        if submission.selected_choice.is_correct:
            score += 1
            result = "Correct"
        else:
            result = "Incorrect"

        results.append({
            "question": submission.question.text,
            "selected": submission.selected_choice.text,
            "result": result
        })

    return render(
        request,
        "exam_result.html",
        {
            "score": score,
            "total": submissions.count(),
            "results": results
        }
    )
