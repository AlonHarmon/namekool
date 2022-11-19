# namekool
Infrastracture for deploying nameko function


# Example

to use namekool create a dockerfile containing `handelr.py`.
that file should contain the function you wish to deploy named `handle`

example docker file:
``` Dockerfile

FROM namekool

COPY requirements.txt .
COPY handler.py .

RUN pip install requirements.txt

# envs

```
