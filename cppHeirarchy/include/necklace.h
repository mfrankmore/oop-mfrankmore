#pragma once

#include <string>
#include "jewelry.h"



namespace bling {

    class Necklace : public Jewelry {
        public: static const string DEFAULT_METAL;
        public: static const string DEFAULT_GEM;
        private: static string gem;
        private: static string metal;

        public: string getGem();
        public: string getMetal();
        public: void setGem(string newGem);
        public: void setMetal(string newMetal);
    };


}