import csv


import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib as mpl
import matplotlib.ticker as ticker
import os

np.set_printoptions(threshold = np.inf) 

MAIN_SYLLABLES = [23, 34, 56, 66, 98, 28, 37, 38, 48, 63, 99, 59, 72, 77, 92, 13, 29, 32, 62, 3, 46, 52, 89]
INDIVIDUAL_MOLE_RAT_FILE = '/Users/maximiliancomfere/transition_matrix_nakedrats /009-895-085 - baseline OF - M - DOB 6-16-2012 - 10min trim.csv'
MONSTER_MOSEQ_FILE = '/Users/maximiliancomfere/transition_matrix_nakedrats /moseq_df.csv'
AVERAGE_MONSTER_DIRECTORY = None

## add column finder to find the column that syllables exists at 

def worker_matrix_compilier():      
    with open(MONSTER_MOSEQ_FILE, \
        newline='') as csvfile:
        syllablereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        syllables = []
        transitions = []
        newsyllable = 0
        count = 0
        
        for row in syllablereader: 
            if count > 0:
                newsyllable = int(row[6])
                break
            count += 1
                
        for row in syllablereader:  
            if "baseline OF" in row[0]: 
                if int(row[6]) != newsyllable and int(row[6]) in MAIN_SYLLABLES:
                    if int(row[6]) not in syllables:
                        syllables.append(int(row[6])) 
                    transitions.append((newsyllable, int(row[6])))
                    newsyllable = int(row[6])
        
        ### Organizing function: prototype 
        '''
        def organizer_for_axis(): 
            count = 0
            for i in syllables: 
                if i in MAIN_SYLLABLES: 
                    count+=1
            if count == len(MAIN_SYLLABLES): 
                syllables = MAIN_SYLLABLES
            else: 
                for i in range(len(MAIN_SYLLABLES)): 
                    if MAIN_SYLLABLES[i] in syllables: 
                        temp = syllables[i]
                        syllables[i] = MAIN_SYLLABLES[i]
                        syllables[syllables.index(MAIN_SYLLABLES[i])] = temp 
        '''
        
                
            
        syllables = MAIN_SYLLABLES   
         
        def y_holder(x): 
            count = 0
            for i in syllables: 
                if x == i:
                    return count
                count+=1
        
        transitions_array = np.zeros((len(syllables), len(syllables)), dtype=float)
        count0 = 0
             
        for p in syllables: 
            total = 0.0
            for q in transitions: 
                x, y = q
                if p == x: 
                    total += 1
                    transitions_array[count0][y_holder(y)] += 1
            for i in range(len(syllables)): 
                if total != 0:
                    transitions_array[count0][i] = "{:.3f}".format(transitions_array[count0][i] / total) 
            count0 += 1
            
        return transitions_array; 

def queen_matrix_compilier():      
    with open(MONSTER_MOSEQ_FILE, \
        newline='') as csvfile:
        syllablereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        syllables = []
        transitions = []
        newsyllable = 0
        count = 0
        
        for row in syllablereader: 
            if count > 0:
                newsyllable = int(row[6])
                break
            count += 1
                
        for row in syllablereader:  
            if "Queen" in row[0] or 'queen' in row[0] and "+" not in row[0]:
                if int(row[6]) != newsyllable and int(row[6]) in MAIN_SYLLABLES:
                    if int(row[6]) not in syllables:
                        syllables.append(int(row[6])) 
                    transitions.append((newsyllable, int(row[6])))
                    newsyllable = int(row[6])
        
        syllables = MAIN_SYLLABLES
         
        def y_holder(x): 
            count = 0
            for i in syllables: 
                if x == i:
                    return count
                count+=1
        
        transitions_array = np.zeros((len(syllables), len(syllables)), dtype=float)
        count0 = 0
             
        for p in syllables: 
            total = 0.0
            for q in transitions: 
                x, y = q
                if p == x: 
                    total += 1
                    transitions_array[count0][y_holder(y)] += 1
            for i in range(len(syllables)): 
                if total != 0:
                    transitions_array[count0][i] = "{:.3f}".format(transitions_array[count0][i] / total)
            count0 += 1
            
        return transitions_array; 
    
def individual_matrix_compilier():      
    with open('/Users/maximiliancomfere/transition_matrix_nakedrats /009-895-085 - baseline OF - M - DOB 6-16-2012 - 10min trim.csv', \
        newline='') as csvfile:
        syllablereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        syllables = []
        transitions = []
        newsyllable = 0
        count = 0
        
        for row in syllablereader: 
            if count > 0:
                newsyllable = int(row[0])
                break
            count += 1
                
        for row in syllablereader:  
            if int(row[0]) != newsyllable and int(row[0]) in MAIN_SYLLABLES:
                if int(row[0]) not in syllables:
                    syllables.append(int(row[0])) 
                transitions.append((newsyllable, int(row[0])))
                newsyllable = int(row[0])
         
        def y_holder(x): 
            count = 0
            for i in syllables: 
                if x == i:
                    return count
                count+=1
        
        transitions_array = np.zeros((len(syllables), len(syllables)), dtype=float)
        count0 = 0
             
        for p in syllables: 
            total = 0.0
            for q in transitions: 
                x, y = q
                if p == x: 
                    total += 1
                    transitions_array[count0][y_holder(y)] += 1
            for i in range(len(syllables)): 
                if total != 0:
                    transitions_array[count0][i] = transitions_array[count0][i] / total  
            count0 += 1
            
        return transitions_array;                  


def averageMonster_matrix_compilier():  
    file_count = 0.0
    final_average_transition_matrix = np.zeros((len(MAIN_SYLLABLES), len(MAIN_SYLLABLES)), dtype=float)   
    for filename in os.listdir(AVERAGE_MONSTER_DIRECTORY): 
        f = os.path.join(AVERAGE_MONSTER_DIRECTORY, filename)
        if os.path.isfile(f):
            with open(f, newline='') as csvfile:
                syllablereader = csv.reader(csvfile, delimiter=',', quotechar='|')
                syllables = []
                transitions = []
                newsyllable = 0
                count = 0
    
                for row in syllablereader: 
                    if count > 0:
                        newsyllable = int(row[0])
                        break
                    count += 1
                        
                for row in syllablereader:  
                    if int(row[0]) != newsyllable and int(row[0]) in MAIN_SYLLABLES:
                        if int(row[0]) not in syllables:
                            syllables.append(int(row[0])) 
                        transitions.append((newsyllable, int(row[0])))
                        newsyllable = int(row[0])
                
                def y_holder(x): 
                    count = 0
                    for i in syllables: 
                        if x == i:
                            return count
                        count+=1
                    
                transitions_matrix = np.zeros((len(syllables), len(syllables)), dtype=float)
                count0 = 0
                        
                for p in syllables: 
                    total = 0.0
                    for q in transitions: 
                        x, y = q
                        if p == x: 
                            total += 1
                            transitions_matrix[count0][y_holder(y)] += 1
                    for i in range(len(syllables)): 
                        if total != 0:
                            transitions_matrix[count0][i] = transitions_matrix[count0][i] / total  
                    count0 += 1
        file_count += 1  
        final_average_transition_matrix = np.add(final_average_transition_matrix, transitions_matrix)   
    final_average_transition_matrix = np.divide(final_average_transition_matrix, file_count) 
    return final_average_transition_matrix     
               


def runner(): 
    arrayholder = worker_matrix_compilier(); 
    print(arrayholder)
    plt.imshow(arrayholder)
    plt.xlabel("Syllables")
    plt.ylabel("Syllables")
    plt.tick_params(left = False, bottom = False)
    plt.axis('off')
    plt.colorbar()
    plt.show()
runner()

