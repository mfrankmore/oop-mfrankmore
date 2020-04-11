#pragma once

#include <string>
#include "jewelry.h"


namespace bling {

    class Ring : public Jewelry {
        public: static const string DEFAULT_METAL;
        public: static const string DEFAULT_GEM;
        public: static const int DEFAULT_SIZE;
        private: static string gem;
        private: static string metal;
        private: static int size;

        public: string getGem();
        public: string getMetal();
        public: int getSize();
        public: void setGem(string newGem);
        public: void setMetal(string newMetal);
        public: void setSize(int newSize);

    };


}