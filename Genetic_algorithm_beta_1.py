import random

class Algorithm:
    def __init__(self, input_val):
        self.input_val = input_val
        
    def return_val(input_val):
        return_val = []
        for i in range(len(input_val)):
            return_val.append(input_val[i] ** 2)

        return return_val
        
class Fitness:
    def __init__(self, genotype, fitness, start_num, end_num, bits):
        self.genotype = genotype
        self.fitness = fitness
        self.start_num = start_num
        self.end_num = end_num
        self.bits = bits
        
    def Calculate_num(genotype, start_num, end_num, bits):
        range_ = end_num - start_num
        output = []
        for i in range(len(genotype)):
            output.append(1/(2 ** bits) * range_ * genotype[i] + start_num)
        return output
    
    
class Breeder:
    def __init__(self, population, fitness, sel, length):
        self.population = population
        self.fitness = fitness
        self.sel = sel
        self.length = length

    def breed(sel, length):
        new_generation = []
        genotype = list(sel.keys())
        a = 0
        b = 0

        new_genotype = ""
        
        while len(new_generation) < length:
            a = random.randint(0, len(genotype)-1)
            b = random.randint(0, len(genotype)-1)

            new_genotype = genotype[a][:4] + genotype[b][4:]
            new_generation.append(new_genotype)

            new_genotype = ""

        return new_generation

    def mutate(population):
        mutation = 0
        for i in range(len(population)):
            mutation = random.randint(0, 100)
            if mutation == 75:
                gene = []
                temp = population[i]
                print("mutating gene: " + temp)

                for i in range(len(temp)):
                    gene.append(temp[i])
                    
                bit = random.randint(0, 7)

                if gene[bit] == "0":
                    gene[bit] = "1"
                elif gene[bit] == "1":
                    gene[bit] = "0"
                    
                temp = ""
                
                for i in range(len(gene)):
                    temp+= gene[i]
                print("gene mutated to: " + temp)

                population[i] = temp
            

    def random_selection(population, fitness, num):
        p = 0
        total_fitness = 0
        temp = 0
        selected = {}
        for i in range(len(fitness)):
            total_fitness += fitness[i]

        for _ in range(num):
            sel = 0

            while (sel == 0):
                p = random.uniform(0, total_fitness)
                temp = 0
        
                for i in range(len(fitness)):
                    temp += fitness[i]
                    if temp >= p:
                        selected[population[i]] = fitness[i]
                        population.pop(i)
                        fitness.pop(i)
                        sel = 1
                        break
                    

        return selected
class ListConverter:
    def __init__(self, population, bits):
        self.population = population
        self.bits = bits

    def ConvertToBinary(population, bits):
        for i in range(len(population)):
            population[i] = bin(population[i])[2:]
            
            while len(population[i]) < bits:
                population[i] = "0" + population[i]

        return population
    
    def Convert_to_decimal(population):
        for i in range(len(population)):
            population[i] = "0b" + population[i]
            population[i] = int(population[i], 2)
            
if __name__ == "__main__":
    pop_size = 100
    
    population = list(random.randint(0, 2 ** 8) for _ in range(pop_size))
    print("Gen 0: ")
    print(population)
    for i in range(0, 50):
        fitness = Fitness.Calculate_num(population, -10, 10, 8)
    
        fitness = Algorithm.return_val(fitness)
        population = ListConverter.ConvertToBinary(population, 8)

        selected = Breeder.random_selection(population, fitness, 50)

        population = (Breeder.breed(selected, pop_size))
        Breeder.mutate(population)
        print("Gen " + str(i) + " :")
        print(population)
        ListConverter.Convert_to_decimal(population)

