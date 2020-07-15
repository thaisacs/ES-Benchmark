# Trabalho - MO833

 Para executar o NPB local, basta seguir os comandos a seguir:
 
 ```
 # NPB
 cd ES-Benchmark/NPB3.4-MPI/experiments
 ./script-build.sh
 ./script-exp.sh
  ```
  Já para executar o Pyranda, basta executar os seguintes comandos:
  
   ```
# Pyranda
 cd ES-Benchmark/pyranda/experiments
 source script-build.sh
 ./script-exp.sh
 ```
# Experimentação na Nuvem Computacional

Com o python3, git e CLAP instalados, execute os seguintes comandos:

```
git clone https://github.com/thaisacs/ES-Benchmark --recursive
ssh-keygen -b 2048 -t rsa -f /home/seu-user/.clap/private/id_rsa -q -N ""
```

Com o virtual-env do clapp ativado basta executar os seguintes comandos:

```
cd ES-Benchmark/experiments/creation-deletion-scripts
python3 run-creation.py
```

Após a finalização desses comandos será fornecido o EFS IP na tela. Configure o arquivo execution-scripts/config.yml com esse IP e com as informações das aplicações que devem ser executadas. Depois, basta executar os seguintes comandos:

```
cd ../execution-scripts
python3 run-compile.py
python3 run-experiment.py
cd ../creation-deletion-scripts/
python3 run-deletion.py
```

No final, os dados irão para o diretório /experiments/experimental_results. Para gerar os gráficos basta executar os seguintes comandos:

```
cd ../charts-csv-scripts
./charts-csv.sh
./charts-run.sh
cd speedup
python3 speedup.py
cd summary
python3 generator-summary.py
python3 chart-mean.py
```

