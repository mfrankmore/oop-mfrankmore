#pragma once

#include <string>
#include "jewelry.h"



namespace bling {

    class Necklace : public Jewelry {
        public: static const string DEFAULT_METAL;
        public: static const string DEFAULT_GEM;

        public: string getGem();
        public: string getMetal();
        public: void setGem(string gem);
        public: void setMetal(string metal);
    };


}