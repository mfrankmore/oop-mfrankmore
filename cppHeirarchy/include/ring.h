#pragma once

#include <string>
#include "jewelry.h"


namespace bling {

    class Ring : public Jewelry {
        public: static const string DEFAULT_METAL;
        public: static const string DEFAULT_GEM;
        public: static const int DEFAULT_SIZE;

        public: string getGem();
        public: string getMetal();
        public: int getSize();
        public: void setGem(string metal);
        public: void setMetal(string metal);
        public: void setSize(int value);

    };


}