#David Andres Parra Leiva y Julian David Vargas Gomez 2230047-2221885
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setleft(self, left):
        self.left = left
        return self

    def setright(self, right):
        self.right = right
        return self

def peso(tree):
    if tree is None:
        return 0
    return 1 + peso(tree.left) + peso(tree.right)

def orden(tree):
    if tree is None:
        return 0
    hijos = 0
    if tree.left: hijos += 1
    if tree.right: hijos += 1
    return max(hijos, orden(tree.left), orden(tree.right))

def altura(tree):
    if tree is None:
        return 0
    return 1 + max(altura(tree.left), altura(tree.right))

def buscarNodo(tree, valor):
    if tree is None:
        return None
    if tree.value == valor:
        return tree
    izq = buscarNodo(tree.left, valor)
    if izq:
        return izq
    return buscarNodo(tree.right, valor)

# --- Programa principal ---
print("=== CREACIÓN DE ÁRBOL ===")
valor_raiz = input("Ingrese el valor del nodo raíz: ")
raiz = Node(valor_raiz)

while True:
    print("\n--- Menú ---")
    print("1. Agregar nodo")
    print("2. Mostrar peso del árbol")
    print("3. Mostrar orden del árbol")
    print("4. Mostrar altura del árbol")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        padre_val = input("Ingrese el valor del nodo padre: ")
        nuevo_val = input("Ingrese el valor del nuevo nodo: ")
        lado = input("¿Izquierdo (i) o Derecho (d)?: ").lower()

        padre = buscarNodo(raiz, padre_val)
        if padre is None:
            print("Nodo padre no encontrado.")
        else:
            nuevo_nodo = Node(nuevo_val)
            if lado == 'i':
                if padre.left is None:
                    padre.setleft(nuevo_nodo)
                    print("Nodo agregado a la izquierda.")
                else:
                    print("Ya hay un nodo izquierdo.")
            elif lado == 'd':
                if padre.right is None:
                    padre.setright(nuevo_nodo)
                    print("Nodo agregado a la derecha.")
                else:
                    print("Ya hay un nodo derecho.")
            else:
                print("Opción no válida.")

    elif opcion == "2":
        print("Peso del árbol:", peso(raiz))

    elif opcion == "3":
        print("Orden del árbol:", orden(raiz))

    elif opcion == "4":
        print("Altura del árbol:", altura(raiz))

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
