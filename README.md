Jan Król

# How to run
1. Install poetry
2. Run ```git clone https://github.com/jkrol1/datumo_task.git```
3. Navigate to datumo_task folder
4. Run ```git checkout Task-implementation``` to switch to branch with task implementation
5. Run ```make install``` if you've got Make utility or ```poetry install```
6. Prepare file with input data. It has to be a txt file with numbers separated by ",". For example "1,2,3,4,5,6" 
7. Run ```poetry run python main.py -i 'path-to-input-file.txt' -o 'path-to-output-file.txt'```