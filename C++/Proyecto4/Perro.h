#ifndef PERRO_H
#define PERRO_H

#include "Mamifero.h"
#include <string>
using std::string;

class Perro : public Mamifero
{
  private:
    string nombrePerro;
    string razaPerro;
    string sexoPerro;
    int edadPerro;
    bool vacunasPerro;

  public:
    Perro();
    Perro(string,string,string,string,string,int,bool);

    ~Perro();

    string obtenerNombrePerro();
    void actualizarNombrePerro(string);

    string obtenerRazaPerro();
    void actualizarRazaPerro(string);

    string obtenerSexoPerro();
    void actualizarSexoPerro(string);

    int obtenerEdadPerro();
    void actualizarEdadPerro(int);

    bool obtenerVacunasPerro();
    void actualizarVacunasPerro(bool);
};

#endif