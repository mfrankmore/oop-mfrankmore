#pragma once


namespace bling {

    class Jewelry {
        private: bool polished;

        public: Jewelry(bool _polished = true);
        public: virtual void polish();
        public: virtual void wear();

        public: virtual bool isPolished() const;

    };

}