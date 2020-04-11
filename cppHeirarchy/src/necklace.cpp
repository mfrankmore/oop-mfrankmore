#include "necklace.h"

namespace bling {
    const string Necklace::DEFAULT_METAL = "gold";
    const string Necklace::DEFAULT_GEM = "diamond";

    string Jewelry::getGem() {
        return gem;
    }

    string Jewelry::getMetal() {
        return metal;
    }

    void Jewelry::setGem(string newGem) {
        gem = newGem;
    }

    void Jewelry::setMetal(string newMetal) {
        metal = newMetal;
    }



}