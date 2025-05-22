#! /bin/bash

#python manage.py wait_for_db
#python manage.py migrate --noinput
#python manage.py collectstatic --noinput

# Number of recommended workers is 2 x number_of_cores +1
# DO NOT scale the number of workers to the number of clients you expect to have. Gunicorn should only need 4-12 worker
# processes to handle hundreds or thousands of requests per second.
#
# Gunicorn relies on the operating system to provide all of the load balancing when handling requests. Generally we
# recommend (2 x $num_cores) + 1 as the number of workers to start off with. While not overly scientific, the formula is
# based on the assumption that for a given core, one worker will be reading or writing from the socket while the other
# worker is processing a request.
#
# Obviously, your particular hardware and application are going to affect the optimal number of workers. Our
# recommendation is to start with the above guess and tune using TTIN and TTOU signals while the application is under
# load.
#
# Always remember, there is such a thing as too many workers. After a point your worker processes will start thrashing
# system resources decreasing the throughput of the entire system.
#
uvicorn carpet_api.main:app --workers 5 --host 0.0.0.0 --port 8000
