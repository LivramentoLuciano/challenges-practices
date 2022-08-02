######### LeetCode Problem N°207 - Course Schedule (Medium) ################
# There are a total of numCourses courses you have to take, labeled 
# from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Constraints:
#   - 1 <= numCourses <= 2000
#   - 0 <= prerequisites.length <= 5000
#   - prerequisites[i].length == 2
#   - 0 <= ai, bi < numCourses
#   - All the pairs prerequisites[i] are unique.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        Dada una cantidad "numCourses" de Cursos a tomar, y una lista de preequisitos
        de cada uno de estos (cursos que se deben tomar para poder acceder a determinado, de a pares),
        devuelve True si es posible tomar todos los cursos, False, en caso contrario.

        >>> canFinish(2, [[1,0]])
        True
        >>> canFinish(2, [[1,0], [0,1]])
        False
        '''
        # Algoritmo
        # Se basa en el mismo concepto de recorrer un grafo, pero con la salvedad
        # de ir identificando el estado de cada Nodo (Curso): Sin Chequear, Chequeando, Listo
        # De esta manera, al visitar cada uno de los nodos:
        #   - Sin chequear: ...
        #   - Chequeando: ...
        #   - Listo: ...
        def has_loop(course):
            '''
            Devuelve True si encuentra un loop al recorrer el grafo desde  
            un curso, determinando así que no es posible tomar dicha materia.
            '''
            if state[course] == CHECKING:
                # encontró un loop
                return True
            elif state[course] == CHECKED:
                # Se recorrió sin loop
                return False 
            else:
                # estado checking
                state[course] = CHECKING
                
                # recorro los prerequisitos del curso
                for prereq in reqs_graph[course]:
                    if has_loop(prereq):
                        return True
                
                state[course] = CHECKED
                return False


        if not prerequisites: return True

        # Prerequisitos de cada curso (grafo direccionado)
        reqs_graph = { i: [] for i in range(numCourses)}
        for course,req in prerequisites:
            reqs_graph[course].append(req)

        # recorro cada curso y sus requisistos
        # -> si encuentra un bucle, quiere decir que no podría cursar esa materia
        # Estado de cada curso, al recorrer el grafo (-1:Sin chequear, 0: chequeando, 1: Completado)
        NOT_CHECKED, CHECKING, CHECKED = -1, 0, 1
        state = [ NOT_CHECKED for _ in range(numCourses) ]

        for course in reqs_graph:
            if has_loop(reqs_graph, course):
                # Encontró bucle a partir del curso -> No podrá completar las materias
                return False        

        return True


# Pruebas
test1={'numCourses': 2, 'prerequisites': [[1,0]], 'out_exp': True}
test2={'numCourses': 2, 'prerequisites': [[1,0],[0,1]], 'out_exp': False}
test3={'numCourses': 20, 'prerequisites': [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]], 'out_exp': False}
test4={'numCourses': 4, 'prerequisites': [[0,1],[3,1],[1,3],[3,2]], 'out_exp': False}
test6={'numCourses': 5, 'prerequisites': [[1,4],[2,4],[3,1],[3,2]], 'out_exp': True}
test7={'numCourses': 7, 'prerequisites': [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]], 'out_exp': True}
tests = [test1,test2, test3, test4]
tests = [test7]
for test in tests:
    res = Solution().canFinish(test['numCourses'], test['prerequisites'])
    print('numCourses: {}, prerequisites: {}... - Resultado esperado: {} - Resultado: {}'\
          .format(test['numCourses'], test['prerequisites'][:5], test['out_exp'], res))