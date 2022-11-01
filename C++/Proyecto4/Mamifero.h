#ifndef MAMIFERO_H
#define MAMIFERO_H

#include <string>
using std::string;

class Mamifero{

  protected:
    string habitat;
    string sexo;
    
  public:
    Mamifero();
    Mamifero(string,string);

    ~Mamifero();

    string obtenerHabitat();
    void actualizarHabitat(string habitat);

    string obtenerSexo();
    void actualizarSexo(string sexo);
};

#endif