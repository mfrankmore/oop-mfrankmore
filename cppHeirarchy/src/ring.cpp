#include "ring.h"

namespace bling {

    const string Necklace::DEFAULT_METAL = "gold";
    const string Necklace::DEFAULT_GEM = "none";
    const int Necklace::DEFAULT_SIZE = 6

    string Jewelry::getGem() {
        return gem;
    }

    string Jewelry::getMetal() {
        return metal;
    }

    int Jewelry::getSize() {
        return size;
    }

    void Jewelry::setGem(string newGem) {
        gem = newGem;
    }

    void Jewelry::setMetal(string newMetal) {
        metal = newMetal;
    }

    void Jewelry::setSize(int newSize) {
        size = newSize;
    }

}