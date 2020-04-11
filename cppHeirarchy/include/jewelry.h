#pragma once


namespace go {

    class Jewelry {
        private: bool polished;

        public: Jewelry(bool _polished = true);
        public: virtual void polish();
        public: virtual void wear();

        public: virtual bool isPolished() const;

    };

}