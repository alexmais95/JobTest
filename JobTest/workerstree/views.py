from django.http import HttpResponseRedirect
from django.shortcuts import render
from workerstree.models import *
from django.db import connection
from workerstree.form import *
from django.http import JsonResponse



def position_list(requests):
    position = Workers.objects.all()

    return render(requests, 'workerstree/center/center.html', {'position': position})


def get_position(requests, pk):
    worker = Workers.objects.get(pk=pk)

    return render(requests, 'workerstree/center/center.html', {'worker': worker})


def add_workers_to_db(full_name, job_position, date, email, position):
    Workers.objects.create(fullName = full_name,
                           job_position = job_position,
                           date = date,
                           email = email,
                           position = position
                           )
    

def add_workers(requests):
    if requests.method == 'POST'and requests.is_ajax():
        form = AddWorker(requests.POST)
        if form.is_valid():
            full_name = form.cleaned_data["fullName"]
            job_position = form.cleaned_data["job_position"]
            date = form.cleaned_data["date"]
            email = form.cleaned_data["email"]
            position = form.cleaned_data["position"]
            
            add_workers_to_db(full_name, job_position, date, email, position)
            form.save()
            return JsonResponse({'name':full_name}, status = 200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

            
    else:
        form = AddWorker()

    return render(requests, 'workerstree/center/add_worker.html', {'form': form})




def get_worker_by_position(requests, position):
    position_worker = my_db(position)
    return render(requests, 'workerstree/center/workers_by_position.html', {'detail':position_worker})


def my_db(position):
    with connection.cursor() as cursor:
        cursor.execute(f'''
                    SELECT workerstree_position.name, workerstree_workers."fullName"
                    FROM workerstree_position
                    INNER JOIN workerstree_workers
                    ON workerstree_position.id = workerstree_workers.position_id
                    WHERE workerstree_position.name = '{position}';
                    
                    ''')
        
        row = dictfetchall(cursor)

    return row



def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
        ]