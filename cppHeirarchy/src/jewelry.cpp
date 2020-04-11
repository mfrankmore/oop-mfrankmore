#include "jewelry.h"


namespace bling {

    Jewelry::Jewelry(bool _polished) : polished(_polished){

    }

    void Jewelry::polish(){
        polished = true;
    }
    void Jewelry::wear(){
        polished = false;
    }

    bool Jewelry::isPolished() const {
        return polished;
    }

}