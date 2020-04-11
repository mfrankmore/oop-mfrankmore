#pragma once

#include "jewelry.h"

#include <string.h>

namespace bling {

    class Necklace : public Jewelry {
        public: static const string DEFAULT_METAL;
        public: static const string DEFAULT_GEM;

        public: string getGem();
        public: string getMetal();
        public: void setGem();
        public: void setMetal();
    };


}