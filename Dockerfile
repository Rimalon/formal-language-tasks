FROM graphblas/pygraphblas-minimal:v3.3.3
RUN pip3 install pyformlang
COPY . ./formal-language-tasks
WORKDIR ./formal-language-tasks