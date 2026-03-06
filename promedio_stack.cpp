#include <iostream>
#include <stack>

using namespace std;

double calcularPromerio(stack<double> s) {
    double suma = 0;
    int cantidad = 0;
    
    while (!s.empty()) {
        suma += s.top();
        s.pop();
        cantidad++;
    }
    
    return (cantidad > 0) ? suma / cantidad : 0;
}

int main() {
    stack<double> numeros;
    
    // Agregar números al stack
    numeros.push(10);
    numeros.push(20);
    numeros.push(30);
    numeros.push(40);
    numeros.push(50);
    
    cout << "Números en el stack: 10, 20, 30, 40, 50" << endl;
    cout << "Promedio: " << calcularPromerio(numeros) << endl;
    
    return 0;
}
